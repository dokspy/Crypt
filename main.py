import encryption
import decryption


def main(change):

    if change == 1:
        pathDir = input("Ведите путь к файлам которые готовы к шифрованию: ")
        password = input("Введите пароль для шифрования: ")
        encryption.walking_by_dirs(pathDir, password)
    elif change == 2:
        pathDir = input("Ведите путь к файлам которые готовы к дешифрованию: ")
        password = input("Введите пароль для дешифрования: ")
        decryption.walking_by_dirs(pathDir, password)
    else:
        print("Ошибка")


print("Выберете что вы хотите сделать: ")
print("Выберете 1 если хотите шифровать файлы.")
print("Выберете 2 если хотите дешифровать файлы.")

number_for_change = int(input("Выбирайте что хотите сделать: "))
main(number_for_change)
