
import psutil
import os


info = psutil.virtual_memory()
print 'memory usage',psutil.Process(os.getpid()).memory_info().rss,'byte'
print 'total memory',info.total,'byte'
print 'portion of memory',info.percent
print 'number of CPU',psutil.cpu_count()



