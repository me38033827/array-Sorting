import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


####################################################################################################
#plot for data size and run time
####################################################################################################

data=pd.read_csv('data/random_datasize_time.csv')
# data=pd.read_csv('data/normal_datasize_time.csv')
# data=pd.read_csv('data/real1_datasize_time.csv')
# data=pd.read_csv('data/real2_datasize_time.csv')
#
bubbleTime=list()
mergeTime=list()
insertionTime=list()
selectTime=list()
quickTime=list()


bubbleStd=list()
mergeStd=list()
insertionStd=list()
selectStd=list()
quickStd=list()




for i in range(5):

    time4Five=0
    std=list()
    for j in range(1,6):
        time4Five+=data['bubbleSort'+str(j)][i]
        std.append(data['bubbleSort'+str(j)][i])
    bubbleStd.append(np.std(std,ddof=1))
    bubbleTime.append(time4Five/5.0)

    time4Five=0
    std=list()
    for j in range(1,6):
        time4Five+=data['mergeSort'+str(j)][i]
        std.append(data['mergeSort'+str(j)][i])
    mergeTime.append(time4Five/5.0)
    mergeStd.append(np.std(std,ddof=1))

    time4Five=0
    std=list()
    for j in range(1,6):
        time4Five+=data['insertionSort'+str(j)][i]
        std.append(data['insertionSort'+str(j)][i])
    insertionTime.append(time4Five/5.0)
    insertionStd.append(np.std(std,ddof=1))

    time4Five=0
    std=list()
    for j in range(1,6):
        time4Five+=data['quickSort'+str(j)][i]
        std.append(data['quickSort'+str(j)][i])
    quickTime.append(time4Five/5.0)
    quickStd.append(np.std(std,ddof=1))

    time4Five=0
    std=list()
    for j in range(1,6):
        time4Five+=data['selectSort'+str(j)][i]
        std.append(data['selectSort'+str(j)][i])
    selectTime.append(time4Five/5.0)
    selectStd.append(np.std(std,ddof=1))


dataSize=list()

for i in range(500,3000,500):
    dataSize.append(i)




plt.plot(dataSize,bubbleTime,'r-',label='bubble sort')
plt.plot(dataSize,mergeTime,'k-',label='merge sort')
plt.plot(dataSize,insertionTime,'g-',label='insertion sort')
plt.plot(dataSize,quickTime,'y-',label='quick sort')
plt.plot(dataSize,selectTime,'b-',label='select sort')
plt.title('Relation between data size and run time')

plt.xlabel('data size(number of elemets)')
plt.ylabel('run time(s)')
plt.legend()


#
# plt.subplot(511)
# plt.plot(dataSize,bubbleStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for bubble sort')
#
#
# plt.subplot(512)
# plt.plot(dataSize,mergeStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for merge sort')
#
# plt.subplot(513)
# plt.plot(dataSize,quickStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for quick sort')
#
# plt.subplot(514)
# plt.plot(dataSize,selectStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for select sort')
#
# plt.subplot(515)
# plt.plot(dataSize,insertionStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for insertion sort')
# #
plt.show()


####################################################################################################
#plot for sortedness and run time
####################################################################################################

# data=pd.read_csv('data/random_sortedness_time.csv')
# data=pd.read_csv('data/normal_sortedness_time.csv')
# data=pd.read_csv('data/real1_sortedness_time.csv')
# data=pd.read_csv('data/real2_sortedness_time.csv')
#
# bubbleTime=list()
# mergeTime=list()
# insertionTime=list()
# selectTime=list()
# quickTime=list()
#
#
# bubbleStd=list()
# mergeStd=list()
# insertionStd=list()
# selectStd=list()
# quickStd=list()
#
#
# sortedness=list()
#
# for i in range(39):
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['bubbleSort'+str(j)][i]
#         std.append(data['bubbleSort'+str(j)][i])
#     bubbleStd.append(np.std(std,ddof=1))
#     bubbleTime.append(time4Five/5.0)
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['mergeSort'+str(j)][i]
#         std.append(data['mergeSort'+str(j)][i])
#     mergeTime.append(time4Five/5.0)
#     mergeStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['insertionSort'+str(j)][i]
#         std.append(data['insertionSort'+str(j)][i])
#     insertionTime.append(time4Five/5.0)
#     insertionStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['quickSort'+str(j)][i]
#         std.append(data['quickSort'+str(j)][i])
#     quickTime.append(time4Five/5.0)
#     quickStd.append(np.std(std,ddof=1))

#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['selectSort'+str(j)][i]
#         std.append(data['selectSort'+str(j)][i])
#     selectTime.append(time4Five/5.0)
#     selectStd.append(np.std(std,ddof=1))
#
#
#     sortedness.append(data['sortedness'][i])
#
#
#
# plt.plot(sortedness,bubbleTime,'r-',label='bubble sort')
# plt.plot(sortedness,mergeTime,'k-',label='merge sort')
# plt.plot(sortedness,insertionTime,'g-',label='insertion sort')
# plt.plot(sortedness,quickTime,'y-',label='quick sort')
# plt.plot(sortedness,selectTime,'b-',label='select sort')
# plt.title('Relation between sortedness and run time')
#
# plt.xlabel('sortedness(number of inversions)')
# plt.ylabel('run time(s)')
# plt.legend()



# plt.subplot(511)
# plt.plot(sortedness,bubbleStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel(' bubble sort')
# plt.title('standard deviation')
#
# plt.subplot(512)
# plt.plot(sortedness,mergeStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('merge sort')
#
# plt.subplot(513)
# plt.plot(sortedness,quickStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('quick sort')
#
# plt.subplot(514)
# plt.plot(sortedness,selectStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('select sort')
#
# plt.subplot(515)
# plt.plot(sortedness,insertionStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('insertion sort')
#
# plt.show()


