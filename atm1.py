print('*************** Challenge-4 *****************')
print('----------------------------------------------------')
userName=['manish','qamar','rahul','himanshu','robin']
passWord=[123,112,223,543,999]
bankBalance=[10000,20000,25000,12000,3000]
blockVar=1
while(blockVar==1):
    enterUser=input('Enter the Username-')
    if(enterUser in userName):
        userIndex=userName.index(enterUser)
        trail=1
        remainTrail=3
        enterPassword=(input('Enter the password(length must be 3)-'))
        while((len(enterPassword)!=3) and (trail<3)):
            remainTrail=remainTrail-1
            trail=trail+1
            print('*** Remaining Trail *** ->',remainTrail)
            enterPassword=input('Lenth of password is not equal to 3,enter again-')
        if(trail==3):
            print('you have entered password 3 times wrong, Blocked')
            blockVar=0
        elif((int(enterPassword))==int(passWord[userIndex])):
            print('**** Welcome to Techeinest ATM ****')
            print('-------Mr.',enterUser )
            print('1.Withdrwal \n2.Balance \n3.Change Pin \n4.Deposit')
            userChoice=int(input('Choose the Option-'))
            if(userChoice==1):
                userAmount=int(input('Enter the amount-'))
                if(userAmount>bankBalance[userIndex]):
                    print('Insufficient Balance')
                else:
                    print('Processing...')
                    bankBalance[userIndex]=bankBalance[userIndex]-userAmount
                    print('Transaction Successfull')
                    viewBalance=int(input('To display balance, press 1 else other numeric key-'))
                    if(viewBalance==1):
                        print('Balance-',bankBalance[userIndex])
                        print('Thankyou')
                    else:
                        print('Thankyou')
                    
            elif(userChoice==2):
                print('Balance-',bankBalance[userIndex])
                print('Thankyou')
                print(bankBalance)
            elif(userChoice==3):
                newPin=input('Enter the new pin(3 Digits Only)-')
                if(len(newPin)!=3):
                    print('Length of password should be 3')
                else:
                    passWord[userIndex]=int(newPin)
                    print('Password Changed....')
                    print(passWord)
            elif(userChoice==4):
                depositAmount=int(input('Enter the amount to be Deposit-'))
                bankBalance[userIndex]=bankBalance[userIndex]+int(depositAmount)
                print('Amount Deposited')
                print('Balance-',bankBalance[userIndex])
                print(bankBalance)
            else:
                userChoice=int(input('Wrong Opption Selected, Choose Correct one'))
            print('----------------------------------------------------')
        else:
            print('Password doesnot Match')
            print('----------------------------------------------------')
    
    else:
        print('No user exist of name-',enterUser)
        print('Please try again')
        print('----------------------------------------------------')
