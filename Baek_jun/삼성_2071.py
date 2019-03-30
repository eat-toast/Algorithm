def make_maen(num_list):
    aa = sum(num_list)
    average_ = aa // 10

    if aa % 10 >= 5:
        average_ += 1

    return average_


if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        num_list = list(map(int, input().split(' ')))
        aa = make_maen(num_list)
        print('#', str(i + 1), ' ', aa, sep='')