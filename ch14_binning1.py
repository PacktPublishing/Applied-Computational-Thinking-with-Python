#Binning with equal frequency
def equal_frequency(array1, m): 
	l = len(array1) 
	n = int(l / m) 
	for i in range(0, m): 
		array = [] 
		for j in range(i * n, (i + 1) * n): 
			if j >= l: 
				break
			array = array + [array1[j]] 
		print(array) 
#Input dataset 
dataset = [3, 6, 7, 9, 11, 14, 10, 15, 19, 35, 38, 45, 48, 49, 76] 
#Input number of bins
m = 5
print("Equal Frequency Binning: ") 
equal_frequency(dataset, m) 
