def calculate():
    string=input('Enter the numbers:')
    numbers=string.split(' ')
    string='+'.join(numbers)
    result=eval(string)
    print(result)
    
calculate()