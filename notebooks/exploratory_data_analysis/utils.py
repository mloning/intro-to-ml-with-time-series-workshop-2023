#!/usr/bin/env python3 -u
# coding: utf-8

__author__ = ["mloning"]
__all__ = ["load_pressure", "load_temperature", "load_experiments"]

import pandas as pd
from typing import Union, Optional


def _load_data() -> pd.DataFrame:
    """Helper function to load data for workshop.

    References
    ----------
    The data is a small extract from the Tennessee Eastman Process Simulation Data
    for Anomaly Detection. The full data set is available at:
    https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6C3JR1
    """
    return pd.read_csv("./data/chemical_process_data.csv", index_col=0, header=[0, 1])


def _load_single_series(name: str) -> pd.Series:
    data = _load_data()
    series = data.loc[1, name].reset_index(drop=True)
    series.name = name
    return series


def load_experiments(variables: Optional[list[str]]=None) -> Union[pd.Series, pd.DataFrame]:
    data = _load_data()
    if variables is not None:
        return data.loc[:, variables]
    return data


def load_pressure() -> pd.Series:
    return _load_single_series("pressure")


def load_temperature() -> pd.Series:
    return _load_single_series("temperature")
