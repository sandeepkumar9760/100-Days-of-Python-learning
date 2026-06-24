name = input("Enter your name: ")
print(name)

first_num = input("Enter your first num: ")
second_num = input("Enter your second number: ")
print(first_num + second_num)

print("You will see numbers are not added mathematically , because python by default takes it as string so we need to specify the data type of the input we want from the user.")

first_num = int(input("Enter the number 1: "))
second_num = int(input("Enter the number 2: "))

print(first_num+second_num)

print("Now the numbers are added , because now we have specified the data types of the input , and if user gives string as a input it will throw an error.")


#type conversion

#implicit type conversion

print(4+5.6+6j)
print("It automatically converts data types to add")

#explicit type conversion

print(int(4.5))
print("It will convert float into integer")
#like this we can use different functions to convery data types.



