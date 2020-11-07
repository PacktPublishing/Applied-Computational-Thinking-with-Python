#Binning with equal width 
def equal_width(array1, m): 
	w = int((max(array1) - min(array1)) / m) 
	min1 = min(array1) 
	array = [] 
	for i in range(0, m + 1): 
		array = array + [min1 + w * i] 
	arrayi=[] 
	for i in range(0, m): 
		result = [] 
		for j in array1: 
			if j >= array[i] and j <= array[i+1]: 
				result += [j] 
		arrayi += [result] 
	print(arrayi) 

#Input dataset 
dataset = [3, 6, 7, 9, 11, 14, 10, 15, 19, 35, 38, 45, 48, 49, 76, 81, 208, 221] 
#Input number of bins
m = 3

print("\nEqual Width Binning:") 
equal_width(dataset, m)
