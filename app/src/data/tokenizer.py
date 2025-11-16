import pandas as pd 
from tqdm.auto import tqdm
tqdm.pandas()

def tokenize_dataframe(df: pd.DataFrame, src_col: str, tgt_col: str, tokenizer):
    def tokenize_row(row):
        tokens = tokenizer(
            str(row[src_col]),
            text_target=str(row[tgt_col]),
        )
        return tokens
    return df.progress_apply(tokenize_row, axis=1)
