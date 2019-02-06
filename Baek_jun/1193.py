N = int(input())

step = 0
while(1):
    if step * (step+1) / 2 < N <= (step+1) * (step+2) / 2 :
        if step%2 == 0 : # 짝수
            mo = step+1 - ( (step+1) * (step+2) / 2 - N )
            ja = 1 + ( (step+1) * (step+2) / 2 - N )
            print( str(int(ja)) + '/' + str(int(mo)))
        else: # 짝수
            mo = 1 +  ((step + 1) * (step + 2) / 2 - N)
            ja = step+1 - ((step + 1) * (step + 2) / 2 - N)
            print(str(int(ja)) + '/' + str(int(mo)))
        break
    else:
        step += 1