def solve(num_list):

    profit = 0 # 사재기로 획득한 이득

    while len(num_list) > 1:
        max_num = max(num_list)
        max_idx = num_list.index(max_num)

        if max_idx == 0:
            num_list.pop(0)

        else:
            buy = sum(num_list[:max_idx])
            sell = num_list[max_idx] * max_idx - buy
            profit += sell
            num_list = num_list[max_idx + 1:]

    return profit

if __name__ == "__main__":
    T = int(input())

    # 반복문 시작
    for x in range(T):
        N = int(input())
        num_list = list(map(int, input().split(' ')))

        profit = solve(num_list)

        print('#', str(x + 1), ' ', profit, sep='')