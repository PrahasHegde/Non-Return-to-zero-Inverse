import matplotlib.pyplot as plt

output_data = []

def encode(data):
    current_level = 1

    if bits[0] == 0:
        output_data.append(1)
    else:
        output_data.append(-1)

    for i in range(len(bits)):
        if bits[i] == 0:
            output_data.append(current_level)
        elif bits[i] == 1:
            current_level=current_level*(-1)
            output_data.append(current_level)

        else:
            print("invalid input")
    
    return output_data


strbit = input("enter your bit: ")
bits=[int(bit)for bit in strbit]

x = encode(bits)
print(output_data)
y = [i for i in  range(len(output_data))]

plt.step(y,x)


plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('NRZ-L wave') 
plt.show()
