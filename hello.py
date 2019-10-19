print("안녕하세요")
print(920+1234)
print(3>9)

name = "은수"
print("저는" + name+"입니다")

eunsoo = {
    "name" : "미나",
    "age" : "13",
    "gender" : "여"
}

print("저는 만 " + eunsoo["age"] + " 살입니다.")

# 문제!
# 남, 은수, 14라는 글자를 쓰지 말고,
# "은수는 만 14살의 남학생입니다"라고 출력되게 해보자.

print(eunsoo["name"]+"는" + eunsoo["age"] +" 살의 "+ eunsoo["gender"] + "학생입니다.")

# n=0
# while True:
#     print(n)
#     n+=1
