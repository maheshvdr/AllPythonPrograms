def matchingDigits(arg):
    result = 0
    isOneOrZero = 0
    result = result + 1
    temp = '0' * len(arg) 
    for i in range(len(arg)):   
        if((arg[i]=='1') and (isOneOrZero == 0)):
            isOneOrZero = 1
            temp = temp[:i]  +  ('1' * (len(arg)-i))
            print(temp, '1')
            result = result + 1
            if(temp==arg):
                return result-1
        else:
            if((arg[i]=='0') and (isOneOrZero==1)):
                isOneOrZero = 0
                temp = temp[:i] + ('0' * (len(arg)-i))
                print(temp,'0')
                result = result + 1
                if(temp==arg):
                    return result-1
                        


###### if input '0011' result 1
###### if input '0101' result 3
###### if input '1010' result 4
str1 = '0111'
print(matchingDigits(str1))
