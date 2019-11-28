import collections


colours = (
    ('Yasoob', 'Yellow' ),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

from collections import Counter

end = Counter(name for name , color in colours)
print(end )
print()
from collections import defaultdict

favorite = defaultdict(list)

for name , colour  in colours :
    favorite[name].append(colour)
for key , value in favorite.items():
    print(key ,len(value) , value)
