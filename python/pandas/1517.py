import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\\.com$'
    res = users[users['mail'].str.match(regex)]

    return res
