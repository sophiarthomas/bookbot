
def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        return f.read()

def get_num_words(text): 
    words = text.split()
    return len(words)

def main(): 
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)

    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()