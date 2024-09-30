import sys

def words_longer_than_n(S, N):
	assert isinstance(S, str), "First argument must be a string."
	assert isinstance(N, int), "Second argument must be an integer."

	words = S.split()

	longer_words = list(filter(lambda word: len(word) > N, words))

	return longer_words

def main():
	if len(sys.argv) != 3:
		raise AssertionError("The program requires exactly 2 arguments.")

	S = sys.argv[1]
	try:
		N = int(sys.argv[2])
	except ValueError:
		raise AssertionError("Second argument must be an integer.")

	result = words_longer_than_n(S, N)
	print(result)

if __name__ == "__main__":
	try:
		main()
	except Exception as error:
		print(error)
