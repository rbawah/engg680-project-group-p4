import torch
import torch.nn as nn
from torchvision.models import (inception_v3, 
                                Inception_V3_Weights,
                                mobilenet_v2, 
                                MobileNet_V2_Weights)
from transformers import BertTokenizer, BertForSequenceClassification


def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False
