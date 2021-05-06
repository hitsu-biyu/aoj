import math


while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(float, input().split()))
    m = sum(scores) / n
    total = 0 
    for i in range(n):
        total += (scores[i] - m)**2
    variance = total / n
    print(math.sqrt(variance))
