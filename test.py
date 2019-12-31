# import collections
#
#
# colours = (
#     ('Yasoob', 'Yellow' ),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# from collections import Counter
#
# end = Counter(name for name , color in colours)
# print(end )
# print()
# from collections import defaultdict
#
# favorite = defaultdict(list)
#
# for name , colour  in colours :
#     favorite[name].append(colour)
# for key , value in favorite.items():
#     print(key ,len(value) , value)

import functools
# from functools import reduce
# list = [ 1 , 3 , 4  , 7 ,54]
#
# newlist = filter(lambda x : x%2 == 0 , list)
# print(tuple(newlist))
#
# #////////////////////////////////////////////////////////////
# newlist = map(lambda x : x**x, list)
# print(tuple(newlist))
#
# #/////////////////////////////////////////////////////////////
# newlist = reduce((lambda x ,y : x+y) , list)
# print(newlist)
#
# #///////////////////////////////
# from collections import Counter
# x = "amirhasan"
# y = "amirsahan"
# print(dict(Counter(x)))
# print(Counter(y))
# print(Counter(x) == Counter(y))
#
# print("".join(reversed(x)))
# print(x[::-1])
#
#
# #/////////////
# arr1 = [1,3,5,7,9]
# arr2 = [1,2,3,4,5,6,7,8,9]
# instersection = filter(lambda x : x in arr1 , arr2 )
#
# print(tuple(instersection))
#
#
# x  = " amirhasan"
# import re
# matchgoogoo = re.match(r'(.*)a(.*)a(.*)(.*)n',x)
#
# if matchgoogoo != None:
#     print(True)
import re
n = int(input())
arr = []
for i in range(0,2*n):
    arr.append(str(input()))


def f (st1 , st2):
    regg = reg(st2)
    match1 = re.match(regg ,st1 )
    match2 = re.match(regg , st1[::-1])
    if match1 != None or match2 !=None:
        print("YES")
    else :
        print("NO")
def reg (st2):
    output = ''
    for x in st2:
        output += '(.*)'+ x

    return output
for i in range(0,2*n,2):
    f(arr[i],arr[i+1])







