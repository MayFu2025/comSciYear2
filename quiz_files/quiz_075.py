# Quiz 075
from matplotlib import pyplot as plt

def find_num_of_parity_bits(len_msg:int) -> int:
    k = 0
    while 2**k <= len_msg+k+1:
        k+=1
    return k


# x = []
# y = []
# for n in range(0, 1001):
#     x.append(n)  # Where n represents the length of message
#     y.append((n/(n+(find_num_of_parity_bits(n)))))
#
# plt.plot(x, y, color="gray")
# plt.xlabel("Length of Message", fontsize=15)
# plt.ylabel("Efficiency", fontsize=15)
# plt.show()


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


# Quiz 078
def create_message(msg: str) -> str:
    output = []
    k = find_num_of_parity_bits(len(msg))
    pos = find_parity_indices(k)

    msg_index = 0
    for n in range(0, len(msg) + k):
        if n in pos:  #Where a parity should be
            output.append(-1)
        else:
            output.append(msg[msg_index])  # Actual value of the message
            msg_index += 1

    print(output)

    parity_values = []
    for p in range(k): # P0 ~ Pk
        num_ones = 0
        for index in range(len(output)):
            if (2**k) & index:
                if output[index-1] == 1:
                    num_ones += 1
        if num_ones % 2 == 0:
            parity_values.append('0')
        else:
            parity_values.append('1')
    print(parity_values)  # Wrong parity values

    parity_index = 0
    for n in range(len(output)):  #But otherwise kinda correct
        if output[n] == -1:
            output[n] = parity_values[parity_index]
            parity_index += 1

    return output

print(create_message(msg='1011'))






# def create_message(msg: str) -> str:
#     output = ""
#     k = find_num_of_parity_bits(len(msg))
#     pos = find_parity_indices(k)
#     msg_index = 0
#
#     for n in range(0, len(msg)+k):
#         if n in pos:
#             output +=
#         else:
#             output += msg[msg_index]
#             msg_index += 1
#     return output


# Test that it works
# print(create_message("1011"))