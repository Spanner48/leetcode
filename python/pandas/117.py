import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniq_salaries = employee.drop_duplicates(subset='salary')
    uniq_salaries['rank'] = uniq_salaries['salary'].rank(method='dense', ascending=False)

    res = uniq_salaries[uniq_salaries['rank'] == N][['salary']]
    if len(res) == 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    res.rename(columns={'salary':f'getNthHighestSalary({N})'}, inplace=True)

    return res
