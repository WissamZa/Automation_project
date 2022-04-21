import json
import os
import sys
import clipboard


def clipsave():
    key = input("Input key for your clip:")
    value = clipboard.paste()
    data = load_json()
    add_json(data, key, value)


def get():
    data = load_json()
    key = input('Enter the key of the value you want to copy it to the clipboard:\n')
    if key in data:
        clipboard.copy(data[key])
        print(f'{{{data[key]}}} save into the clipboard')
    else:
        print(f'The key {key} not found')

def add_json(data, key, value):
    data[key]=value
    with open("./items.json", "w") as file:
        json.dump(data, file)
    print(f"{{{value}}}added successfuly to items.json as {{{key}}} as a key")


def load_json():
    file_path = './items.json'
    if os.path.exists(file_path):
        with open("./items.json", "r") as file:
            data = json.load(file)
    else:
        data={}
    return data
  
command = 'g'
match command:
    case 's'|'S':
        clipsave()
    case 'g'|'G':
        get()
    case 'l'|'L':
        print(load_json())
    case default:
        print("Wrong keyword")
