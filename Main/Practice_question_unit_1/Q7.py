from functools import reduce

nums = [2, 3, 4, 5]

tot = reduce(lambda a,b: a + b, list(map(lambda x: x*x,nums)), 0)

print(tot)