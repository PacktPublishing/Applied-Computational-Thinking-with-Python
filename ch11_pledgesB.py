import math

tier1 = 1600
tier2 = 800
tier3 = 700

perc = int(input("What percentage of the 100,000 do you expect will be Tier 1? Type a number between 1 and 100. "))
percentage = perc/100

Tier1 = (100000*percentage)/1600
totalTier1 = math.ceil(Tier1)

print("You will need to sell %s Tier 1 pledges if you want %s percent of your sales to be in Tier 1." % (totalTier1,perc))
print("You will need %s items, %s accessories kits, %s carrying cases, and %s year-long memberships." %(totalTier1*2, totalTier1, totalTier1, totalTier1))



