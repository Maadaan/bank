bank_name = []
bank_password = []
bank_account = []
bank_balance = []


def create_new_account(name, password, account, balance):
    global bank_name, bank_password, bank_account, bank_balance

    bank_name.append(name)
    bank_password.append(password)
    bank_account.append(account)
    bank_balance.append(balance)


def show_account():
    global bank_account, bank_password, bank_account, bank_balance
    print('Getting Account .......')
    user_password=input('Enter the password to continue ....')
    
    if user_password==bank_password:
        # print('Bank Name ', bank_name)
        # print('Bank Account ', bank_account)
        # print('Bank Name ', bank_name)
        # print('Bank Name ', bank_name)
        print('''
                Bank Details of a user
                Bank Name : {}
                Bank Account : {}
                Bank Balance : {}
            '''.format(bank_name,bank_account,bank_balance))
    else:
        print('Please!!! Enter the correct password ????')


# def get_account_balance(password):
#     global bank_account, bank_password, bank_account, bank_balance

#     if password!=bank_password:
#         pass

