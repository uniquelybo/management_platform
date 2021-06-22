import pandas as pd


def read_excel(data):
    rows = data.shape[0]
    dicts = {}
    keys = data.columns.values
    for row in range(0, rows):
        dict_key = {}
        for key in keys:
            value = data[key][row]
            if pd.isnull(value):
                dict_key[key] = ""
            else:
                dict_key[key] = str(value)
        dicts["data_%d" % row] = dict_key
    return dicts
