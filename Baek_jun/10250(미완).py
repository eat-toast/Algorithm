tt = int(input())
for t in range(tt):
    h, w, n = map(int,input().split())
    print((n - 1) % h * 100 + (n - 1) // h + 101)