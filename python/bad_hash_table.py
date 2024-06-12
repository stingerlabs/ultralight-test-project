class BadHashTable():
    def __init__(self):
        self.dict = dict()

    def insert(self, key: str, val: any):
        self.dict[key] = val
    
    def get(self, key: str):
        if key in self.dict:
            return self.dict[key]
        raise KeyError("Couldn't find the key")

if __name__ == "__main__":
    hash_table = BadHashTable()
    hash_table.insert('hi', 'hello')
    hash_table.get('hi')