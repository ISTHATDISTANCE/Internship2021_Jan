from common import RECV_DATA_LIST
import common


def recv_msg():
    print("--->recv_msg")
    for i in range(5):
        RECV_DATA_LIST.append(i)


def test_recv_msg():
    print("--->test_recv_msg")
    print(RECV_DATA_LIST)


def recv_msg_next():
    print("--->recv_msg_next")
    if common.HANDLE_FLAG:
        print("处理完成，可以接受数据……")
    else:
        print("处理未完成，等待中……")