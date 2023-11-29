import sys

sys.path.append("/home/hanna/mmsegmentation")

from mmseg.registry import DATASETS
from mmseg.datasets import CustomDataset


class @Dataset(CustomDataset):
    pass


# Manually register your custom dataset
DATASETS.register_module(name="milvueDataset", module=milvueDataset)

# Print the updated DATASETS registry
print(DATASETS)
