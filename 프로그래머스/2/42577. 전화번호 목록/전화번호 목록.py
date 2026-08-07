# 시간 복잡도 : O(n logn), 공간 복잡도 : O(1)

def solution(phone_book):
    phone_book.sort()

    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i - 1]):
            return False

    return True