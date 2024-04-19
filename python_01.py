
# 2-masala

def accum(a):
    k=len(a)
    d=""
    for i in range(k):
        d+="-" + a[i].upper()+ a[i]*(i)
    return d[1:]
print(accum('Asadbek')) # A-Ss-Aaa-Dddd-Bbbbb-Eeeeee-Kkkkkkk


# 3-misol
pass

# 4-misol
a=int(input("Raqam kiritilsin \t:"))
j=2*(a-1)
print(j)
# 5-misol

def opposite(number):
    return -number

print(opposite(-25.5022))

# 6-misol
# 1-soad 60 minut -> 3 600 000 millisekund
# 1-minut 60 sikund-> 60000millisekund
# 1-sekund 1000 millisekund
def past(h, m, s):
    if 0<=h<=23 and 0<=m<=56 and 0<=s<=59:
        ms=h*36000000+m*60000+s*1000
    return ms
print(past(1,2,3))# 36123000
print(past(0,1,2))# 62000


# 7-misol

def make_negative(number):
    
    if number>0:
        return -number
    elif number<0:
        return number
    else:
        return  None #yoke False
    
print(make_negative(5)) # -5
print(make_negative(0)) # None
print(make_negative(-26)) # -26

# 8-misol
pass

# 9-misol

def ather_angle(a,b):
    if a>0 and b>0 and (a+b)<180:
        c=180-(a+b)
        return c
    else:
        return None

print(ather_angle(20, 120)) # 40
print(ather_angle(120, 120)) # None

# 10-misol

def square(n):
    return n**2

print(square(2))
print(square(3))
print(square(10))

# 11-misol

def century(year):
    return str(year//100+1)+" Asr"
print(century(2050))# 21
print(century(50)) # 1
print(century(350)) #4

# 12-misol

def simple_multiplication(number) :
    if number%2==0:
        s=number*8
    else:
        s=number*9
    return s

print(simple_multiplication(2))
print(simple_multiplication(5))

