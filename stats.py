def word_count(text):
    count = 0
    cuts = text.split()
    #print(cuts)
    for words in cuts:
        count += 1
    #print(f"{count} words found in the document")
    return count

def char_count(text):
    count = {}
    char_list = list(text.lower())
    for char in char_list:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return(count)

def report_stats(text):
    count = word_count(text)
    unsorted_char_count = char_count(text)
    sorted_char_count = []
    
    for charac in unsorted_char_count:
	    sorted_char_count.append({
		    	"char": charac,
			    "num": unsorted_char_count[charac]
			    })
    
    return sorted_char_count

def sort_on(sorted_char_count):
	return sorted_char_count["num"]

def print_report(sorted_char_count, count):
    sorted_char_count.sort(reverse=True, key=sort_on)

    print("=========== BOOKBOT ===========")
    print("Analyzing book found at books/Frankenstein.txt...")
    print("---------- Word Count ---------")
    print(f"Found {count} total words")
    print("------- Character Count -------")
    for char in sorted_char_count:
	    if char["char"].isalpha():
		    print(f"{char["char"]}: {char["num"]}")
    print("=============END===============")