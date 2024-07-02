chaewon = ["임채원", '33', '010-2210-****']
name = chaewon[0]
age = chaewon[1]
phone = chaewon[2]

print(type(chaewon))
print(name , age, phone)

names = [['강수경', '강혜나' , '김민석'],['21','22','23'],['010-****-****','010-****-****','010-****-****']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(numbers))

#리스트에 요소 추가하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)