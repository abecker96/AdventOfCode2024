

with open("input.txt") as file:
    arr1 = []
    arr2 = []

    for line in file:
        out = line.split()
        
        arr1.append(int(out[0]))
        arr2.append(int(out[1]))

    arr1.sort()
    arr2.sort()

    total_value = 0

    for i in range(len(arr1)):
        difference = arr1[i] - arr2[i]

        if(difference < 0):
            difference *= -1

        total_value += difference

    print(total_value)

# Answer 1660292 was correct