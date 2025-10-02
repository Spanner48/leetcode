import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    # count files that have at least 1 (one) occurance of:
    # 'bull' OR 'bear'
    # also count number of appereances for each word

    bull_regex = r'(\s+bull\s+)'
    bear_regex = r'(\s+bear\s+)'

    bull_count = files[files['content'].str.contains(bull_regex, regex=True, case=False)]['file_name'].nunique()
    bear_count = files[files['content'].str.contains(bear_regex, regex=True, case=False)]['file_name'].nunique()

    df = pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]
    })

    return df
