def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(pos)
    print(neg)
    print(zero)

    print(format(pos / len(arr), ".6f"))
    print(format(neg / len(arr), ".6f"))
    print(format(zero / len(arr), ".6f"))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))[:n]
    plusMinus(arr)
