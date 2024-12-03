import os
import numpy as np 
import pandas as pd
from PIL import Image
import re
from collections import Counter
import time
import torchvision
from torchvision import datasets
from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Union
import random
from transformers import BertTokenizer
from torch.utils.data import Dataset
from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Union
from torchvision.datasets.folder import default_loader, IMG_EXTENSIONS

# initialize BertTokenizer    
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]

# use random_split to split data into train, val, and test sets
def split_dataset(dataset, test_size = 0.2, val_size = None):
    random.shuffle(dataset)
    
    data_size = len(dataset)
    val_size = test_size if val_size is None else val_size
    train_size = 1 - (test_size + val_size)

    # 0-------a---b----data_size
    a = int(data_size*train_size)
    b = int(data_size*(train_size + val_size))
    train_split = dataset[slice(0, a)]
    val_split = dataset[slice(a, b)]
    test_split = dataset[slice(b, -1)]

    return train_split, val_split, test_split


def validate_image(path):
    try:
        im = Image.open(path)
        return True
    except:
        return False