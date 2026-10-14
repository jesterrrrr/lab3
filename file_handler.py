class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Записано в {self.filename}")

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.read()

    def append(self, text):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(text)
        print(f"Дописано в {self.filename}")

    def clear(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write('')
        print(f"Файл {self.filename} очищен")


if __name__ == '__main__':
    fh = FileHandler('test.txt')
    fh.write("Привет, мир!\n")
    fh.append("Вторая строка\n")
    print(fh.read())
    fh.clear()
