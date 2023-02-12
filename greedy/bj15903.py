# 15903번 - 카드 합체 놀이

# 가장 작은 점수를 계산하는 프로그램

# x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
# 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.


x, y = map(int, input().split())
card = list(map(int, input().split()))


for i in range(y) :
    # 카드 오름차순 정렬
    card = sorted(card)
    # 두 장의 카드의 값을 더한다
    cover = card[0] + card[1]
    # 두 장의 카드에 cover값을 덮어 씌움
    card[0] = cover
    card[1] = cover

print(sum(card))
