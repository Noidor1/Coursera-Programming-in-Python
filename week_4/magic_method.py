import os.path
import tempfile

class File:

    def __init__(self, file_path=None):
        self.file_path = file_path
        try:
            open(self.file_path, 'r')
        except FileNotFoundError:
            with open(self.file_path, 'w') as f:
                pass

    def read(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as filen:
                return filen.read()
        else:
            raise FileNotFoundError

    def write(self, user_str):
        with open(self.file_path, 'w') as q:
            q.write(user_str)


    def __add__(self, obj):
        with open('test.log', 'r') as a, open_file('testcon.log', 'r') as b:
            f_1 = a.readline()
            f_2 = b.readline()

        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'w') as f:
            f.write(f_1 + f_2)

        return File(storage_path)

    def __str__(self):
        return os.path.abspath(self.file_path)
    
    def __iter__(self):
        yield from open(self.file_path)
    
    def __next__(self):
        curr_str = 0
        with open(self.file_path, 'r') as f:
            str = f.readlines()[curr_str]
        curr_str += 1
        if str == '':
            raise StopIteration
        return str


