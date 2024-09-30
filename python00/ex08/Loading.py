def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 50

    for i, elem in enumerate(lst):
        percent = (i + 1) / total
        bar_fill = '█' * int(percent * bar_length)
        bar_empty = ' ' * (bar_length - len(bar_fill))
        percent_display = int(percent * 100)

        progress_bar = f"{percent_display: >3}%|{bar_fill}{bar_empty}| {i + 1}/{total}"

        print(f"\r{progress_bar}", end='', flush=True)
        yield elem
    print()  # Move to the next line after completion
