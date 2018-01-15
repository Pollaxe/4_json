import json
import sys
import codecs


def load_data(filepath):
    data = codecs.open(filepath, encoding='utf-8').read()
    return data


def pretty_print_json(data):
    data = json.loads(data)
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    filepath = sys.argv[1]
    data = load_data(filepath)
    pretty_print_json(data)
