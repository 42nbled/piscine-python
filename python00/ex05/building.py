import sys
import string

def count_characters(input_text):
    counts = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in input_text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1

    return counts

def main():
    if len(sys.argv) > 2:
        raise AssertionError("More than one argument provided.")

    if len(sys.argv) == 2:
        input_text = sys.argv[1]
    else:
        input_text = input("What is the text to count?\n")

    counts = count_characters(input_text)
    total_chars = len(input_text)

    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

if __name__ == "__main__":
    main()
