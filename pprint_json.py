import json
import sys
import codecs


def load_data(file_path):
    json_content = codecs.open(file_path, encoding='utf-8').read()
    return json_content


def pretty_print_json(json_content):
    json_content = json.loads(json_content)
    print(json.dumps(json_content, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    file_path = sys.argv[1]
    json_content = load_data(file_path)
    pretty_print_json(json_content)
