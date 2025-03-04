def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def wordcount(file):
    textlist =[]
    with open(file) as f:
        textlist += get_book_text(file).split()
        wc=len(textlist)
        return wc
