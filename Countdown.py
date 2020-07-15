import sys

def main(arr):
    if(len(arr) == 0):
        ValidInput()

def ValidInput():
    print('Valid Input:\nMultiple numbers\nA Target Number\ne.g. python3 Countdown.py 2 3 4 5 100')

if __name__ == '__main__':
    main(sys.argv[1:])