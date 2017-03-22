import argparse
import json, os, chardet, codecs
import sys

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('filepath')
    return parser


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_json:
            char_type = chardet.detect(file_json.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_json:
            return json.load(file_json)



def pretty_print_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


if __name__ == '__main__':
<<<<<<< HEAD
    parser = create_parser()
    namespace = parser.parse_args()
    data_alkoshops = load_data(namespace.filepath)
    print(pretty_print_json(data_alkoshops))

=======
    try:
        if sys.argv[1]:
            data_alkoshops = load_data(sys.argv[1])
            print(pretty_print_json(data_alkoshops))
    except IndexError:
        print('input path to file')
>>>>>>> 045091021dd15549881acbeb6e509db49d7e22d2
