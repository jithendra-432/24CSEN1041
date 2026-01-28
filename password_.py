password = "python123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access Granted")
        break
    else:
        attempts = attempts -1
        print("Wrong password. Attempts left:", attempts)
  ##ouput
    Enter password: python123
Access Granted
Enter password: python123
Access Granted



   
Enter password: hgiljh
Wrong password. Attempts left: 2
Enter password: ghsh
Wrong password. Attempts left: 1
Enter password: gggdafg
Wrong password. Attempts left: 0

=== Code Execut
