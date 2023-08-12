def switch():
    My_list=[1,2,3,4,5]
print("press 1 for append\n press 2 for remove\n press 3 for insert\n press 4 for display the element\n press 5 for stop the code")
option=int(input("Enter your option:"))
if option == 1:
    My_list=[1,2,3,4,5]
    result=My_list.append(6)
    print(My_list)
option=int(input("Enter your option:"))
if option == 2:
    My_list=[1,2,3,4,5]
    result=My_list.remove(4)
    print(My_list) # Output: [1, 2, 3, 5]
option=int(input("Enter your option:"))
if option == 3:
    My_list=[1,2,3,4,5]
    result=My_list.insert(6, 7)
    print(My_list) # Output: [1, 2, 3, 4, 5, 6, 7]
option=int(input("Enter your option:"))
if option == 4:
    My_list=[1,2,3,4,5]
    for element in My_list:
        print(My_list) # Output: [1, 2, 3, 4, 5]
        elif option == 5:
            break
switch()