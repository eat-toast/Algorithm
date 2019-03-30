def make_sum(num_list):
    num_list = [x for x in num_list if x % 2 == 1]
    result = sum(num_list)
    return result

if __name__ == "__main__":

    N = int( input() )

    for i in range(1, N+1):
        num_list = list(map(int, input().split(' ')))
        result = make_sum(num_list)
        print('#', str(i), ' ', result, sep='')