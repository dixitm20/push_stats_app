import json
import os


def get_stats_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def get_success_brand_list(path):
    out_list = []
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                input_json_dict = json.loads(line.strip())
                out_list.append(input_json_dict['brand'])
        return out_list


def get_input_stats(path):
    with open(path) as f:
        for line in f:
            input_json_dict = json.loads(line.strip())
            yield input_json_dict
