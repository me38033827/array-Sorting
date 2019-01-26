import random
import Sortedness

def decrease_unsortness(n, l, r, limit):
    if r > l and limit > 0:
        pivot = random.randint(l, r)
        head = l
        tail = r - 1
        mid = n[pivot]
        n[pivot] = n[r]
        n[r] = mid
        while head < tail:
            while n[head] < mid and head < tail:
                head += 1
            while n[tail] >= mid and tail > head:
                tail -= 1
            temp = n[head]
            n[head] = n[tail]
            n[tail] = temp
        if n[head] >= mid:
            temp = n[head]
            n[head] = n[r]
            n[r] = temp
        else:
            head += 1
            temp = n[head]
            n[head] = n[r]
            n[r] = temp
        if head > 0:
            decrease_unsortness(n, l, head-1, limit-1)
        decrease_unsortness(n, head+1, r, limit-1)


def increase_unsortness(n, l, r, limit):
    if r > l and limit > 0:
        pivot = random.randint(l, r)
        head = l
        tail = r - 1
        mid = n[pivot]
        n[pivot] = n[r]
        n[r] = mid
        while head < tail:
            while n[head] >= mid and head < tail:
                head += 1
            while n[tail] < mid and tail > head:
                tail -= 1
            temp = n[head]
            n[head] = n[tail]
            n[tail] = temp
        if n[head] < mid:
            temp = n[head]
            n[head] = n[r]
            n[r] = temp
        else:
            head += 1
            temp = n[head]
            n[head] = n[r]
            n[r] = temp
        if head > 0:
            increase_unsortness(n, l, head-1, limit-1)
        increase_unsortness(n, head+1, r, limit-1)


a=[]

for i in range(100000):
    a.append(i)

increase_unsortness(a,0,99999,1)

print(Sortedness.sortCount(a,0,len(a)))

a=[]

for i in range(100000):
    a.append(i)
increase_unsortness(a,0,99999,3)
print(Sortedness.sortCount(a,0,len(a)))

a=[]

for i in range(100000):
    a.append(i)
increase_unsortness(a,0,99999,7)

print(Sortedness.sortCount(a,0,len(a)))

a=[]

for i in range(100000):
    a.append(i)
increase_unsortness(a,0,99999,10)

print(Sortedness.sortCount(a,0,len(a)))
