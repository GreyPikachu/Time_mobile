def write(self):
    file = open(r'Info.txt', 'a', encoding='utf-8')

    file.write(self + '\n')
