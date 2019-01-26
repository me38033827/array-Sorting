# a=[1,2,3,4,5,6,7,8,9,10]
# b=[9,8,7,6,5,4,3,2,1]
#
# c=[1,2,3,4,5,6,7,8,10,9]



def sortCount(a,begin,end):
    length=len(a)


    if(end-begin<2):
        return 0
    else:
        mid=(begin+end)/2
        a1=sortCount(a,begin,mid)
        a2=sortCount(a,mid,end)
        r=mergeCount(a,begin,mid,end)

    return a1+a2+r

def mergeCount(a,begin,mid,end):
    count=0


    i=begin
    j=mid

    while i<mid and j<end:
        if a[i]>a[j]:
            count+=(mid-i)
            j+=1
        else:
            i+=1

    return count

#
#
# a1=c
# print sortCount(a1,0,len(a1))
