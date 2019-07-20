print('******** Challenge-2 ********')

resultList=[]

enterName=input('Enter the Name-')
while(len(enterName)==0):
    enterName=input('Name can not be Empty, Enter Name-')
resultList.append(enterName)

emailVar=0
emailloop=1
emailId=input('Enter the Email ID -')
while(emailloop==1):
    if(len(emailId)==0):
        while(len(emailId)==0):
            emailId=input('Email-Id cannot be Empty,Enter Email ID-')
            if(len(emailId)!=0):
                emailVar=1
            if(emailVar==1):
                while(('@' in emailId)==0):
                    emailId=input('Email-Id is incorrect(@ Missing), Enter again-')
                indexOfAtTheRate=emailId.index('@')
                while(indexOfAtTheRate==0):
                    emailId=input('Email-Id is incorrect(Prefix before @ Missing), Enter again-')
                    indexOfAtTheRate=emailId.index('@')
                serDomain=emailId[indexOfAtTheRate:]
                while(('.' in serDomain)==0):
                    emailId=input('Email-Id is incorrect(Dot(.) Missing in Domain), Enter again-')
                    indexOfAtTheRate=emailId.index('@')
                    serDomain=emailId[indexOfAtTheRate:]
                emailloop=0
    else:
        while(('@' in emailId)==0):
            emailId=input('Email-Id is incorrect(@ Missing), Enter again-')
        indexOfAtTheRate=emailId.index('@')
        while(indexOfAtTheRate==0):
            emailId=input('Email-Id is incorrect(Prefix before @ Missing), Enter again-')
            indexOfAtTheRate=emailId.index('@')
        serDomain=emailId[indexOfAtTheRate:]
        while(('.' in serDomain)==0):
            emailId=input('Email-Id is incorrect(Dot(.) Missing in Domain), Enter again-')
            indexOfAtTheRate=emailId.index('@')
            serDomain=emailId[indexOfAtTheRate:]
        emailloop=0
resultList.append(emailId)

phoneNumber=input('Enter the Phone Number-')
phoneVar=1
while(phoneVar==1):
    if(len(phoneNumber)==0):
        while(len(phoneNumber)==0):
            phoneNumber=input('Phone Number Cannot Be Empty, Enter Valid Number-')    
        startDigit=int(phoneNumber[0])
        while(startDigit in range(0,6,1)):
            phoneNumber=input('Incorrect Phone Number(Should not start from 0-5),Enter Valid Number-')
            startDigit=int(phoneNumber[0])
        while(len(phoneNumber)!=10):
            phoneNumber=input('Incorrect Phone Number(No 10 Digits),Enter Valid Number-')

        phoneVar=0
    else:
        startDigit=int(phoneNumber[0])
        while(startDigit in range(0,6,1)):
            phoneNumber=input('Incorrect Phone Number(Should not start from 0-5),Enter Valid Number-')
            startDigit=int(phoneNumber[0])
        while(len(phoneNumber)!=10):
            phoneNumber=input('Incorrect Phone Number(No 10 Digits),Enter Valid Number-')
        phoneVar=0
phoneNumber=int(phoneNumber)
resultList.append(phoneNumber)

course=input('Enter the Course-')
while(len(course)==0):
    course=input('Course cannot be Empty, Enter again-')
resultList.append(course)

print('Data stored in ResultList As-',resultList)
            
