# Quiz 075
from matplotlib import pyplot as plt


def find_num_of_parity_bits(len_msg: int) -> int:
    k = 0
    while (2 ** k) < (len_msg + k + 1):
        k += 1
    return k


# x = []
# y = []
# for n in range(0, 1001):
#     x.append(n)  # Where n represents the length of message
#     y.append(n/(n+(find_num_of_parity_bits(n))))
#
# plt.plot(x, y, color="gray")
# plt.xlabel("Length of Message", fontsize=15)
# plt.ylabel("Efficiency", fontsize=15)
# plt.show()


# Quiz 076
def find_parity_indices(k: int) -> list[int]:
    positions = []
    for n in range(k):
        positions.append((2 ** n) - 1)
    return positions

# print(find_parity_indices(3))
# print(find_parity_indices(4))
# print(find_parity_indices(5))


# Quiz 077
def get_indices_checked(p: int, msg_len: int) -> list[int]:
    """Gets the 0-indexed indices of the bits checked by the p-th parity bit.
    p: int, the p-th parity bit
    msg_len: the length of the total message including parity bits
    """

    indices = []
    for a in range(msg_len+1):
        if a & (2 ** (p - 1)):
            indices.append(a - 1)
    return indices


# Quiz 078
def create_message(msg: str) -> str:
    output = []
    k = find_num_of_parity_bits(len(msg))
    pos = find_parity_indices(k)
    # print(k, pos)

    msg_index = 0
    for n in range(len(msg) + k):
        if n in pos:  # Where a parity should be
            output.append(-1)
        else:
            output.append(msg[msg_index])  # Actual value of the message
            msg_index += 1
    # print(output)

    # Quiz 079
    check = []
    for n in range(1, k + 1):
        check.append(get_indices_checked(p=n, n=len(msg), k=k))
    # print(check)
    p_index = 0
    for n in range(len(output)):
        if n in pos:
            num_1s = 0
            for a in check[p_index][1:]:
                # print(a)
                if output[a] == "1":
                    num_1s += 1
            if num_1s % 2 == 1:
                output[n] = "1"
            else:
                output[n] = "0"
            p_index += 1
    # print(output)

    return ''.join(output)


# Test that it works:
# print(create_message(msg='1011'))

