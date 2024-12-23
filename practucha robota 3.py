def remove_duplicates(lst):
    """Функція для видалення дублікатів зі списку."""
    return list(set(lst))

def sort_list(lst):
    """Функція для сортування списку за умовою."""
    # Розділяємо елементи на числа та рядки
    numbers = sorted([x for x in lst if isinstance(x, (int, float))])
    strings = sorted([x for x in lst if isinstance(x, str)])
    return numbers + strings

# Вхідний список
input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

# Видаляємо дублікат
unique_list = remove_duplicates(input_list)

# Сортуємо список
sorted_list = sort_list(unique_list)

# Результат
print("Список без повторів:", unique_list)
print("Відсортований список:", sorted_list)

