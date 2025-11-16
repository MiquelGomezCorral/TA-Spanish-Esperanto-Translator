from torch.utils.data import Dataset

class TranslationDataset(Dataset):
    def __init__(self, tokenized_list):
        self.tokenized_list = tokenized_list
    
    def __len__(self):
        return len(self.tokenized_list)
    
    def __getitem__(self, idx):
        return self.tokenized_list[idx]


class HuggingFaceDatasetWrapper(Dataset):
    """Wrapper to make HuggingFace datasets compatible with PyTorch DataLoader
    
    
    Args:
        dataset: HuggingFace Dataset or dict-like object with tokenized data
        split: Optional split name ('train', 'validation', 'test') if using HF datasets
    """
    def __init__(self, dataset, split=None):
        # If it's a dict-like with splits (HuggingFace DatasetDict)
        if split and hasattr(dataset, '__getitem__') and split in dataset:
            self.dataset = dataset[split]
        else:
            self.dataset = dataset
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        item = self.dataset[idx]
        return {
            'input_ids': item['input_ids'],
            'attention_mask': item['attention_mask'],
            'labels': item.get('labels', item['input_ids'])  
        }
