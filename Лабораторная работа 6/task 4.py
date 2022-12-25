import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_file) -> list[dict]:
    with open(csv_file) as f:
        list_ = []
        lines = [line.rstrip() for line in f]
        headline = lines[0].split(',')
        for line in lines[1:]:
            list_.append(dict(zip(headline, line.split(','))))
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
