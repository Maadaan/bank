account_name = input('Enter the name of account holder : ')
account_password = input('Enter the password of account holder : ')
account_balance = int(input('Enter the balance of account holder : '))

while True:
    print("""
            Press 'b' to get the balance
            Press 'd' to deposit the balance
            Press 'w' to withdraws the deposit
            Press 's' to showing details of the account
            Press 'q' to quit
        """)

    question = input("Press any character which is given above !!! 'b' or 'd' or 'w' or 's' or 'q' : ")
    question = question.lower()

    # -------------------------
    # getting the balance
    # -------------------------
    if question == 'b':

        print('Getting balance .....')
        user_password = input('Please enter the password ????  :  ')

        if user_password != account_password:
            print('Incorrect password !!! Please enter correct password to continue .....')

        else:
            print('Your balance is : {} '.format(account_balance))


    # -------------------------
    # deposit the balance
    # -------------------------
    elif question == 'd':
        print('Balance is depositing !!!!!!')

        deposit_amount = int(input('Enter the deposit amount ??? : '))
        user_password = input('Enter correct password to deposit the balance : ')

        if deposit_amount < 0:
            print('Enter the positive value number ')

        elif account_password != user_password:
            print('Please !!! Enter the correct password to continue !!!   ')

        else:
            print('Previously your balance was {}'.format(account_balance))
            account_balance += deposit_amount
            print('Now your balance is {}:'.format(account_balance))

    # -------------------------
    # withdrawing the balance
    # -------------------------

    elif question == 'w':
        print('Withdrawing balance !!!!')
        user_password = input('Enter the user  password !!! : ')

        if user_password == account_password:
            withdrawing_balance = int(input('Enter the amount you want to withdraw : '))
            print('Withdrawing balance loading !!!!')

            if account_balance < withdrawing_balance:
                print('Insufficient balance !!!')

            elif withdrawing_balance < 0:
                print('Please enter the positive values !!!')

            else:
                print('Your balance was {} '.format(account_balance))
                account_balance -= withdrawing_balance
                print('Now your balance is {} '.format(account_balance))

        else:
            print('Enter a correct password to continue !!!')

    # -------------------------
    # showing details of the balance
    # -------------------------
    elif question == 's':
        user_password = input('Enter a user password : ')

        if user_password == account_password:
            print('Loading user Informations !!!!!')

            print("""
                User Informations ......
                    Account Name : {}
                    Account Balance : {}
                Thank You !!!
            """.format(account_name, account_balance))
        else:
            print('Enter a correct password !!!')
    else:
        print('Choose any of the above questions : ')
        break
