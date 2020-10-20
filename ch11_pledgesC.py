import math

tier1 = 1600
tier2 = 800
tier3 = 700

perc = int(input("What percentage of the 100,000 do you expect will be Tier 1? Type a number between 1 and 100. "))

percTier1 = perc/100
percTier2 = (100-perc)/3/100
percTier3 = (100-perc-percTier2)/100

Tier1 = (100000*percTier1)/1600
totalTier1 = math.ceil(Tier1)
itemsTier1 = totalTier1*2
accTier1 = totalTier1
cases1 = totalTier1
yearMemb = totalTier1

Tier2 = (100000*percTier2)/800
totalTier2 = math.ceil(Tier2)
itemsTier2 = totalTier2
cases2 = totalTier2
sixMemb = totalTier2

Tier3 = (100000*percTier3)/700
totalTier3 = math.ceil(Tier3)
itemsTier3 = totalTier3
cases3 = totalTier3

totalItems = itemsTier1 + itemsTier2 + itemsTier3
totalAccessories = accTier1
totalCases = cases1 + cases2 + cases3

print("You will need to sell %s Tier 1 pledges if you want %s percent of your sales to be in Tier 1." %(totalTier1, perc))
print("You will need %s Tier 2 pledges and %s Tier 3 pledges to meet or exceed your $100,000 funding goal." % (totalTier2, totalTier3))
print("These percentages are equivalent to %s total items, %s total cases, %s accessories kits, %s year-long memberships, and %s six-month memberships." \
      % (totalItems, totalCases, totalAccessories, yearMemb, sixMemb))



