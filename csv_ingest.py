#!python3

import pandas


def ingest(filename):
    df = pandas.read_csv(filename)
    return df
