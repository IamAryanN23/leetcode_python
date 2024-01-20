def jewelinstone(jewels, stones):
    count =0
    for i in stones:
        if i in jewels:
            count+=1
    return count

jewels = "aA"
stones = "aAAbbbb"
print(jewelinstone(jewels, stones))
