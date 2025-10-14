import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    res = patients[patients['conditions'].str.startswith(r'DIAB1') | patients['conditions'].str.contains(r' DIAB1')]

    return res
