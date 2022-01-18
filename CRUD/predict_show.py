import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
classes = ('M0', 'M1')
num_classes = len(classes)
mean_nums = [0.485, 0.456, 0.406]
std_nums = [0.229, 0.224, 0.225]

transform = {
    'Test': transforms.Compose([
        transforms.Resize([224, 224]),
        transforms.ToTensor(),
        transforms.Normalize(mean_nums, std_nums)
    ])
}


def resnet50_pth(num_classes, pth):
    """获取预训练模型
    num_classes : 类别数量
    """
    model = models.resnet50()
    num_features = model.fc.in_features  # 全连接层的特征
    model.fc = nn.Linear(num_features, num_classes)
    model.load_state_dict(torch.load(pth, map_location='cpu'))
    return model


def predict(model, img_path):
    model.eval()
    torch.no_grad()
    img = Image.open(img_path)
    img = transform['Test'](img).unsqueeze(0).to(device)
    outputs = model(img)
    _, predicted = torch.max(outputs, 1)
    return classes[predicted[0]]


if __name__ == '__main__':
    predict_result = predict(resnet50_pth(num_classes, 'res_sgd_pre.pth').to(device),
                             'F:/桌面软件/学习/课设4/课程设计训练集影像/M1/000842537-rk.jpg')
    print('Predict :', predict_result)