from audioop import tostereo
from pathlib import Path
import albumentations as A
import numpy as np
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torch
import glob
import cv2
from sklearn.model_selection import train_test_split
from albumentations.pytorch.transforms import ToTensorV2
from re import search

# Фикс сортировки python по названию файла
sort_path = [x[0] for x in sorted([(x, int(search(r'(\d+).png$', x).groups()[0])) 
             for x in glob.glob(r'images\true\*.png')], key=lambda x: x[1])]

# Открываем файл с разметкой в формате [[xmin, ymin, xmax, ymax]]
with open(r'images/bbox.txt', 'r') as f:
    list_bboxes = [eval(s) for s in f.readlines()]


# Собираем набор данных
df = pd.DataFrame(data={'img_path': sort_path, 'bbox': list_bboxes})
train_df, test_df = train_test_split(df, test_size=0.2)
train_df = train_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)


# Функции аугментации изображений
def transform():
    return A.Compose([
    A.RandomBrightnessContrast(p=0.2),  
    A.GaussianBlur(p=0.2),             # добавляем размытие                            
    A.HorizontalFlip(p=0.3),                        # отзеркаливаем
    A.Flip(p=0.3),                                  # переворачиваем на 180
    A.Rotate(p=0.5, value=1, limit=8),
    A.HueSaturationValue(p=0.2),
    # A.PixelDropout(p=0.2),
    # A.RandomGamma(p=0.2),
    A.ToSepia(p=0.2),             # поворачиваем до угла 45 с шагом 5
    A.Resize(768, 512),                              # приводим формат к единому
    ToTensorV2(p=1)                                 # переводим результаты в тензор для вычислений
                      ], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['labels']))

def inf_transform():
    return A.Compose([
        A.Resize(height=768, width=512),
        ToTensorV2(p=1)
    ])

class DatasetTest(Dataset):
    def __init__(self, path, augmentation=None):
        self.path = path
        self.augmentation = augmentation
    
    def __len__(self):
        return 1
    
    def __getitem__(self, index):
        image_path = self.path
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        if self.augmentation is not None:
            aug = self.augmentation(image=image)
            image = aug['image']
        
        return image



# Преобразуем родительский класс pytorch Dataset
class DatasetAug(Dataset):
    def __init__(self, dataframe, augmentation=None):
        self.dataframe = dataframe
        self.augmentation = augmentation
        
    def __len__(self) -> int:
        return self.dataframe.shape[0]
    
    def __getitem__(self, index: int):
        df_index = self.dataframe.iloc[index]

        # Считываем изображение
        image_path = df_index['img_path']
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    
        # Определяем баундбоксы
        bbox = df_index['bbox']

        if self.augmentation is not None:
            aug = self.augmentation(image=image, bboxes=bbox, labels=[1])
            image, bbox, labels = aug['image'], aug['bboxes'], aug['labels']

        # Так, как на обучение у нас только положительные значение, то label = 1
        labels = torch.Tensor([1]).to(torch.int64)


        bbox = torch.as_tensor(bbox, dtype=torch.float32)

        # Не понял для чего :(
        iscrowd = torch.zeros_like(labels, dtype=torch.int64)

        # Вычислим область внутри баундбокса
        # area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
        # area = torch.as_tensor(area, dtype=torch.float32)

        target = {}
        target['boxes'] = bbox
        target['labels'] = labels
        # target['area'] = area
        target['iscrowd'] = iscrowd

        # image = torch.from_numpy(image).permute(2, 1, 0)
            
        return image, target

dover_train = DatasetAug(train_df, transform())
dover_test = DatasetAug(test_df, transform())


def collate_fn(batch):
    return tuple(zip(*batch))


trainloader = DataLoader(dover_train, shuffle=True, collate_fn=collate_fn, batch_size=8)
testloader = DataLoader(dover_test, shuffle=True, collate_fn=collate_fn, batch_size=8)


# Для тестирование препроцессинга с помощью визуализации
 
# import matplotlib.pyplot as plt


# images, targets = next(iter(trainloader))

# boxes = targets[0]['boxes'].cpu().numpy().astype(np.int32)[0]
# image = images[0].permute(1,2,0).cpu().numpy()
# print(boxes)
# print(image)
# def displayImage(image, boxes):
#     fig, ax = plt.subplots(1, 1, figsize=(16, 8))

#     cv2.rectangle(image,
#                     (boxes[0], boxes[1]),
#                     (boxes[2], boxes[3]),
#                     (220, 0, 0), 3)

#     ax.set_axis_off()
#     ax.imshow(image)

#     plt.show()

# print(displayImage(image, boxes))