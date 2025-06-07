import sys
from stats import word_count, sort_on, char_count, report_stats, print_report
#import stats

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    #path_to_file = input("Enter file path: ")
    try:
        if not sys.argv[1]:
            raise ValueError("Usage: python3 main.py <path_to_book>")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(sys.argv[1])
    count = word_count(text)
    
    print_report(report_stats(text), count)

main ()