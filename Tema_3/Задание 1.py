#  реализовать сортировку пузырьком (НЕ КОПИПАСТИТЬ)
a = [100, 77, 56, -5, 0, 89, 12]
def count(now_spk):
    last_elm = len(now_spk) - 1
    for i in range(0, last_elm):
        for x in range(0, last_elm):
            if now_spk[x] > now_spk[x + 1]:
                now_spk[x], now_spk[x + 1] = now_spk[x + 1], now_spk[x]
    return now_spk


new_list = count(a).copy()
print(new_list)