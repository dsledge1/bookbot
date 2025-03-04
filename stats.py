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
    
def charcount(file):
    charlist=list(get_book_text(file))
    char1=len(charlist)
    return char1
   

def cc(file):
    cd ={}
    with open(file) as f:
        tl=get_book_text(file).lower()
        characters = list(tl)
        for c in tl:
            cd.update({c:0})
        for c in tl:
            cd[c]+=1
        return cd

        #return characters    
