
def first_recurrent_symbol(arr):
    unique_symbols = []
    for i in arr:
        if i in unique_symbols:
            return i
        unique_symbols.append(i)
    return None

def first_recurrent_symbol1(arr):
    unique_values = set()
    for i in arr:
        if i in unique_values:
            return i
        else:
            unique_values.add(i)
    return None
   
print(first_recurrent_symbol([2, 1, 5, 2, 1, 3, 8]))
print(first_recurrent_symbol1([2, 1, 5, 2, 1, 3, 8]))


