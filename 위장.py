def solution(clothes):
    answer = 0
    hashMap = {}
    for cloth in clothes:
        if cloth[1] not in hashMap.keys():
            hashMap[cloth[1]] = 1
        else:
            hashMap[cloth[1]] += 1
    answer = 1
    for key in hashMap.values():
        answer *= (key + 1)
    return answer-1


clothes = [
    ["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]
]

hashMap={}
for cloth in clothes:
    print(cloth)
    print(cloth[1])
    if cloth[1] not in hashMap.keys():
        hashMap[cloth[1]] = 1
    else:
        hashMap[cloth[1]] += 1
print(hashMap)
answer = 1
for key in hashMap.values():
    answer *= (key+1)
print(answer-1)
print(hashMap.keys())