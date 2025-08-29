from stats import get_num_words, get_num_characters, get_sorted_num_characters  

def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        return f.read()
    
def print_report(book_path, num_words, sorted_num_char): 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("------- Character Count ---------")
    for char, count in sorted_num_char: 
        if char.isalpha(): 
            print(f"{char}: {count}")
    print("============= END ===============")


def main(): 
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_num_words(text)
    num_char = get_num_characters(text)
    sorted_num_char = get_sorted_num_characters(num_char)

    print_report(book, num_words, sorted_num_char)
    


if __name__ == "__main__":
    main()