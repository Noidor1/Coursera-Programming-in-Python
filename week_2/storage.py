import os
import argparse
import json
import tempfile

def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    
    with open(storage_path, "r") as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}

def write_data(storage_path, data):
    with open(storage_path, "w") as f:
        f.write(json.dumps(data, indent=4))

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="key_name", type=str)
    parser.add_argument("--value", help="dict_value", type=str)
    return parser.parse_args()    

def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)

def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])

def main(storage_path):
    args = parse()

    if args.key and args.value:
        put(storage_path, args.key, args.value)
    elif args.key:
        print(*get(storage_path, args.key), sep=", ")
    else:
        print("The program is called with invalid parameters.")


if __name__ == "__main__":
    storage_path = os.path.join(tempfile.gettempdir(), 
                                'storage.data')
    main(storage_path)
