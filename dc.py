dic = {'임채원' : 33, '김민석': 28}
print(dic['김민석'])

# 딕셔너리 데이터 업데이트
dic['임채원'] = 34
print(dic['임채원'])

dic_2 = {'임채원': [33 , 175 , 86, '010-2210-****'], '최아진':[20, ]}
print(dic_2['임채원'][1])

dic_3 = {'임채원': {'나이': 33, '키':175, '몸무게':86, '연락처': '010-2210-****'}}

print(dic_3['임채원']['나이'])