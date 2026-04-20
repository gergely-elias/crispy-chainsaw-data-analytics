import pandas as pd


def calculate_max_of_column(df: pd.DataFrame, column: str) -> float:
    """Calculate the maximum value of a column in a DataFrame.

    Args:
        df: Input data.
        column: Column name.

    Returns:
        Maximum value of the column.
    """
    return df[column].max()


def calculate_min_of_column(df: pd.DataFrame, column: str) -> float:
    """Calculate the minimum value of a column in a DataFrame.

    Args:
        df: Input data.
        column: Column name.

    Returns:
        Minimum value of the column.
    """
    return df[column].min()
