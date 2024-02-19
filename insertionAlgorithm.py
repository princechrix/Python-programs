numbers = [32,12,65,14,9,5,62,7]

for i in range(len(numbers)):
    selectedNum = numbers[i]
    prevIndex = i - 1 

    while prevIndex >= 0 and selectedNum < numbers[prevIndex]:
        numbers[prevIndex + 1] = numbers[prevIndex]

        prevIndex -= 1

    numbers[prevIndex + 1] = selectedNum

print(numbers)


largestNum = numbers[0]

for num in numbers:
    if num > largestNum:
        largestNum = num

print(f"The Largest Number is {largestNum}")