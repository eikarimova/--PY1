import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(cvs_file, new_line='\n', delimiter=',') -> list[dict]:
    with open(cvs_file, 'r') as f:
        list_ = []
        headline = f.readline().strip(new_line).split(delimiter)
        [list_.append(dict(zip(headline, line.strip(new_line).split(delimiter)))) for line in f]
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
