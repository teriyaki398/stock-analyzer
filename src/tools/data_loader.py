from pathlib import Path

def load_financial_results(sc, save_dir_path, key):
    path = Path(save_dir_path, key)

    with open(str(path)) as f:
        all_data_list = f.read().split('\n')
    return select_data_by_sc(sc, all_data_list)

"""
return list data extracted by sc
"""
def select_data_by_sc(sc, all_data_list):
    for data_str in all_data_list:
        data = [d.replace('"', '') for d in data_str.split(",")]
        if str(sc) == data[0]:
            return data
