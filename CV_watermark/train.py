import torchvision
from tqdm import tqdm
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import torch
from torchvision.ops.boxes import nms
import os
import numpy as np
import cv2
import albumentations as A
import matplotlib.pyplot as plt

from preprocessing import trainloader, testloader

# Функция создания модели, где num_classes = количество предсказываемых признаков
def create_model(num_classes):
  """Функция создания модели, где num_classes = количество предсказываемых признаков:
     в случае детекции 2 признака (background, watermark)"""
  weights = torchvision.models.detection.FasterRCNN_MobileNet_V3_Large_FPN_Weights.auto
  model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_fpn(weights=weights)
  in_features = model.roi_heads.box_predictor.cls_score.in_features
  model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
  return model

# Инициализируем оборудования для вычисления
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


model = create_model(2).to(device)
params = [p for p in model.parameters() if p.requires_grad]

# Оптимизации функции выбора значения при обучении
optimizer = torch.optim.Adam(params)

# Оптимизатор процесса обучения, уменьшаем скорость обучения при отсутствии результата
lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, verbose=True, patience=2)

def train(model, optim, train_loader, valid_loader, path, num_of_epochs):
  print('Starting training')
  itr=1
  try:
    os.mkdir(path)
  except: path=path

  for epoch in tqdm(range(num_of_epochs)):
    sum_losses=[]
    validation_losses=[]

    for images, targets in train_loader:
      images = list(image.to(device) for image in images)
      targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
      loss_dict = model(images, targets)
      losses = sum(loss for loss in loss_dict.values())
      losses_value = losses.item()
      sum_losses.append(losses_value)
      optim.zero_grad()
      losses.backward()
      optim.step()
      print(losses)
    
    with torch.no_grad():
      for val_images, val_targets in valid_loader:
        val_images = list(image.to(device) for image in val_images)
        val_targets = [{k: v.to(device) for k, v in t.items()} for t in val_targets]
        val_loss_dict = model(val_images, val_targets)
    
      val_losses = sum(loss for loss in val_loss_dict.values())
      val_losses_value = val_losses.item()
      validation_losses.append(val_losses_value)


    print(f"Epoch: {epoch} , Loss: {np.mean(sum_losses)}, Validation Loss : {np.mean(validation_losses)}")

  torch.save(model.state_dict(),f"{path}/{np.mean(validation_losses)}.pt")

if __name__ == '__main__':
  train(model, optimizer, trainloader, testloader,'models', 30)
  model.eval()
  image, _ = next(iter(trainloader))
  predict = model(image)
  print(predict[0])

