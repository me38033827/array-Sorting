import numpy as np
import time
#Bubble Sort

def bubbleSort(a):
    length=len(a)
    temp=0
    flag=1
    while(flag==1):             #if flag=0, then there is no change in the preivous loop. the sort can finish.
        flag=0
        for i in range(length-1):              #two loop to bubble sort
            for j in range(length-i-1):
                if a[j]>a[j+1]:
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
                    flag=1

    return a



#Insertion Sort

def insertionSort(a):
    length=len(a)

    for i in range(1,length):
        cur=a[i]                            #use cur to store the element waiting for insertion
        j=i-1
        while(j>=0 and a[j]>cur ):      #the inner loop break when reaching the first element smaller than cur
            a[j+1]=a[j]
            j-=1

        a[j+1]=cur
    return a


#Selection sort

def selectSort(a):
    length=len(a)

    for i in range(length-1):
        k=i
        for j in range(i+1,length):
            if(a[j]<a[k]):
                k=j
        if(i!=k):
            temp=a[i]
            a[i]=a[k]
            a[k]=temp

    return a




#Quick sort

def quickSort(a,begin,end):
    if(begin<end):
        k=partition(a,begin,end)
        quickSort(a,begin,k-1)
        quickSort(a,k+1,end)

    return a


def partition(a,begin,end):
    i=begin
    j=end
    temp=a[begin]

    while(i<j):
        while(i<j and a[j]>temp):
            j-=1
        if(i<j):
            a[i]=a[j]
            i+=1
        while(i<j and a[i]<temp):
            i+=1
        if(i<j):
            a[j]=a[i]
            j-=1
    a[i]=temp

    return i


#Merge sort

def mergeSort(a,begin,end):
    if(end-begin<2):
        return
    mid=(begin+end)/2

    mergeSort(a,begin,mid)
    mergeSort(a,mid,end)

    merge(a,begin,mid,end)
    return a


def merge(a,begin,mid,end):
    i=begin
    j=mid
    k=0

    b=list()

    while i<mid and j<end:
        if a[i]<a[j]:
            b.append(a[i])
            i+=1
        else:
            b.append(a[j])
            j+=1

    while i<mid:
        b.append(a[i])
        i+=1

    while j<end:
        b.append(a[j])
        j+=1

    i=begin
    k=0

    while i<end:
        a[i]=b[k]
        k+=1
        i+=1







# a=np.random.randint(low=0, high=10000, size=5000)
# print a
#
# t1=time.time()
#
# print bubbleSort(a)
# print time.time()-t1
#
#
# a=[4,2,5,1,4,6,7,0,-2,-3,1,4,5,6,0]
# print insertionSort(a)
#
# a=[4,2,5,1,4,6,7,0,-2,-3,1,4,5,6,0]
# print selectSort(a)
#
# a=[4,2,5,1,4,6,7,0,-2,-3,1,4,5,6,0]
# print quickSort(a,0,len(a)-1)
#
# a=[4,2,5,1,4,6,7,0,-2,-3,1,4,5,6,0]
# print mergeSort(a,0,len(a))
#
