
import time
import src.request

def get_payload(path):
    try:
        with open(path, 'r') as f:
            payload = f.readlines()
        return payload
    except FileNotFoundError:
        print(f"File '{path}' doesn't exist.")
        return []

def get_default_headers(path):
    map = {}
    with open(path, 'r') as f:
        for ligne in f:
            key, value = ligne.strip().split(": ")
            map[key] = value
    return map


def conform_path(path):
    if path[0] == '/' and path[-1] == '/':
        return path[1:-1]
    elif path[0] == '/':
        return path[1:]
    elif path[-1] == '/':
        return path[:-1]
    else:
        return path

def conform_payload(path, payload):
    new_array = []

    for string in payload:
        new_string = string.replace("admin", path)
        new_array.append(new_string)
    return new_array

