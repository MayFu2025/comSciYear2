def find_num_of_parity_bits(len_msg: int) -> int:
    k = 0
    while (2 ** k) < (len_msg + k + 1):
        k += 1
    return k

def find_parity_indices(k: int) -> list[int]:
    positions = []
    for n in range(k):
        positions.append((2 ** n) - 1)
    return positions

# Check to see it works:
print(find_parity_indices(3))
print(find_parity_indices(4))
print(find_parity_indices(5))

# HL part:
def create_list(n: int)->list[int]:
    k = find_num_of_parity_bits(n)
    indices = find_parity_indices(k)
    output = []
    for a in range(n+k):
        if a in indices:
            output.append(1)
        else:
            output.append(0)
    return output
