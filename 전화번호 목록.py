def solution(phone_book):
    for phone_number in phone_book:
        temp = 0
        for phone_number2 in phone_book:
            if phone_number2.find(phone_number) != -1:
                temp += 1
            if temp == 2:
                return False
    return True

phone_book=["119","97674223","1195524421"]
print(solution(phone_book))

phone_book=["123","456","789"]
print(solution(phone_book))

phone_book=["12","123","1235","567","88"]
print(solution(phone_book))

hashMap = {}
for phone_number in phone_book:
    hashMap[phone_number] = 1
    print(hashMap)
for phone_number in phone_book:
    temp = ""
    for number in phone_number:
        temp += number
        if temp in hashMap and temp != phone_number:
            answer=False
