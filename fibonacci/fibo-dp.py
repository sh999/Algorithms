'''
fibo-dp.py
Dynamic programming solution to computing nth Fibonacci number
Do this by memorizing previous computations
Much better than recursive solution, which can be (O(2^n)). 
This solution is O(n), disregarding arithmetic time
'''
import sys, pprint

def fibo(n):
	'''
		Return value of nth fibonacci number (hereby called f(n))
	'''
	n = int(n)
	memory = {0:0,1:1}  # Set memory table with f(0) and f(1)
	if n in memory: 	# Edge case if user asks trivially f(0) or f(1)
		return memory[n]
	else:
		to_solve = [i for i in range(2,n+1)] 		# Get list of numbers of nth fibo numbers to solve. e.g. to solve f(5), need to solve f(4), f(3)... f(0)
		for i in to_solve:   						# Build memory table from bottom up f(0), f(1), f(2), ...
			memory[i] = memory[i-1] + memory[i-2]	# f(n) = f(n-1) + f(n-2)
		return memory[n]

def main():
	n = sys.argv[1]
	print "f(",n,") = ", fibo(n)

main()

