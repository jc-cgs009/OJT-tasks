# import itertools

# combinations = itertools.permutations('abc')

# for c in combinations:
#     print(c)

# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n-r, -1))
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i+1:] + indices[i:i+1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return
# count = 0     
# for c in permutations('abcde'):
#     count += 1
#     print(c)
# print(count)

# print(list(filter(lambda a : a%2 != 0, [1,2,3,4,5,6,7,8,9])))
 
# class CustomForLoop:
#     def __init__(self, items):
#         self.items = items
#         self.index = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         item = self.items[self.index] * 2
#         self.index += 1
#         return item

# numbers = [1, 2, 3, 4, 5]
# for item in CustomForLoop(numbers):
#     print(item)


# n = '912319'

# res = '0'

# for i in range(len(n)):
#     val = n[:i]+n[i+1:]
#     if val > res:
#         res = val

# print(res)



