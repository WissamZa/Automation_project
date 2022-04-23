import json
import os
import clipboard

class multi_clip:
    # def __init__(self) -> None:

    #     command = 's'
    #     match command:
    #         case 's' | 'S':
    #             self.clipsave()
    #         case 'g' | 'G':
    #             self.get()
    #         case 'l' | 'L':
    #             print(self.load_json())
    #         case default:
    #             print("Wrong keyword")

    def clipsave(self):
        key = input("Input key for your clip:")
        value = clipboard.paste()
        data = self.load_json()
        return self.add_json(data, key, value)

    def get(self):
        data = self.load_json()
        key = input('Enter the key of the value you want to copy it to the clipboard:\n')
        if key in data:
            clipboard.copy(data[key])
            print(f'{{{data[key]}}} save into the clipboard')
        else:
            print(f'The key {key} not found')

    def add_json(self,data, key, value):
        data[key]=value
        with open("./items.json", "w") as file:
            json.dump(data, file)
        print(f"{{{value}}} added successfuly to items.json as {{{key}}} as a key")
        return value

    def load_json(self):
        file_path = './items.json'
        if os.path.exists(file_path):
            with open("./items.json", "r") as file:
                data = json.load(file)
        else:
            data={}
        return data
    
if __name__=='__main__':
    multi_clip()
      
