

num = [1,'Good',1,'Good',3,1,'Good',5,'Good',1,76,'Good','Good',1,8,'Good',1,4,1]
print(num)
for x in range(0,7,+1):
    num.remove("Good")
print(num)


# 0-7 because counting will start form 0 and end on 7 but will not include 7 so total iterations will be 6 that will be
# performed we can also write 1-8 or 2-9 etc having gap of 7  because we have 7 ---- 0nes in that list that we have to
# remove
