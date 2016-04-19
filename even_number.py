def even_number(list):
   n = input('Input a list of number: ')
   x=0
   list = [int(x) for x in n.split()]
   print("even number: ",end='')
   for x in list:
       if (x%2 == 0):
        print(x ,end=' ' )
a=even_number(list)


