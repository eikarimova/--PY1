from random import randint


def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    unique_figure = []
    unique_numbers = ([randint(-10, 10) for _ in range(15)])
    for numbers in unique_numbers:
        if numbers in unique_figure:
            continue
        else:
            unique_figure.append(numbers)
    return unique_figure


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
