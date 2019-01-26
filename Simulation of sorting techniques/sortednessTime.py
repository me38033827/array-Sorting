import sortTech
import numpy as np
import time
import pandas as pd
import generateSortness as gs
import Sortedness as sn

import sys

sys.setrecursionlimit(3000000)


data=pd.read_csv('data/winemag-data-130k-v2.csv')
a=list(data['points'])[0:10001]


sortTime=dict()


for i in range(1,6):
    sortTime['bubbleSort'+str(i)]=list()
    sortTime['insertionSort'+str(i)]=list()
    sortTime['selectSort'+str(i)]=list()
    sortTime['quickSort'+str(i)]=list()
    sortTime['mergeSort'+str(i)]=list()


sortedness=list()

# a=np.random.normal(5000,5000,10000)
sortTech.mergeSort(a,0,len(a))


for i in range(250,10000,250):
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


        t1=time.time()
        sortTech.bubbleSort(a1)
        t2=time.time()
        sortTime['bubbleSort'+str(j)].append(t2-t1)
        print 'bubble',j


        t1=time.time()
        sortTech.insertionSort(a2)
        t2=time.time()
        sortTime['insertionSort'+str(j)].append(t2-t1)
        print 'insertion',j


        t1=time.time()
        sortTech.selectSort(a3)
        t2=time.time()
        sortTime['selectSort'+str(j)].append(t2-t1)
        print 'select',j


        t1=time.time()
        sortTech.quickSort(a4,0,len(a4)-1)
        t2=time.time()
        sortTime['quickSort'+str(j)].append(t2-t1)
        print 'quick',j

        t1=time.time()
        sortTech.mergeSort(a5,0,len(a5))
        t2=time.time()
        sortTime['mergeSort'+str(j)].append(t2-t1)
        print 'merge',j


sortTime['sortedness']=sortedness




df=pd.DataFrame(data=sortTime)


df.to_csv('data/real2_sortedness_time.csv')


