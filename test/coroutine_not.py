def consumer(a):
    if  a != '':
        print('[CONSUMER] Consuming %s...' % a)
        print('[PRODUCER] Consumer return: %s' % '200 OK')

def produce(c):
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        c(n)
c = consumer('')
produce(c)