from transformers import AutoTokenizer


def decode_list(tokenizer: AutoTokenizer, code_lists: list):
    return [
        "".join(tokenizer.convert_ids_to_tokens(codes)) 
        for codes in code_lists
    ]

def clean_sequence(seq: str):
    seq = seq.replace("<s>", "")
    seq = seq.replace("<s>", "")
    seq = seq.replace("</s>", "")
    seq = seq.replace("<pad>", "")
    seq = seq.replace("▁", " ")
    seq = seq.replace("spa_Latn", "")
    seq = seq.replace("epo_Latn", "")
    return seq