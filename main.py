import sys
from stats import num_words
from stats import letter_count
from stats import sort_letters
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
def main():
    contents = get_book_text(sys.argv[1])
    num = num_words(contents)
    count_dict = letter_count(contents)
    sorted_chars = sort_letters(count_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count -----------')
    print(f"Found {num} total words")
    print('--------- Character Count ---------')
    for key in sorted_chars: 
        if key['char'].isalpha():
            print(f'{key['char']}: {key['count']}')
    print('=============== END ===============')
    return
def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

main()

