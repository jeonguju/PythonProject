#1. 숫자형
a=80
b=75
c=55
d=(a+b+c)/3
print(d)

#2. 숫자형-연산자
a=13
b=a%2
print(b)

#3. 문자열 자료형-슬라이싱
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)



#4. 문자열 자료형-인덱싱
pin = "881120-1068234"
print(pin[7])

pin = "881120-1068234"
print(pin[7])
a = pin[7]
if a == "1":
    print("man")
else:
    print("woman")

#5. 문자열 함수_replace
a = "a:b:c:d"
b = a.replace(":" , "#")
print(b)

#6. 리스트 내장 함수
a = [1, 3, 5, 4, 2]
a.sort() #p80 리스트 정렬
print(a)
a.reverse() #p81 리스트 뒤집기
print(a)

#7. 문자열 삽입 join 함수
a = ['Life' , 'is' , 'too', 'short']
result = ' '.join(a) #p68
print(result)

a = "Life is too short"
print(a.split())

#8. 튜플 자료형
a = (1, 2, 3)
a = a + (4, )
print(a)

#9.
#10.
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12.
a = b = [1, 2, 3]
a[1] = 4
print(b)