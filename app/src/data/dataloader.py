from torch.utils.data import Dataset

class TranslationDataset(Dataset):
    def __init__(self, tokenized_list):
        self.tokenized_list = tokenized_list
    
    def __len__(self):
        return len(self.tokenized_list)
    
    def __getitem__(self, idx):
        return self.tokenized_list[idx]
