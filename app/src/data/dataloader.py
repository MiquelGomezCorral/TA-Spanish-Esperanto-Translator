from torch.utils.data import Dataset

class TranslationDataset(Dataset):
    def __init__(self, dataframe, tokenizer, src_col, tgt_col, max_length=128):
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.src_col = src_col
        self.tgt_col = tgt_col
        self.max_length = max_length
    
    def __len__(self):
        return len(self.dataframe)
    
    def __getitem__(self, idx):
        source = self.dataframe.iloc[idx][self.src_col]
        target = self.dataframe.iloc[idx][self.tgt_col]
        
        # Tokenize
        inputs = self.tokenizer(
            source,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(
                target,
                max_length=self.max_length,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )
        
        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': labels['input_ids'].squeeze()
        }
    

class TranslationDatasetLLM(Dataset):
    def __init__(self, dataframe, tokenizer, src_col, tgt_col, task_prefix, max_length=128):
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.src_col = src_col
        self.tgt_col = tgt_col
        self.task_prefix = task_prefix
        self.max_length = max_length
    
    def __len__(self):
        return len(self.dataframe)
    
    def __getitem__(self, idx):
        source = self.dataframe.iloc[idx][self.src_col]
        target = self.dataframe.iloc[idx][self.tgt_col]
        
        # print(f"Source: {source}")
        # print(f"Prefix: {self.task_prefix}")
        # Tokenize
        inputs = self.tokenizer(
            self.task_prefix + str(source),
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(
                target,
                max_length=self.max_length,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )
        
        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': labels['input_ids'].squeeze()
        }