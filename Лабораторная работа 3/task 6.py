list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
last_max_index = 0
last_max_number = list_numbers[last_max_index]

for i, current_number in enumerate(list_numbers):
    last_max_number = list_numbers[last_max_index]
    if current_number >= last_max_number:
        last_max_index = i
        last_max_number = list_numbers[last_max_index]
last_index = list_numbers[-1]
list_numbers[last_max_index], list_numbers[-1] = list_numbers[-1], list_numbers[last_max_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
