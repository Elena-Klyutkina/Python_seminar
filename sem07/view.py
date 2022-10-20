def get_name():
    with open('file.txt', 'r',encoding="utf-8") as f:
        for line in f.readlines()[:1]:
            return (line.rstrip('\n'))
        

def get_number():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[1:2]:
            return (line.rstrip('\n'))

def what_to_do():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[2:]:
            return (line.rstrip('\n'))


def export_book(book: dict):
    with open('newfile.txt','a',encoding="utf-8") as newfile:
        newfile.writelines(f"{book}")
        newfile.writelines('\n')