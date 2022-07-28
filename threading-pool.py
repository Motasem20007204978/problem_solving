
def queue_time(customers:list[int], n:int) -> int:
    """
    :param customers: list of customers
    :param n: number of threads
    :return: time to serve all customers
    """
    n = len(customers) if n > len(customers) else n 
    
    time = 0
    poped = customers[0:n]
    customers = customers[n:]
    while poped:
        time += min(poped)
        poped = [x-min(poped) for x in poped]
        print(poped, 'before filter')
        poped = list(filter(lambda x: x > 0, poped))
        print(time, 'times')
        print(poped, 'after filter')
        while len(poped) < n and customers:
            poped.append(customers.pop(0))
            print(poped, 'after pop')
        
    return time

# another solution
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
        

customers = [10,2,3,3]
n = 2
print(queue_time(customers, n))