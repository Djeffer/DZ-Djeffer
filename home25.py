import os

#  Задание №1

# file = r'test_dir\f1\4.txt'
# if os.path.exists(file):
#     f1 = os.path.basename(file)
#     f2 = os.path.dirname(file)
#     f3 = os.path.getctime(file)
#     print(f'{f1} ({f2}) - last access time {f3} sec')
# else:
#     print("File not found")

#  Задание №2

# files = r'test_dir'
# f1 = os.listdir(files)
# print(f"{f1}")



# path = r'test_dir'
# for dirs, folder, files in os.walk(path):
#     f1 = dirs
#     f2 = folder
#     f3 = files


#  Задание №3


def print_free(root):
    for rot, dirs, files in os.walk(root, topdown=True):
        if rot == root:
            for i in dirs:
                print(i)
            for j in files:
                print(j, os.path.getsize(rot + "\\" + j), 'byte')


print_free(r'test_dir')
