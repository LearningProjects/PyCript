import os
from tqdm import tqdm
import argparse


def xor_file(cript_file_path, key):
    cript_file = open(cript_file_path, 'rb')
    newFile = open('new_' + cript_file_path, 'wb')

    file_size = os.path.getsize(cript_file_path)
    file_content = cript_file.read()

    newContent = []
    for i, byte_value in tqdm(zip(range(file_size), file_content), total=file_size):
        c = key[i%len(key)]
        newContent.append(byte_value ^ ord(c))

    newFile.write(bytes(newContent))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="File path")
    ap.add_argument("-k", "--key", required=True, help="Key")
    args = vars(ap.parse_args())
    
    print('Py Crip em execução...')

    print("Arquivo para criptografar: " + args["file"])
    print("Chave: " + args["key"])

    xor_file(args["file"], args["key"])

    print("\nArquivo 'new_" + args["file"] + "' está criptografado!")


if __name__ == '__main__':
    main()