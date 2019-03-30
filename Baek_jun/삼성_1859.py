def gen():
    yield list(map(int, input().split(' ')))

def solve(num_list,profit):

    max_num = max(num_list)
    max_idx = [idx for idx, x in enumerate(num_list) if x == max_num][0]

    while len(num_list) > 0:
        if max_idx == 0:
            num_list = num_list[max_idx + 1:]

        elif start_index == max_idx:
            num_list = []
        else:
            buy = sum(num_list[start_index:max_idx])
            sell = num_list[max_idx] * (max_idx - start_index) - buy
            profit += sell

            num_list = num_list[max_idx + 1:]
            if len(num_list) == 0:
                break
            else:
                max_num = max(num_list)
                max_idx = [idx for idx, x in enumerate(num_list) if x == max_num][0]

    return profit

if __name__ == "__main__":
    T = int(input())

    # 반복문 시작
    for x in range(T):
        N = int(input())

        start_index = 0
        end_index = N - 1
        mile_stone = 0
        profit = 0

        for num_list in gen():
            profit = solve(num_list, profit)
            print('#', str(x + 1), ' ', profit, sep='')