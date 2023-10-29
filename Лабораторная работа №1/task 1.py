numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
one_numbers = numbers [0:4] + numbers [5:]
a= sum(one_numbers)
b= len(numbers)
c= a / b
numbers [4]= c
print("Измененный список:", numbers)
