# Problem: Count the number of odd numbers from 1 to 2018 that are not divisible by 5 and 2

x = 0
y = 0
while (x*7 < 986 and y*4 <= 876 and x-y > -67):
    x += 2
    y += 3
    
print(x, y)
