if True:
    print("True입니다.")
    print("정말 True입니다.")


if True:
    print("True")
else:
    print("Else")


aval=1
if aval == 0:
    print("zero")
elif aval == 1:
    print("one")
else:
    print("other")

# 미구현한 상태일 경우 pass 키워드를 통해서 넘김.
if True:
    pass
else:
   pass

# 미구현한 상태일 경우 raise NotImplementedError
if True:
    raise NotImplementedError
else:
   raise NotImplementedError