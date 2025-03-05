from stats import *
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")     
    sys.exit(1)

def main():
    #count=wordcount("./books/frankenstein.txt")
    #print(f"{count} words found in the document")
    #print(cc("./books/frankenstein.txt"))
    #sorted=dict_sorter("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for dict in dict_sorter(sys.argv[1]):
        if dict['char'].isalpha() == True:
                print(f"{dict['char']}: {dict['count']}")

main()        