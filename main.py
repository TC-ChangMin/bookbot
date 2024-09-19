# prints text into terminal
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_words_in_book(text)
    histogram = letters_histogram(text)
    print(num_words)
    print(histogram)

# gets book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# makes a histogram of each letter
def letters_histogram(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

# gets word count
def get_words_in_book(text):
    words = text.split()
    return len(words)

main()