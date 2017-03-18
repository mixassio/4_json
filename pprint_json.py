import json, os, chardet, codecs
import pprint


def load_data(filepath):
    if os.path.exists(filepath):
        char_type = chardet.detect(open(filepath, "rb").read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as fh:
            return json.load(fh)



def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    data_alkoshops = load_data('alkoshops.json')
    print(pretty_print_json(data_alkoshops))
