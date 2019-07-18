
#CheapoMax 20L £19.99 10square meters per l
#AverageJoes 15L £17.99 11 square meters per l
#DuluxourousPaints 10L £25 20square meters per l
CheapoMax = [20, 19.99, 10] #liters, price, meters per litre
AverageJoes = [15,17.99, 11]
Duluxorous = [10, 25, 20]
roomMeters = int(input("How many square meters room has? \n"))

#caluclate how many liters of paint will be left over
CheapoMaxTotalSquareMeters = CheapoMax[0] * CheapoMax[2]
AverageJoesTotalSquareMeters = AverageJoes[0] * AverageJoes[2]
DuluxorousTotalSquareMeters = Duluxorous[0] * Duluxorous[2]
#calculate how many cans will be needed
CheapoMaxCansNeeded = roomMeters//CheapoMaxTotalSquareMeters + (roomMeters % CheapoMaxTotalSquareMeters > 0)
AverageJoesNeeded = roomMeters//AverageJoesTotalSquareMeters + (roomMeters % AverageJoesTotalSquareMeters > 0)
DuluxorousNeeded = roomMeters//DuluxorousTotalSquareMeters + (roomMeters % DuluxorousTotalSquareMeters > 0)

#caluclate total price
TotalPriceForCheapoMax = CheapoMaxCansNeeded * CheapoMax[1]
TotalPriceForAverageJoes= AverageJoesNeeded * AverageJoes[1]
TotalPriceForDuluxorous = DuluxorousNeeded * Duluxorous[1]

#calc remaining sq meters of paint
CheapoMaxWaste = CheapoMaxCansNeeded * CheapoMaxTotalSquareMeters - roomMeters
AverageJoesWaste = AverageJoesNeeded * AverageJoesTotalSquareMeters - roomMeters
DuluxorousWaste = DuluxorousNeeded * DuluxorousTotalSquareMeters - roomMeters
#calc remainig liters of paint
CheapoMaxWasteInLiters = CheapoMaxWaste // CheapoMax[2]
AverageJoesWasteInLiters = AverageJoesWaste // AverageJoes[2]
DuluxorousWasteInLiters = DuluxorousWaste // Duluxorous[2]
print("cheapo max costs: £", TotalPriceForCheapoMax, "with pain left to paint: " , CheapoMaxWaste , "square meters, with about: " , CheapoMaxWasteInLiters , " Liters of paint left")
print("AverageJoes costs: £", TotalPriceForAverageJoes, "with pain left to paint: ", AverageJoesWaste, "square meters, with about: " , AverageJoesWasteInLiters , " Liters of paint left")
print("Duluxorous costs: £", TotalPriceForDuluxorous, "with pain left to paint: ", DuluxorousWaste, "square meters, with about: " , DuluxorousWasteInLiters , " Liters of paint left\n\n")

if TotalPriceForCheapoMax < TotalPriceForAverageJoes and TotalPriceForCheapoMax < TotalPriceForDuluxorous:
    print("cheapest paint is cheapo max costing: £", TotalPriceForCheapoMax, "with painr left to paint: " , CheapoMaxWaste , "square meters ")
elif TotalPriceForAverageJoes < TotalPriceForCheapoMax and TotalPriceForAverageJoes < TotalPriceForDuluxorous:
    print("cheapest paint is AverageJoes costing: £", TotalPriceForAverageJoes, "with painr left to paint: " , AverageJoesWaste , "square meters ")
elif TotalPriceForDuluxorous < TotalPriceForCheapoMax and TotalPriceForDuluxorous < TotalPriceForAverageJoes:
    print("cheapest paint is Duluxorous costing: £", TotalPriceForDuluxorous, "with painr left to paint: " , DuluxorousWaste , "square meters ")


