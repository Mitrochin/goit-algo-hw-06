from main import *

# Создание адресной книжки
book = AddressBook()

# Создание записи для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Добавление записи John в адресную книгу
book.add_record(john_record)

# Создание и добавление новой записи для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Вывод всех записей в книге
for name, record in book.data.items():
    print(f"{record}")

# Поиск и редактирование телефона John
john = book.find("John")
print(john)

john.edit_phone("1234567890", "1112223333")
print(john)

# Поиск конкретного телефона John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")

# Удаление записи Jane
book.delete("Jane")

# Вывод всех записей в книге после удаления Jane
for name, record in book.data.items():
    print(f"{record}")
