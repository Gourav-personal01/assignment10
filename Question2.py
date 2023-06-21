# Threading Module is bascially used to provide the functionality of using Multithreading option in python

# 1. Active Count - It Return the number of Thread objects currently alive.
# 2. Current Thread - It Return the number of Thread objects currently alive.
# 3. enumurate - It Return a list of all Thread objects currently alive.

#Example 
import threading
a = threading.enumerate()
b = threading.active_count()
c = threading.current_thread()
print(a)
print(b)
print(c)