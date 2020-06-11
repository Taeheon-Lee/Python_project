import sys

class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = open(filename, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.index = []
        self.data = []
        self.result = []
        self.corrupted = self.parses()

    def parses(self):
        file = list(list(elem.split(self.sep)) for elem in list(self.file))
        index_num = len(file[0])
        i = 0
        for elem in file:
            self.data.append(list(line.strip() for line in elem))
            if len(self.data[i]) != index_num:
                return (True)
            i += 1
        if self.header:
            self.index.append(self.data.pop(0))
        return (False)

    def getdata(self):
        start = 0
        end = len(self.data)
        if self.skip_top != 0:
            start += 1
        if self.skip_bottom != 0:
            end -= 1
        for i in range(start, end):
            self.result.append(self.data[i])
        return (self.result)

    def getheader(self):
        if self.header:
            return (self.index)
        else:
            return (self.data[0])

    def __enter__(self):
        if self.corrupted is True:
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        raise Exception("Too many arguments")
    with CsvReader(sys.argv[1], skip_top=1) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
