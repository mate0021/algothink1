a, b = 0, 1
while b < 20:
    # print b
    a, b = b, a + b

stack = [2, 3, 4]
stack.append(5)
print stack.pop()
print stack

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f1(x): return x*x
def f2(n): return 2 ** n

print "kwadrat: " + str(map(f1, input))
print "2 ^ n:   " + str(map(f2, input))

def sum(x, y): return x + y
print reduce(sum, input)

print [(x, y) for x in range(1, 40) for y in range(1, 40) if y == 2*x]