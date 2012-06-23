import redis
import time

def without_pipelining():
    now = time.time()
    r = redis.StrictRedis(host='localhost',port=6379,db=0)
    for i in range(1,10000):
        r.set('foo','bar')
    print 'in without_pipelining:', time.time()-now

def with_pipelining():
    now = time.time()
    r = redis.StrictRedis(host='localhost',port=6379,db=0)
    pipe = r.pipeline()
    for i in range(1,10000):
        pipe.set('foo','bar')
    pipe.execute()
    print 'in with_pipelining:',time.time()-now

if __name__ == "__main__":
    without_pipelining()
    with_pipelining()
