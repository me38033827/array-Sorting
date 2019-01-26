import sortTech
import numpy as np
import time
import pandas as pd
import generateSortness as gs
import Sortedness as sn
import memory_profiler as mp
import sys
import psutil

sys.setrecursionlimit(3000000)

data=pd.read_csv('data/winemag-data-130k-v2.csv')
a=list(data['points'])[0:20000]

sortMemory=dict()


for i in range(1,6):
    sortMemory['bubbleSort'+str(i)]=list()
    sortMemory['insertionSort'+str(i)]=list()
    sortMemory['selectSort'+str(i)]=list()
    sortMemory['quickSort'+str(i)]=list()
    sortMemory['mergeSort'+str(i)]=list()


sortedness=list()

# a=np.random.normal(10000,10000,20000)
sortTech.mergeSort(a,0,len(a))


for i in range(500,20000,500):
    print i

    gs.increase_unsortness(a,0,i,1)
    sortedness.append(sn.sortCount(a,0,len(a)))
    print sn.sortCount(a,0,len(a))
    a1=a
    a2=a
    a3=a
    a4=a
    a5=a


    for j in range(1,6):


        sortMemory['bubbleSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.bubbleSort,(a1,)))))


        sortMemory['insertionSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.insertionSort,(a2,)))))

        sortMemory['selectSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.selectSort,(a3,)))))

        sortMemory['quickSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.quickSort,(a4,0,len(a4)-1,)))))

        sortMemory['mergeSort'+str(j)].append(np.mean(mp.memory_usage((sortTech.mergeSort,(a5,0,len(a5),)))))



sortMemory['sortedness']=sortedness




df=pd.DataFrame(data=sortMemory)


df.to_csv('data/real2_sortedness_memory.csv')


