from decimal import Decimal

N, K = map(int, input().split())
A = list(map(int, input().split()))


def get_min_var(A, K):
    sums = [0 for _ in range(N+1)]
    sq_sums = sums[:]
    for i in range(1, N+1):
        sums[i] = sums[i-1] + A[i-1]
        sq_sums[i] = sq_sums[i-1] + A[i-1]**2
    min_var = Decimal('INF')
    for k in range(K, N+1):
        for i in range(N-k+1):
            m = Decimal(sums[i+k] - sums[i]) / k
            var = Decimal(sq_sums[i+k] - sq_sums[i]) / k - m*m
            min_var = min(min_var, var)
    return min_var.sqrt()

print(get_min_var(A, K))