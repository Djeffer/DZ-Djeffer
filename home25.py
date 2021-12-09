import os, os.path

#  Задание №1

file = r'test_dir\f1\4.txt'
if os.path.exists(file):
    f1 = os.path.basename(file)
    f2 = os.path.dirname(file)
    f3 = os.path.getctime(file)
    print(f'{f1} ({f2}) - last access time {f3} sec')
else:
    print("File not found")

#  Задание №2

path = r'test_dir'
files = os.listdir(path)
files = list(map(lambda i: os.path.join(path, i), files))
print(files)

s = sorted(files, key=os.path.isfile, reverse=True)
print(s)

#  Задание №3
empty = r'test_dir/mtfile'


def print_nonempty_files(root, topdown):
    for root, dirs, files in os.walk(root, topdown=topdown):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > 0:
                print(f"{file_path} - {file_size} bytes")


def move_empty_files(root, dir):
    for root, dirs, files in os.walk(root):
        if root == dir:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                os.rename(file_path, os.path.join(dir, file))
                print(f"{file} moved from {root} to {dir}")


print_nonempty_files('test_dir', topdown=True)
os.makedirs(empty)
move_empty_files('test_dir', empty)
