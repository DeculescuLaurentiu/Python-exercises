#Super simple loop wich prints from 1 to 10
num = 1

while num <= 10:
    print(num)
    num += 1
    
    loop_condition = True
 
 #Loop wich i forgot what it does
while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False
    
    for i in range(1, 11):
        print(i)
        
#Loop wich prints the smallest number
        smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)