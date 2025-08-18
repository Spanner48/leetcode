import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # filter animals that weigh >100kg
    # return sorted by weight DESC

    df = animals[animals['weight'] > 100]
    df = df.sort_values(by='weight', ascending=False)
    df = df[['name']]

    return df
