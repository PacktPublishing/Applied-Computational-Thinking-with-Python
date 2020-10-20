import math
numberTiers = int(input("How many tiers of pledges will you offer? Enter a number between 3 and 5 inclusive. "))

#Number of tiers percentages
if numberTiers == 3:
    tier1 = .50
    tier2 = .30
    tier3 = .20
elif numberTiers == 4:
    tier1 = .40
    tier2 = .30
    tier3 = .20
    tier4 = .10
elif numberTiers == 5:
    tier1 = .40
    tier2 = .30
    tier3 = .15
    tier4 = .10
    tier5 = .05
else:
    print("Please try again and enter the numbers 3, 4, or 5. ")

#Number of items per tier
if numberTiers == 3:
    numTier1Items = int(input("How many items will be provided for a Tier 1 pledge? "))
    numTier2Items = int(input("How many items will be provided for a Tier 2 pledge? "))                 
    numTier3Items = int(input("How many items will be provided for a Tier 3 pledge? "))
elif numberTiers == 4:
    numTier1Items = int(input("How many items will be provided for a Tier 1 pledge? "))
    numTier2Items = int(input("How many items will be provided for a Tier 2 pledge? "))                 
    numTier3Items = int(input("How many items will be provided for a Tier 3 pledge? "))
    numTier4Items = int(input("How many items will be provided for a Tier 4 pledge? "))
elif numberTiers == 5:
    numTier1Items = int(input("How many items will be provided for a Tier 1 pledge? "))
    numTier2Items = int(input("How many items will be provided for a Tier 2 pledge? "))                 
    numTier3Items = int(input("How many items will be provided for a Tier 3 pledge? "))
    numTier4Items = int(input("How many items will be provided for a Tier 4 pledge? "))
    numTier5Items = int(input("How many items will be provided for a Tier 5 pledge? "))

#Price points for each Tier
if numberTiers == 3:
    priceTier1 = int(input("What is the price point of Tier 1? Enter dollar amount without dollar sign. "))
    priceTier2 = int(input("What is the price point of Tier 2? Enter dollar amount without dollar sign. "))                
    priceTier3 = int(input("What is the price point of Tier 3? Enter dollar amount without dollar sign. "))
elif numberTiers == 4:
    priceTier1 = int(input("What is the price point of Tier 1? Enter dollar amount without dollar sign. "))
    priceTier2 = int(input("What is the price point of Tier 2? Enter dollar amount without dollar sign. "))                 
    priceTier3 = int(input("What is the price point of Tier 3? Enter dollar amount without dollar sign. "))
    priceTier4 = int(input("What is the price point of Tier 4? Enter dollar amount without dollar sign. "))
elif numberTiers == 5:
    priceTier1 = int(input("What is the price point of Tier 1? Enter dollar amount without dollar sign. "))
    priceTier2 = int(input("What is the price point of Tier 2? Enter dollar amount without dollar sign. "))              
    priceTier3 = int(input("What is the price point of Tier 3? Enter dollar amount without dollar sign. "))
    priceTier4 = int(input("What is the price point of Tier 4? Enter dollar amount without dollar sign. "))
    priceTier5 = int(input("What is the price point of Tier 5? Enter dollar amount without dollar sign. "))

#Breakdown of number of Tiers based on funding goal
fundGoal = int(input("What is the funding goal for this campaign? Enter dollar amount with no symbols. "))

if numberTiers == 3:
    Tier1Total = math.ceil(fundGoal*tier1/priceTier1)
    Tier2Total = math.ceil(fundGoal*tier2/priceTier2)
    Tier3Total = math.ceil(fundGoal*tier3/priceTier3)
    print("For a funding goal of %s with %s tiers, you'll need %s Tier 1 pledges, %s Tier 2 pledges, and %s Tier 3 pledges. " % (fundGoal, numberTiers, Tier1Total, Tier2Total, Tier3Total))
    Tier1Items = numTier1Items*Tier1Total
    Tier2Items = numTier2Items*Tier2Total
    Tier3Items = numTier3Items*Tier3Total
    print("For %s Tier 1 pledges, you'll need %s items. For %s Tier 2 pledges, you'll need %s items. For %s Tier 3 pledges, you'll need %s items. " %(Tier1Total, Tier1Items, Tier2Total, Tier2Items, Tier3Total, Tier3Items))
elif numberTiers == 4:
    Tier1Total = math.ceil(fundGoal*tier1/priceTier1)
    Tier2Total = math.ceil(fundGoal*tier2/priceTier2)
    Tier3Total = math.ceil(fundGoal*tier3/priceTier3)
    Tier4Total = math.ceil(fundGoal*tier4/priceTier4)
    print("For a funding goal of %s with %s tiers, you'll need %s Tier 1 pledges, %s Tier 2 pledges, %s Tier 3 pledges, and %s Tier 4 pledges. " % (fundGoal, numberTiers, Tier1Total, Tier2Total, Tier3Total, Tier4Total))
    Tier1Items = numTier1Items*Tier1Total
    Tier2Items = numTier2Items*Tier2Total
    Tier3Items = numTier3Items*Tier3Total
    Tier4Items = numTier4Items*Tier4Total
    print("For %s Tier 1 pledges, you'll need %s items. For %s Tier 2 pledges, you'll need %s items. For %s Tier 3 pledges, you'll need %s items. For %s Tier 4 pledges, you'll need %s items. " %(Tier1Total, Tier1Items, Tier2Total, Tier2Items, Tier3Total, Tier3Items, Tier4Total, Tier4Items))
elif numberTiers == 5:
    Tier1Total = math.ceil(fundGoal*tier1/priceTier1)
    Tier2Total = math.ceil(fundGoal*tier2/priceTier2)
    Tier3Total = math.ceil(fundGoal*tier3/priceTier3)
    Tier4Total = math.ceil(fundGoal*tier4/priceTier4)
    Tier5Total = math.ceil(fundGoal*tier5/priceTier5)
    print("For a funding goal of %s with %s tiers, you'll need %s Tier 1 pledges, %s Tier 2 pledges, %s Tier 3 pledges, %s Tier 4 pledges, and %s Tier 5 pledges. " % (fundGoal, numberTiers, Tier1Total, Tier2Total, Tier3Total, Tier4Total, Tier5Total))
    Tier1Items = numTier1Items*Tier1Total
    Tier2Items = numTier2Items*Tier2Total
    Tier3Items = numTier3Items*Tier3Total
    Tier4Items = numTier4Items*Tier4Total
    Tier5Items = numTier5Items*Tier5Total
    print("For %s Tier 1 pledges, you'll need %s items. For %s Tier 2 pledges, you'll need %s items. For %s Tier 3 pledges, you'll need %s items. For %s Tier 4 pledges, you'll need %s items. For %s Tier 5 pledges, you'll need %s items. " %(Tier1Total, Tier1Items, Tier2Total, Tier2Items, Tier3Total, Tier3Items, Tier4Total, Tier4Items, Tier5Total, Tier5Items))
       
