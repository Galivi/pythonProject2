# # Dictionary(사전)란?
# d1 = {'name': '한 남자', 'age': 22, 'gender': True}
# print(d1, type(d1))
#
# # 키 반복
# for key in d1.keys():
#     print(key, ':', d1[key])
#
# # 값 반복
# for value in d1.values():
#     print(value)
#
# # 추가
# d1['hobby'] = ['술', '춤', '잠']
# d1['weight'] = 78.65
# print(d1)
#
# # 동시에 여러 요소 추가
# d1.update({'weight':67.8,'height': 189.7})
# print(d1)
#
# # 수정
# d1['hobby'] = ['술','춤', '잠', '게임', '등산']
# print(d1)
#
# # 요소 삭제
# del d1['weight']
# print(d1)
#
# # (key, value)쌍 얻기
# print(d1.items())
# for data in d1.items():
#     # print(data, type(data))
#     print(data[0], ':', data[1])






# tuple1 = 1, 2, 3, 4
# print(tuple1, type(tuple1))
#
# #요소 값 변경
# tuple1[0] = 'A'
# #요소 값 삭제
# del tuple1[0]

