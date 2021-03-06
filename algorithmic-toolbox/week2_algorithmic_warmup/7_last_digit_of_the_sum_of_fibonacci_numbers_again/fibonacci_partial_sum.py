# Uses python3
import sys


def fib_sum_last(n):
    lis = [0, 1]
    if n > 60:
        n = (n%60) + 60
    while n > 0:
        lis.append(lis[-1]%10 + lis[-2]%10)
        lis.remove(lis[0])
        n = n-1
    sum = (lis[-1]%10 + lis[-2]%10)%10
    if sum == 0:
        return 9
    else:
        return sum - 1


def fib_sum_again(m, n):
    res = fib_sum_last(n) - fib_sum_last(m-1)
    if res < 0:
        res = 10 + res
    return res

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_sum_again(from_, to))
