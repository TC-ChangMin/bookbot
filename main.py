# prints text into terminal
def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_words_in_book(text)
    histogram = letters_histogram(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for key, val in histogram.items():
        print(f"The '{key}' character was found {val} times")
    print("--- End report ---")
    
# gets book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# makes a histogram of each letter sorted from higheset frequency to lowest
def letters_histogram(text):
    #creates the histogram
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Sort the dictionary by values in descending order using dict() and sorted()
    #creates a list of tuples. list is sorted by the using the "key" parameter in sorted(). key is set to the 2nd value in item, item[1]
    # lambda creates a temp function with the parameter item. it then returns item[1]. because we have a list of tuples, item[1] is the 2nd value of each tuple
    sorted_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

# gets word count
def get_words_in_book(text):
    words = text.split()
    return len(words)

main()