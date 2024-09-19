# prints text into terminal
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    print(text)

# gets book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# gets word count
def count_words_in_book(file_path):
    text = get_book_text(file_path)
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

file_path = 'books/frankenstein.txt'
word_count = count_words_in_book(file_path)
print(word_count)
