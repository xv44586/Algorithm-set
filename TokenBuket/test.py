import time
from buket import Token


def test():
    result1 = [Token().get_token() for i in range(15)]
    result2 = [Token().get_token() for i in range(10)]
    time.sleep(5)
    result3 = [Token().get_token() for i in range(10)]
    time.sleep(5)
    result4 = [Token().get_token() for i in range(10)]

    print('result1:', result1)
    print('result2:', result2)
    print('result3', result3)
    print('result4', result4)


if __name__ == '__main__':
    test()