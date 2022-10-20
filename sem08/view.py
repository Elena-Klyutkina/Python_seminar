def get_name():
    with open('file.txt', 'r',encoding="utf-8") as f:
        for line in f.readlines()[:1]:
            return (line.rstrip('\n'))
        

def get_position():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[1:2]:
            return (line.rstrip('\n'))

def what_to_do():
    with open('file.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines()[2:]:
            return (line.rstrip('\n'))


def export_catalog(catalog: dict):
    with open('newfile.txt','a',encoding="utf-8") as newfile:
        newfile.writelines(f"{catalog}")
        newfile.writelines('\n')