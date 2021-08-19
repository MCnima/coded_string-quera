import coder
import sys


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    string = sys.argv[3]
    if n and k >= 1:
        if n and k <= 100:
            pass
    else:
        print('Massage or repeat times is to big.\nTake it easy!!')
    coder.last_first(k, string)


if __name__ == '__main__':
    main()
