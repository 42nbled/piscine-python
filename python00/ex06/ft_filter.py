def ft_filter(function, iterable):
	for item in iterable:
		if function(item):
			yield item

def is_even(n):
    return n % 2 == 0

def main():
	numbers = [1, 2, 3, 4, 5, 6]
	filtered_builtin = filter(is_even, numbers)
	print(list(filtered_builtin))

	filtered_custom = ft_filter(is_even, numbers)
	print(list(filtered_custom))

	for i in ft_filter(is_even, numbers):
		print(i)

	print(filtered_custom.__getattribute__)
	print(filtered_custom.__iter__)
	print(filtered_custom.__next__)
	print(filtered_custom.__reduce__)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
