newlist = [x for x in range(0,101) if x%3 == 0 and x%5 == 0]
# more effcient way [x for x in range(0, 101, 15)]
print(newlist) 