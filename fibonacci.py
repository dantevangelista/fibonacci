# Solves power summation of the Fibonacci sequence
# F(n) = 1, 1, 2, 3, 5, ...

# Let F_1 = F_2 = 1
# let N, n in *N*, m in *R*
# F = sum^N_{n = 1} f^m_n
# where by Binet's formula, 
# f_n = 1/sqrt{5} (((1 + sqrt{5})/2)^n - (1 - sqrt{5})/2)^n)


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