output = []
x = int(input("Insert number: "))
for i in range(2,x//2):
    if x%i == 0:
        if i == 2:
            pass
        elif i == 4:
            output.append(2)
            output.append(2)
        else:
            while i%2 == 0:
                i = i/2
        output.append(i)
        x = x/i
if x != 1:
    output.append(int(x))

if 1.0 in output:
    output.remove(1.0)
print(output)
