# import collections


# n = int(input())
# L = collections.deque()
# cursor = 0
# for i in range(n):
#     l =list(map(int,input().split()))
#     if l[0] == 0:
#         L.insert(cursor, l[1])
#     if l[0] == 1:
#         cursor += l[1]
#     if l[0] == 2:
#         del L[cursor]
# for j in L:
#     print(j)


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data
    
       