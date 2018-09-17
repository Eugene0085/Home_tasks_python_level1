# # -*-  coding: Utf-8 -*-
# import math

# Задача №4 Normal
#
# list_choord = []
# for i in range(1, 5):
#     print(" Координаты A", i)
#     x = int(input("введите  x:"))
#     y = int(input("введите y:"))
#
#     list_choord.append((x, y))
# list_segment = []
# for i in range(0,len(list_choord)-1):
#     for j in range(i+1,len(list_choord)):
#         if list_choord[i] != list_choord[j]:
#             x1, y1 = list_choord[i]
#             x2, y2 = list_choord[j]
#             q = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#             line_segment = (list_choord[i], list_choord[j], q)
#             # print (th)
#             list_segment.append(line_segment)
# count = 0
# for t in list_segment:
#     for tmp_t in list_segment:
#         A1, A2, q1 = t
#         B1, B2, q2 = tmp_t
#         if tmp_t != t and A1 != B1 and A1 != B2 and A2 != B1 and A2 != B2 and q1 == q2:
#             count += 1
# #             print(t,tmp_t)
# # print(count)
# if count >= 2:
#     print("параллелограмм")
# else:
#     print(" не параллелограмм")


def fibonaci(n):
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b
        print()

fibonaci(1000)



