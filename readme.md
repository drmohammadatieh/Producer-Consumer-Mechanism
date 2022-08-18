## The Producer-Consumer Mechanism

This is an exercise on producer-consumer mechanism as part of the Secure Software Development course of the CS PgCert at the University of Essex Online. 

## Instructions

Run producer-consumer.py, where the queue data structure is used. Now answer the following questions:

1- How is the queue data structure used to achieve the purpose of the code?
2- What is the purpose of q.put(I)?
3- What is achieved by q.get()?
4- What functionality is provided by q.join()?
5- Extend this producer-consumer code to make the producer-consumer scenario available in a secure way. What technique(s) would be appropriate to apply?

## Answers

### Q1

The queue data structure works by the first in first our principle (FIFO). This allows the items in the queue to be retrieved in the order they were placed.

### Q2

```q.put(i)``` is used to place a value in the queue.

### Q3

```q.get(i)``` is used to retrieve the first item placed in the queue. The next time ```q.get(i)``` is used, the next after the first in the queue is retrieved based on the FIFO principle, etc.

### Q4 

```q.join()``` waits until all the items in the queue are processed before proceeding to the next line of code.

### Q5

This code can be extended by adding the ```thread_lock.aquire()``` to lock the thread until it finishes all the tasks, then ```thread_lock.release()```. The code is commented where the first and second addition are added.