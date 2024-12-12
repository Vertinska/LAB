import os
import glob
import shutil

def find(name_part, search_path="."):
    search_pattern = os.path.join(search_path, f"*{name_part}*")
    found_files = glob.glob(search_pattern, recursive=True)
    if found_files:
        print("Найденные файлы:")
        for file in found_files:
            print(os.path.abspath(file))
    else:
        print("Файлы не найдены.")

def rename(old_path, new_name):
    if not os.path.exists(old_path):
        print("Указанный путь не существует.")
        return

    dir_name = os.path.dirname(old_path)
    new_path = os.path.join(dir_name, new_name)

    try:
        os.rename(old_path, new_path)
        print(f"Переименование успешно: {old_path} -> {new_path}")
    except Exception as e:
        print(f"Ошибка при переименовании: {e}")

def move(src_path, dest_path):
    """Перемещает файл или папку."""
    if not os.path.exists(src_path):
        print("Источник не существует.")
        return

    try:
        shutil.move(src_path, dest_path)
        print(f"Перемещение успешно: {src_path} -> {dest_path}")
    except Exception as e:
        print(f"Ошибка при перемещении: {e}")

def main():
    while True:
        print("\nФайловый менеджер:")
        print("3 - Найти файл/файлы")
        print("7 - Переименовать файл/папку")
        print("9 - Переместить файл/папку")
        print("0 - Выйти")

        choice = input("Выберите действие: ")

        if choice == "3":
            name_part = input("Введите полное имя или часть имени файла: ")
            search_path = input("Введите путь для поиска (оставьте пустым для текущей папки): ") or "."
            find(name_part, search_path)

        elif choice == "7":
            old_path = input("Введите путь к файлу/папке для переименования: ")
            new_name = input("Введите новое имя: ")
            rename(old_path, new_name)

        elif choice == "9":
            src_path = input("Введите путь к файлу/папке для перемещения: ")
            dest_path = input("Введите новый путь: ")
            move(src_path, dest_path)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()