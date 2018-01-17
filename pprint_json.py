import json
import sys
import codecs


def load_data(file_path):
    json_content = codecs.open(file_path, encoding='utf-8').read()
    return json_content


def pretty_print_json(json_content):
    json_decoded = json.loads(json_content)
    print(json.dumps(json_decoded, sort_keys=True, ensure_ascii=False,
                     indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        json_content = load_data(file_path)
        pretty_print_json(json_content)
    except IndexError:
        try:
            file_path = input('Please input filename:')
            json_content = load_data(file_path)
            pretty_print_json(json_content)
        except FileNotFoundError:
            print('File not found, please try again.')
    except FileNotFoundError:
        print('File not found, please try again.')