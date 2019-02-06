# K means
import numpy as np
import copy
import matplotlib.pyplot as plt

k = 2   # 군집 수
n = 100 # 데이터 갯수
np.random.seed(n+2)

data = np.random.rand(n, 2)
x = data[:,0]
y = data[:,1]

init = np.random.rand(k, 2)

center = np.zeros(shape = (n,k))

# 초기 중심점( 단, cluster의 갯수가 k개 아니라면, k개 될때까지 랜덤으로 init를 배치)
while(1):
    for i, cent in enumerate(init) :
        diff = cent - data
        center[:,i] = np.sum(diff**2, axis = 1) # sqrt는 생략한다.

    cluster = np.array([ np.argmin(center[i]) for i in range(len(center)) ] )

    unique_cluster = np.unique(cluster)

    if len( unique_cluster  ) != k :
        cluster = np.random.randint(0, k, n)
    unique_cluster = np.unique(cluster)

    if len (unique_cluster) == k:
        break

# 군집별 중심점(평균)을 찾는다.
for i in range(k):
    idx = np.where(cluster == i)[0]
    init[i] = np.mean(data[idx,:], axis = 0)

# init가 바뀌지 않을 때 까지 반복한다.
epoch = 0
while(1):
    old_init = copy.deepcopy(init)
    for i, cent in enumerate(init):
        diff = cent - data
        center[:, i] = np.sum(diff ** 2, axis=1)  # sqrt는 생략한다.

    cluster = np.array([np.argmin(center[i]) for i in range(len(center))])

    # 군집별 중심점(평균)을 찾는다.
    for i in range(k):
        idx = np.where(cluster == i)[0]
        init[i] = np.mean(data[idx, :], axis=0)

    condition = old_init == init
    condition = condition.reshape(( condition.size, ))
    if all(condition) :
        break
    else:
        print( '지금은 {}'.format(epoch))
    epoch += 1


plt.scatter(x,y,s=50,marker='D',c='b')
plt.scatter(init[:,0],init[:,1],s=50,marker='D',c='r')
plt.show()
