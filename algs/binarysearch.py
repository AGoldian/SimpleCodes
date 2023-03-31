import numpy as np
from math import log2

max_range = 10000000
df = np.array(range(1, max_range), dtype=int)
print(log2(max_range))


char = 12342233

def binary_search(df, char):
    min_index = 0
    max_index = len(df) - 1
    mid = 0
    i = 0

    while min_index <= max_index:
        mid = (min_index + max_index) // 2

        if char > df[mid]:
            min_index = mid + 1
        elif char < df[mid]:
            max_index = mid - 1
        else:
            print(f'Число {char} найдено его индекс - {mid}')
            print(f'Потребовалась {i} итераций')
            break
        
        i += 1
    
    else:
        print('Найдена токо шляпа')

binary_search(df, char)
