import json, os, chardet, codecs
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_json:
            char_type = chardet.detect(file_json.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_json:
            return json.load(file_json)



def pretty_print_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    try:
        if sys.argv[1]:
            data_alkoshops = load_data(sys.argv[1])
            print(pretty_print_json(data_alkoshops))
    except IndexError:
        print('input path to file')
