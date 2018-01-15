import random
# make random random in range
nums = [num * random.randrange(10, 25) for num in range(1, 6)]
print(sum(nums, 0), nums)

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
sumareas = [i for i in areas if isinstance(i, float) or isinstance(i, int)] # range only costs in independent list
print(sumareas)

# Sum of kitchen and bedroom area: eat_sleep_area
odd = [areas[x] for x in range(len(areas)) if not x % 2 == 0] # map odds in index of array

beds = ['kitchen', 'bedroom']
twobedscost = [areas.index('kitchen') + 1, areas.index('bedroom') + 1]
# sum cost of beds only
sumthis = map(lambda i: areas[areas.index(i) + 1], beds)
eat_sleep_area = sum(sumthis, 0)
#
allsum = sum(sumareas, 0)
print(eat_sleep_area, allsum)
names = map(lambda x: x if isinstance(x, str) else areas.remove(x), areas)
print(list(names), areas)