####################################################################################################
#plot for data size and memory usage
####################################################################################################
#
#
# data=pd.read_csv('data/random_datasize_memory.csv')
# data=pd.read_csv('data/normal_datasize_memory.csv')
# data=pd.read_csv('data/real2_datasize_memory.csv')
#
#
# bubbleMemory=list()
# mergeMemory=list()
# insertionMemory=list()
# selectMemory=list()
# quickMemory=list()
#
#
# bubbleStd=list()
# mergeStd=list()
# insertionStd=list()
# selectStd=list()
# quickStd=list()
#
#
#
#
# for i in range(39):
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['bubbleSort'+str(j)][i]
#         std.append(data['bubbleSort'+str(j)][i])
#     bubbleStd.append(np.std(std,ddof=1))
#     bubbleMemory.append(time4Five/5.0)
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['mergeSort'+str(j)][i]
#         std.append(data['mergeSort'+str(j)][i])
#     mergeMemory.append(time4Five/5.0)
#     mergeStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['insertionSort'+str(j)][i]
#         std.append(data['insertionSort'+str(j)][i])
#     insertionMemory.append(time4Five/5.0)
#     insertionStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['quickSort'+str(j)][i]
#         std.append(data['quickSort'+str(j)][i])
#     quickMemory.append(time4Five/5.0)
#     quickStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['selectSort'+str(j)][i]
#         std.append(data['selectSort'+str(j)][i])
#     selectMemory.append(time4Five/5.0)
#     selectStd.append(np.std(std,ddof=1))
#
#
# dataSize=list()
#
# for i in range(500,20000,500):
#     dataSize.append(i)



#
# plt.plot(dataSize,bubbleMemory,'r-',label='bubble sort')
# plt.plot(dataSize,mergeMemory,'k-',label='merge sort')
# plt.plot(dataSize,insertionMemory,'g-',label='insertion sort')
# plt.plot(dataSize,quickMemory,'y-',label='quick sort')
# plt.plot(dataSize,selectMemory,'b-',label='select sort')
# plt.title('Relation between data size and memory usage')
#
# plt.xlabel('data size(number of elemets)')
# plt.ylabel('memory usage(Mb)')
# plt.legend()


#
# plt.subplot(511)
# plt.plot(dataSize,bubbleStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for bubble sort')
#
#
# plt.subplot(512)
# plt.plot(dataSize,mergeStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for merge sort')
#
# plt.subplot(513)
# plt.plot(dataSize,quickStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for quick sort')
#
# plt.subplot(514)
# plt.plot(dataSize,selectStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for select sort')
#
# plt.subplot(515)
# plt.plot(dataSize,insertionStd,'-')
# plt.xlabel('data size')
# plt.ylabel('standard deviation for insertion sort')
#
# plt.show()





####################################################################################################
#plot for sortedness and memory usage
####################################################################################################

#
# # data=pd.read_csv('data/random_sortedness_memory.csv')
# data=pd.read_csv('data/real2_sortedness_memory.csv')
# # data=pd.read_csv('data/normal_sortedness_memory.csv')
#
# bubbleMemory=list()
# mergeMemory=list()
# insertionMemory=list()
# selectMemory=list()
# quickMemory=list()
#
#
# bubbleStd=list()
# mergeStd=list()
# insertionStd=list()
# selectStd=list()
# quickStd=list()
#
# sortedness=list()
#
#
# for i in range(39):
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['bubbleSort'+str(j)][i]
#         std.append(data['bubbleSort'+str(j)][i])
#     bubbleStd.append(np.std(std,ddof=1))
#     bubbleMemory.append(time4Five/5.0)
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['mergeSort'+str(j)][i]
#         std.append(data['mergeSort'+str(j)][i])
#     mergeMemory.append(time4Five/5.0)
#     mergeStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['insertionSort'+str(j)][i]
#         std.append(data['insertionSort'+str(j)][i])
#     insertionMemory.append(time4Five/5.0)
#     insertionStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['quickSort'+str(j)][i]
#         std.append(data['quickSort'+str(j)][i])
#     quickMemory.append(time4Five/5.0)
#     quickStd.append(np.std(std,ddof=1))
#
#     time4Five=0
#     std=list()
#     for j in range(1,6):
#         time4Five+=data['selectSort'+str(j)][i]
#         std.append(data['selectSort'+str(j)][i])
#     selectMemory.append(time4Five/5.0)
#     selectStd.append(np.std(std,ddof=1))
#
#     sortedness.append(data['sortedness'][i])
#


#
# plt.plot(sortedness,bubbleMemory,'r-',label='bubble sort')
# plt.plot(sortedness,mergeMemory,'k-',label='merge sort')
# plt.plot(sortedness,insertionMemory,'g-',label='insertion sort')
# plt.plot(sortedness,quickMemory,'y-',label='quick sort')
# plt.plot(sortedness,selectMemory,'b-',label='select sort')
# plt.title('Relation between sortness and memory usage')
#
# plt.xlabel('sortedness(number of inversions)')
# plt.ylabel('memory usage(Mb)')
# plt.legend()
#


# plt.subplot(511)
# plt.plot(sortedness,bubbleStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('bubble sort')
# plt.title('standard deviation')
#
# plt.subplot(512)
# plt.plot(sortedness,mergeStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('merge sort')
#
# plt.subplot(513)
# plt.plot(sortedness,quickStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('quick sort')
#
# plt.subplot(514)
# plt.plot(sortedness,selectStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('select sort')
#
# plt.subplot(515)
# plt.plot(sortedness,insertionStd,'-')
# plt.xlabel('sortedness')
# plt.ylabel('insertion sort')
#
#
#
# plt.show()

