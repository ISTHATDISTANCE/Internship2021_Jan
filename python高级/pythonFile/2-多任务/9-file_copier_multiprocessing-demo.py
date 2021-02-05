import os
from multiprocessing import Pool, Manager


def copy_file(q, file_name, old_file_name, new_file_name):
    # print("copying from %s to %s: %s" % (old_file_name, new_file_name, file_name))
    old_f = open(old_file_name + '/' + file_name, 'rb')
    content = old_f.read()
    old_f.close()
    new_f = open(new_file_name + '/' + file_name, 'wb')
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def print_bar(copied, file_num):
    print('\r', end='')
    for i in range(int(50 * copied / file_num)):
        print("*", end='')
    print("%.2f%%" % (copied * 100 / file_num), end='')

def main():
    # 获取要拷贝的文件夹名
    old_folder_name = input("Please enter the old folder name: ")
    # 获取要创建的文件夹名
    new_folder_name = input("Please enter the new folder name: ")
    # 创建新文件夹，存在则pass
    try:
        os.mkdir(new_folder_name)
    except:
        pass

    #  获取要文件夹中的所有文件名 listdir()
    file_names = os.listdir(old_folder_name)

    #  创建进程池
    po = Pool(5)

    # 如果用进程池，则要用Manage()中的Queue()
    q = Manager().Queue()
    # 向进程池中添加copy任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    #  子进程开始复制文件
    file_num = len(file_names)
    copied = 0
    while copied < file_num:
        file_name = q.get()
        # print("copy complete: %s" % file_name)
        copied += 1
        print_bar(copied, file_num)
    print('\n')

if __name__ == "__main__":
    main()
