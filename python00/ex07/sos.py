import sys

NESTED_MORSE = {
    "A": ".- ",
	"B": "-... ",
	"C": "-.-. ",
	"D": "-.. ",
	"E": ". ",
	"F": "..-. ",
	"G": "--. ",
	"H": ".... ",
	"I": ".. ",
	"J": ".--- ",
	"K": "-.- ",
	"L": ".-.. ",
	"M": "-- ",
	"N": "-. ",
	"O": "--- ",
	"P": ".--. ",
	"Q": "--.- ",
	"R": ".-. ",
	"S": "... ",
	"T": "- ",
	"U": "..- ",
	"V": "...- ",
	"W": ".-- ",
	"X": "-..- ",
	"Y": "-.-- ",
	"Z": "--.. ",
	"0": "----- ",
	"1": ".---- ",
	"2": "..--- ",
	"3": "...-- ",
	"4": "....- ",
	"5": "..... ",
	"6": "-.... ",
	"7": "--... ",
	"8": "---.. ",
	"9": "----. ",
	" ": "/ "
}

def encode_to_morse(input_string):
    assert isinstance(input_string, str), "Argument must be a string."
    input_string = input_string.upper()
    encoded_string = ''.join([NESTED_MORSE[char] for char in input_string if char in NESTED_MORSE])
    return encoded_string.strip()

def main():
    if len(sys.argv) != 2:
        raise AssertionError("The program requires exactly 1 argument.")
    input_string = sys.argv[1]
    encoded_string = encode_to_morse(input_string)
    print(encoded_string)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
