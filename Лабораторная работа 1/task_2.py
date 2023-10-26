# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024
numbers_of_page = 100
numbers_of_rows = 50
numbers_of_symbol = 25
volume_of_one_symbol = 4

volume = volume_of_one_symbol * numbers_of_page * numbers_of_rows * numbers_of_symbol

numbers_book = disk // volume
print("Количество книг, помещающихся на дискету:", int(numbers_book))

