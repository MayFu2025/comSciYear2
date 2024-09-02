# Quiz 075
from matplotlib import pyplot as plt

def find_num_of_parity_bits(len_msg:int) -> int:
    k = 0
    while 2**k <= len_msg+k+1:
        k+=1
    return k


x = []
y = []
for n in range(0, 1001):
    x.append(n)  # Where n represents the length of message
    y.append((n/(n+(find_num_of_parity_bits(n)))))

plt.plot(x, y, color="gray")
plt.xlabel("Length of Message", fontsize=15)
plt.ylabel("Efficiency", fontsize=15)
plt.show()


# Quiz 076
def find_parity_indices(k: int) -> list[int]:
    positions = []
    for n in range(k):
        positions.append((2**n)-1)
    return positions


# Quiz 077
def get_indices_checked(p: int, n: int, k: int) -> list[int]:
    """Gets the indices of the bits checked by the p-th parity bit.
    p: int, the p-th parity bit
    n: int, the length of the message intending to be sent
    k: int, the number of parity bits
    """

    indices = []
    for a in range(n+k+1):
        if a & (2**(p-1)):
            indices.append(a-1)
    return indices
