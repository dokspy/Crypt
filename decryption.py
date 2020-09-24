import pyAesCrypt
import os


# function decryption file
def decryption(file, password):
    # size buffer
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[File '" + str(os.path.splitext(file)[0]) + "' decrypted]")

    # remove original file
    os.remove(file)


# function scanning dirs
def walking_by_dirs(dir, password):
    # перебираем все поддириктории в указвнной дирекрории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
                os.remove(path)
                print("File remove")
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)
