from random import randint


def get_unique_list_numbers(start: int, stop: int, length: int) -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    unique_figures = []
    while len(unique_figures) < length:
        unique_figure = randint(start, stop)
        if unique_figure not in unique_figures:
           unique_figures.append(unique_figure)
    return unique_figures


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
