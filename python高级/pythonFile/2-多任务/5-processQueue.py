import multiprocessing


def download_from_web(q):
    data = [11, 22, 33, 44]
    for i in data:
        q.put(i)
    print("Download successfully")


def analysis_data(q):
    dataList = list()
    while q.empty() is False:
        data = q.get()
        dataList.append(data)
    print(dataList)


def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
