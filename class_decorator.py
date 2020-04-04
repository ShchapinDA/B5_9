import time
from functools import wraps

class time_this(object):
    def __init__(self, n):
        self.n = n
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def __call__(self, f):
        @wraps(f)
        def wrap():
            NUM_RUNS = self.n
            for iter in range(NUM_RUNS):
                iter +=1
                avg_time = 0
                t0 = time.time()
                f()
                t1 = time.time()
                avg_time += (t1 - t0)
                print ("Итерация-{} Время расчета: {}".format(iter, avg_time))
            avg_time /= NUM_RUNS
            return "Среднее время выполнения: {}".format(avg_time)
        return wrap
    
@time_this(10)
def fibonachi():
    cur = 1
    prev = 0
    iter = 0
    sum_=0
    while cur <= 400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        iter += 1
        #print ("{}: {}".format(iter,cur))
        cur = cur + prev
        prev = cur - prev
        sum_+=cur

with time_this(10):
    print(fibonachi())



