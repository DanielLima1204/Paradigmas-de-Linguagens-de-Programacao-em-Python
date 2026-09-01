# a = 0
# for i in range(30):
#     print(i)
#     if a % 2 == 0:
#         a += 1
#         continue
#     elif a % 5 == 0:
#         break
#     else:
#         a += 3

def foo(n):
    if n > 1:
        return n * foo(n - 1)
    return n
print(foo(4))