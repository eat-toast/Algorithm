N = int( input() )

step = 1
old_num = 1

if N == 1:
    print(1)
else:
    while(1):
        max_num = 6*step + old_num
        if old_num < N <= max_num:
            print(step+1)
            break
        else:
            step += 1
            old_num = max_num