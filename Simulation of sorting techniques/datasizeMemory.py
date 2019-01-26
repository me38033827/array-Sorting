import sortTech
import numpy as np
import pandas as pd
import memory_profiler as mp


import sys

sys.setrecursionlimit(3000000)


data=pd.read_csv('data/winemag-data-130k-v2.csv')
a=list(data['points'])[0:20001]


sortMemory=dict()


for i in range(1,6):
    sortMemory['bubbleSort'+str(i)]=list()
    sortMemory['insertionSort'+str(i)]=list()
    sortMemory['selectSort'+str(i)]=list()
    sortMemory['quickSort'+str(i)]=list()
    sortMemory['mergeSort'+str(i)]=list()

dataSize=list()

for i in range(500,20000,500):
    print i

    dataSize.append(i)


    for j in range(1,6):
        # a=np.random.randint(low=0, high=15000, size=i)
        # a=np.random.normal(5000,5000,i)
        b=a[0:i]
        a1=b
        a2=b
        a3=b
        a4=b
        a5=b


        sortMemory['bubbleSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.bubbleSort,(a1,)))))

        sortMemory['insertionSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.insertionSort,(a2,)))))

        sortMemory['selectSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.selectSort,(a3,)))))

        sortMemory['quickSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.quickSort,(a4,0,len(a4)-1,)))))

        sortMemory['mergeSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.mergeSort,(a5,0,len(a5),)))))




sortMemory['dataSize']=dataSize




df=pd.DataFrame(data=sortMemory)


df.to_csv('data/real2_datasize_memory.csv')


