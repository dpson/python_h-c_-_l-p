My_color_list=('Blue','Red','Black','Pink','Brown','Yellow')
print("My color list")
print(My_color_list)
print(str.format("color_list at index 3: {0}",My_color_list[3]))
i=int(input("Enter a number from 0-5: "))
while i<6:
    print(str.format("Your color: {0}",My_color_list[i]))
    break
###1.4
print(My_color_list[0])
print(My_color_list[1])
print(My_color_list[2])
print(My_color_list[3])
print(My_color_list[4])
print(My_color_list[5])
###1.5
m=input("What is your favorite color? ")
for h in My_color_list:
    n=My_color_list.index(h)
    if m==h:
       print("Your color is at index",My_color_list[n],"in my list")
       break
    elif m!=h:
       print("Sorry,I could not find your color")
       break
2 FLOCK_SHEEP
flock_sheep=[ 10, 20, 30, 40, 50, 60, 70, 80]
########
print("Hello,my name is Son and these are my sheep sizes")
print(flock_sheep)
print("Now my biggest sheep has size",max(flock_sheep),"let's shear it")
n = max(flock_sheep)
m = flock_sheep.index(n)
flock_sheep.remove(n)
flock_sheep.insert(m, 8)
print("After shearing, here is my flock ")
print(flock_sheep)
####### 1 MOTH
i=0
length=len(flock_sheep)
while True:
    if i<length:
        flock_sheep[i]=flock_sheep[i]+50
        i=i+1
        continue
    print("One month has passed,now here is my flock")
    print(flock_sheep)
    break
#### N Month
flock_sheep=[ 10, 20, 30, 40, 50, 60, 70, 80]
print('Heloo, My name is Son, now here is my flock')
print(flock_sheep)
i=1
n=0
length=len(flock_sheep)
while i<6:
    if n<length:
        flock_sheep[n]=flock_sheep[n]+50
        n=n+1
        continue
    print(str.format("MONTH {0}",i))
    print("One month has passed,now here is my flock")
    print(flock_sheep)
    print(str.format("Now my bigget sheep has size {0} let's shear it",max(flock_sheep)))
    a = max(flock_sheep)
    b=flock_sheep.index(a)
    flock_sheep.remove(a)
    flock_sheep.insert(b, 8)
    print("After shearing,here is my flock ")
    print(flock_sheep)
    i=i+1
    n=0
s=0
d=1
while True:
    if n<length:
        s=s+flock_sheep[n]
        n=n+1
        continue
    print("My flock has size in total: ",s)
    d=int(s)*2
    print(str.format("I would get {0} *2$ = {1}%",s,d))
    break
        
    
