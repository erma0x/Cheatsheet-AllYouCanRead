import threading
import time
import schedule

def job(g):
    print('c')
    t=time.clock()
    print(t)
    return(g+2)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(2).seconds.do(run_threaded, job(0))


while 1:
    schedule.run_pending()
    time.sleep(1)
