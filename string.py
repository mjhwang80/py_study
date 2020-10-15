hello="문자열입니다."
print(hello)

#문자열의 길이
print("문자열의 길이는 : ", len(hello))

#문자열 선택 연산자(인덱스)
print(hello[0:2])
print(hello[2:len(hello)])
print("문자열의 뒤에서 부터 선택 :: ", hello[-1])

#문자열 반복 연산자 *
print(hello * 3)


#문자열 연결 연산자
print(hello + hello)

#자료형 확인하기
print(type(hello))
