import collections

def solution(participant, completion):
    answer = ''
    answer=collections.Counter(participant)-collections.Counter(completion)
    answer=list(answer.keys())
    return answer


p=["mislav","stanko","mislav","ana"]
c=["stanko","ana","mislav"]

print(collections.Counter(p))
#Counter({'c': 1, 'd': 1, 'e': 1, 'b': 1, 'a': 1})
print(collections.Counter(c))
#Counter({'a': 1, 'e': 1, 'd': 1, 'b': 1})

print(type(collections.Counter(p)))

print(collections.Counter(p)-collections.Counter(c))
answer=collections.Counter(p)-collections.Counter(c)
print(answer)
print(type(answer))
print(answer.keys())
print(list(answer.keys()))
print(list(answer.keys())[0])

print("*********")
p=["mislav","stanko","mislav","ana"]
c=["stanko","ana","mislav"]
dict={}
print(dict)
for p_ in p:
    print(p_)
    if p_ in dict:
        dict[p_] += 1
    else:
        dict[p_] = 1
    print(dict)
for p_ in dict:
    print(p_, dict[p_])

print("----------")
p=["mislav","stanko","mislav","ana"]
c=["stanko","ana","mislav"]
dic = {}
temp = 0
for p_ in p:
    dic[hash(p_)] = p_
    print("dic: ", dic)
    temp += int(hash(p_))
    print("temp: ",temp)
for c_ in c:
    temp -= int(hash(c_))
    print("temp: ",temp)
answer = dic[temp]

print(answer)

