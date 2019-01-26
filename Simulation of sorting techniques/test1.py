import sortTech
import numpy as np
import time
import pandas as pd

import sys

sys.setrecursionlimit(3000000)

# data=pd.read_csv('data/winemag-data-130k-v2.csv')c
# a=list(data['points'])[0:15001]

sortTime=dict()


for i in range(1,6):
    sortTime['bubbleSort'+str(i)]=list()
    sortTime['insertionSort'+str(i)]=list()
    sortTime['selectSort'+str(i)]=list()
    sortTime['quickSort'+str(i)]=list()
    sortTime['mergeSort'+str(i)]=list()

dataSize=list()

for i in range(500,3000,500):
    print i

    dataSize.append(i)


    for j in range(1,6):
        a=np.random.randint(low=0, high=30000, size=i)
        # a=np.random.normal(5000,5000,i)
        # b=a[0:i]

        a1=a.copy()
        a2=a.copy()
        a3=a.copy()
        a4=a.copy()
        a5=a.copy()

        t1=time.time()
        sortTech.bubbleSort(a1)
        t2=time.time()
        sortTime['bubbleSort'+str(j)].append(t2-t1)


        t1=time.time()
        sortTech.insertionSort(a2)
        t2=time.time()

        sortTime['insertionSort'+str(j)].append(t2-t1)

        t1=time.time()
        sortTech.selectSort(a3)
        t2=time.time()
        sortTime['selectSort'+str(j)].append(t2-t1)


        t1=time.time()
        sortTech.quickSort(a4,0,len(a4)-1)
        t2=time.time()
        sortTime['quickSort'+str(j)].append(t2-t1)

        t1=time.time()
        sortTech.mergeSort(a5,0,len(a5))
        t2=time.time()
        sortTime['mergeSort'+str(j)].append(t2-t1)


sortTime['dataSize']=dataSize




df=pd.DataFrame(data=sortTime)


df.to_csv('data/random_datasize_time.csv')


