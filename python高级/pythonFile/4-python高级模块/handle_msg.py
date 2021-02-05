from common import RECV_DATA_LIST
# from common import HANDLE_FLAG 此时只是仅仅指向import模块中变量的值
import common


def handle_data():
    print("--->handle_data")
    for i in RECV_DATA_LIST:
        print(i)
    common.HANDLE_FLAG = True


def test_handle_data():
    print("--->test_handle_data")
    if common.HANDLE_FLAG:
        print("处理完成")
    else:
        print("未处理完成")