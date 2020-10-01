import math
total=int(input('Enter total number of outcomes:'))
choose=int(input('\nEnter number of items to choose:'))
result=math.comb(total,choose)
print('\nTotal combinations:'+str(result))