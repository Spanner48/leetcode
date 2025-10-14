import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uniq_salaries = employee.drop_duplicates(subset='salary')
    uniq_salaries['rank'] = uniq_salaries['salary'].rank(method='dense', ascending=False)

    res = uniq_salaries[uniq_salaries['rank'] == 2][['salary']]
    if len(res) == 0:
        return pd.DataFrame({f'SecondHighestSalary': [None]})

    res.rename(columns={'salary':f'SecondHighestSalary'}, inplace=True)

    return res
