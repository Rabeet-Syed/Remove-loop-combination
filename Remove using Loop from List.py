

num = [1,1,3,1,5,1,76,1,8,1,4,1]
print(num)
for x in range(0,7,+1):
    num.remove(1)
print(num)


# 0-7 because counting will start form 0 and end on 7 but will not include 7 so total iterations will be 6 that will be
# performed we can also write 1-8 or 2-9 etc having gap of 7  because we have 7 ---- 0nes in that list that we have to
# remove
