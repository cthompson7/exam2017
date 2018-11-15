trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    listOfNumbers = []
    stringNumber = str(number)

    if 10 >= number >= 0:
        return trans[str(number)]

    if  19 >= number >= 11:
        return trans['10'] + " " + trans[str(number-10)]

    if 99 >= number >= 20:
        for i in stringNumber:
            listOfNumbers.append(i)
        if listOfNumbers[1] == '0':
            return trans[listOfNumbers[0]] + ' ' + trans['10']
        return trans[listOfNumbers[0]] + ' ' + trans['10'] + ' ' + trans[listOfNumbers[1]]

    if number == 100:
        return trans['1'] + " " + trans['100']

    if 999 >= number >= 101:
        for i in stringNumber:
                listOfNumbers.append(i)
        if listOfNumbers[1] == '0' and listOfNumbers[2] == '0':
            return trans[listOfNumbers[0]] + ' ' + trans['100']
        if listOfNumbers[1] == '0':
            return trans[listOfNumbers[0]] + ' ' + trans['100'] + ' ' + trans['0'] + ' ' + trans[listOfNumbers[2]]
        if listOfNumbers[2] == '0':
            return trans[listOfNumbers[0]] + ' ' + trans['100'] + ' ' + trans[listOfNumbers[1]] + ' ' + trans['10']
        return trans[listOfNumbers[0]] + ' ' + trans['100'] + ' ' + trans[listOfNumbers[1]] + ' ' + trans['10'] + ' ' + trans[listOfNumbers[2]]

# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
