def heap_for_i(arr, n, i):
	left=2*i+1
	right=2*i+2
	large=i
	if left<n and arr[left]>arr[i]:
		large=left
	if right<n and arr[right]>arr[large]:
		large=right
	if large!=i:
		arr[i], arr[large] = arr[large], arr[i]
		heap_for_i(arr, n, large)

def Sort(arr):
	n=len(arr)
	for i in range(n//2-1, -1, -1):
		heap_for_i(arr, n, i)
	for i in range(n-1,-1,-1):
		arr[i], arr[0] = arr[0], arr[i]
		heap_for_i(arr, i, 0)
	return arr
