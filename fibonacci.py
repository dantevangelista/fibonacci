# Solves power summation of the Fibonacci sequence
# F(n) = 1, 1, 2, 3, 5, ...

F1 = 1
F2 = 1
m = 2
n = 48

i = 2
sum = F1**2 + F2**2
while i < n:
    F = F1 + F2
    F1 = F2
    F2 = F
    sum += F**m
    i += 1
print(sum)