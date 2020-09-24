import pyAesCrypt
import os


# function encryption file
def encryption(file, password):
    # size buffer
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[File '" + str(os.path.splitext(file)[0]) + "' encrypted]")

    # remove original file
    os.remove(file)


# function scanning dirs
def walking_by_dirs(dir, password):
    # перебираем все поддириктории в указвнной дирекрории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


# pathDir = input("Ведите путь к файлам которые готовы к шифрованию: ")
#
# password = input("Введите пароль для шифрования: ")
# walking_by_dirs(pathDir, password)

# C:/Users/Admin/Desktop/myTest
