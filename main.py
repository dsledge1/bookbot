from stats import *

def main():
    #count=wordcount("./books/frankenstein.txt")
    #print(f"{count} words found in the document")
    #print(cc("./books/frankenstein.txt"))
    #sorted=dict_sorter("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount("./books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    for dict in dict_sorter("./books/frankenstein.txt"):
        if dict['char'].isalpha() == True:
                print(f"{dict['char']}: {dict['count']}")

main()        