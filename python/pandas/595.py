import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res_df = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    res_df = res_df[['name', 'population', 'area']]

    return res_df