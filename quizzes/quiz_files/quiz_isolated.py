from quiz_075 import find_parity_indices, find_num_of_parity_bits, get_indices_checked

def find_parity_indices(k: int) -> list[int]:
    positions = []
    for n in range(k):
        positions.append((2 ** n) - 1)
    return positions

# Check to see it works:
print(find_parity_indices(3))
print(find_parity_indices(4))
print(find_parity_indices(5))