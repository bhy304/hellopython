# 딕셔너리 : (일반적으로) 문자열을 기반으로 값을 저장하는 것

dict_a = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}
print(dict_a["name"])
print(dict_a["type"])
print(dict_a["ingredient"])
print(dict_a["ingredient"][0])
print(dict_a["ingredient"][1])
print(dict_a["origin"])

# 딕셔너리 추가 : dict_a["new_name"] = 10
dict_a["price"] = 5000
dict_a["name"] = "8D 건조 망고"
# print(dict_a)

# 딕셔너리 제거 : del dict_a["name"]
del dict_a["origin"]
# print(dict_a)

# 딕셔너리 확인 : key in dict_a
key = "name"
if key in dict_a:
    print(dict_a[key])
else:
    print(key, "는 존재하지 않습니다.")

print()
print(dict_a.get("name"))

name_value = dict_a.get("dddddd") #없으면 None 출력!
if name_value != None:
    print(name_value)
else:
    print("키가 존재하지 않습니다.")