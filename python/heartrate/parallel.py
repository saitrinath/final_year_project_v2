from multiprocessing import Process
import time
def func1():
	print('func1: starting')
	for i in range(10000000): pass
	print('func1: finishing')

def func2():
	print('func2: starting')
	for i in range(10000000): pass
	print ('func2: finishing')


p1 = Process(target=func1)
p1.start()
p2 = Process(target=func2)
p2.start()
time.sleep(.5)
print('processes started successfullyy')
p1.join()
p2.join()
print('done')
