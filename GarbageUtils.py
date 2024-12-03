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