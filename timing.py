def time_this(num_runs=10):
    import time
    def decortor (func): 
        def wrap():
            NUM_RUNS = num_runs
            for iter in range(NUM_RUNS):
                iter +=1
                avg_time = 0
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
                print ("Итерация-{} Время расчета: {}".format(iter, avg_time))
            avg_time /= NUM_RUNS
            return ( "Среднее время выполнения: {}".format(avg_time))
        return wrap
    return decortor
    

@time_this(num_runs=10)
def fibonachi():
    cur = 1
    prev = 0
    iter = 0
    sum_=0
    while cur <= 400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        iter += 1
        print ("{}: {}".format(iter,cur))
        cur = cur + prev
        prev = cur - prev
        sum_+=cur

print(fibonachi())