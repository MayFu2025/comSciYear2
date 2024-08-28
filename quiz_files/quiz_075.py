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