from matplotlib import pyplot as plt
import numpy as np
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import torch
import cv2
import albumentations as A
from train import create_model, device
from preprocessing import testloader
import matplotlib.pyplot as plt
import nms
from preprocessing import DatasetTest, inf_transform
from torch.utils.data import DataLoader
from albumentations.pytorch.transforms import ToTensorV2




model = create_model(2).to(device)
model.load_state_dict(torch.load(r'models/mobile320_new.pt'))
model.eval()
# images, targets = next(iter(testloader))
# images = torch.stack(images).to(device)
# print(images)
# outputs = model(images)
# print(outputs)
TEST_IMAGE_PATH = r'images/true/page_4.png'

test = DataLoader(DatasetTest(TEST_IMAGE_PATH, augmentation=inf_transform()))
test = next(iter(test))

def displayImage(image, boxes=None):
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))

    if boxes is not None:
        cv2.rectangle(image,
                        (boxes[0], boxes[1]),
                        (boxes[2], boxes[3]),
                        (220, 0, 0), 3)
        # cv2.rectangle(image,
        #                 (orig_boxes[0], orig_boxes[1]),
        #                 (orig_boxes[2], orig_boxes[3]),
        #                 (0.0, 255.0, 0.0), 3)
    

    ## EXPERIMENTAL
    # ind = nms(predict[0]['boxes'], predict[0]['scores'], IOU_TRESHOLD).detach().cpu().numpy()
    # for i, box in enumerate(predict[0]['boxes'][ind]):
    #     if predict[0]['scores'][i] > THRESHOLD:
    #         cv2.rectangle(image, 
    #                 (int(box[0]), int(box[1])), 
    #                 (int(box[2]), int(box[3])), 
    #                 (255, 0, 0), 5)

    ax.set_axis_off()
    ax.imshow(image)
    ax.set_title(msg)

    plt.show()


# images, targets = next(iter(testloader))

# orig_boxes = targets[0]['boxes'].cpu().numpy().astype(np.int32)[0]

image = test[0].permute(1, 2, 0).cpu().numpy()

predict = model(test)

msg = None
print(predict)
print(image)
IOU_TRESHOLD = 0.1 
THRESHOLD = 0.2
print([(torch.Tensor.tolist(t['boxes']), torch.Tensor.tolist(t['scores'])) for t in predict])

try:
    boxes = predict[0]['boxes'][0]
    boxes = torch.Tensor.tolist(boxes)
    boxes = [int(i) for i in boxes]
    print(boxes)
except IndexError:
    msg = 'BBox not detected'

print(displayImage(image))
