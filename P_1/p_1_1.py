def time_string(sec):
    hou, min = 0, 0

    while sec >= 60:
        min+=1
        sec-=60
        if min >= 60:
            hou += 1
            min -= 60

    print(f'{hou}:{min}:{sec}')


def list_sum(lst):
    return sum(lst)

print((first[0] + first[-1])/2 * len(first))

# for time in schedule:
#     if parrot%100 <=40:
#         if abs(time - parrot) < dif and abs(time - parrot) >=5 and time > parrot:
#             nearest_parrot = time
#             dif = abs(time - parrot)
#             print(nearest_parrot)
#             return abs(nearest_parrot - parrot) - 5 if abs(nearest_parrot - parrot) <=45 else abs(nearest_parrot - parrot) - 45
#     else:
#         if abs(time - parrot) < dif and abs(time - parrot) >= 45 and time > parrot:
#             nearest_parrot = time
#             dif = abs(time - parrot)
#             return abs(nearest_parrot - parrot) - 45

