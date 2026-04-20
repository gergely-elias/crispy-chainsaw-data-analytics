import pandas as pd
import pytest

from crispy_chainsaw_data_analytics.column_statistics import (
    calculate_max_of_column,
    calculate_min_of_column,
)


@pytest.fixture
def sample_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "column1": [
                1,
                2,
                3,
                4,
                5,
            ],
            "column2": [
                10,
                20,
                30,
                40,
                50,
            ],
        }
    )


def test_calculate_min_of_column(sample_data: pd.DataFrame) -> None:
    assert calculate_min_of_column(sample_data, "column1") == 1
    assert calculate_min_of_column(sample_data, "column2") == 10


def test_calculate_max_of_column(sample_data: pd.DataFrame) -> None:
    assert calculate_max_of_column(sample_data, "column1") == 5
    assert calculate_max_of_column(sample_data, "column2") == 50
