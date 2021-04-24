# def 객체이름불러오기(xx):
#     return [objname for objname, oid in globals().items() if id(oid) == id(xx)][0]


# #class는 객체(object)를 만드는 틀을 의미한다.
# class 쿠키틀:
#     def 쿠키굽기(self):
#         a=객체이름불러오기
#         print(f'{객체이름불러오기(self)}가 구워졌어요')
#     pass

# 초코칩쿠키=쿠키틀()
# 화이트초코쿠키=쿠키틀()
# 아몬드쿠키=쿠키틀()

# 초코칩쿠키.쿠키굽기()
# 화이트초코쿠키.쿠키굽기()
# 아몬드쿠키.쿠키굽기()


# """리스트 연습"""
# alist=list(['1번', '2번',3,3.14])
# blist=['가나다라마바사아자차카타파함', 'ㄴㅇㄻㄴㅇㄹㄴㅁㄹ', 'ㄴㅁㄹㄴㅇㄻㅁㅇㄴ', 11232312323123213291380]

# print(len(alist))
# print(type(blist))
# print(blist)





empty_list = list()
print(len(empty_list))

fruits = ['banana' 'orange','mango', 'lemon']
vegetables = ['tomato', 'potato','cabbage','onion', 'carrot']
animal_products = ['milk','meat','butter','yoghurt']
web_techs = ['HTML','CSS', 'JS', 'React', 'Redux', 'Node','MongDB']
countries = ['Finrand','Estonia', 'Denmark', 'Sweden','Norway']

print('과일:', fruits)
print('과일 개수:', len(fruits))
print('야채:', vegetables)
print('야채 개수:',len(vegetables))
print('동물 식품:', animal_products)
print('동물 식품의 개수:', len(animal_products))
print('인터넷 기술:', web_techs)
print('인터넷 기술 개수:', len(web_techs))
print('국가:', countries)
print('국가 개수:', len(countries))

an=input('과일, 야채, 동물 식품, 인터넷 기술, 국가 중 하나를 입력하세요.')

for i in fruits:
    if an == i:
        ab= '과일'
for i in vegetables:
    if an == i:
        ab= '야채'
for i in animal_products:
    if an == i:
        ab= '동물제품'
for i in web_techs:
    if an == i:
        ab= '웹기술'
for i in countries:
    if an == i:
        ab= '나라'

print(an, '는', ab, '입니다.')




