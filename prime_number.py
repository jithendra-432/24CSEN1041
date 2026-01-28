num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("Enter a number greater than 1")
##output
  Enter a number: 3
3 is a prime number


  Enter a number: 1
Enter a number greater than 1
