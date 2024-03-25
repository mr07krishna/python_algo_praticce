# queue = []
# queue.append(5)
# queue.append(80)
# queue.append(9)
# queue.append(3)
# queue.append(7)
# queue.append(1)
# queue.append(6)
# print(queue)
# queue.pop()
# print(queue)
# print(queue.pop())
# print(queue)


def isEmpty(queue):
    if not queue:
        return True
    else:
        return False

def enqueue(queue, n):
    queue.append(n)
    return queue
def dequeue(queue):
    if isEmpty(queue):
        print("queue empty")
        return False
    else:
        return (queue.pop())

queue = []
queue.append(5)
queue.append(80)
queue.append(9)
queue.append(3)
queue.append(7)
queue.append(1)
queue.append(6)
print(queue)
queue.pop()
print(queue)
print(queue.pop())
print(queue)

'''
def isEmpty(queue):
    return not queue

def enqueue(queue, n):
    queue.append(n)
    return queue

def dequeue(queue):
    if isEmpty(queue):
        print("queue empty")
        return None
    else:
        return queue.pop(0)

queue = []
queue.append(5)
queue.append(80)
queue.append(9)
queue.append(3)
queue.append(7)
queue.append(1)
queue.append(6)

print(queue)
queue.pop()
print(queue)
print(dequeue(queue))
print(queue)
'''
