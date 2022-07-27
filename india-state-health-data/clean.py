import pandas as pd
from pandas import DataFrame

def read_file(xlsx_path: str, sheet_name: int|str = 0, header: int = 0) -> DataFrame:

    df = pd.read_excel(xlsx_path, sheet_name=sheet_name, header=header)

    return df

