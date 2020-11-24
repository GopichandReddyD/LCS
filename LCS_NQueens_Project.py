from math import ceil
import sys
import os

file = open("input.cnf", mode='w')


def main():
	global file

	if len(sys.argv) == 1:
		N = int(input("Enter n: "))
	else:
		N = int(sys.argv[1])
	if N < 4:
		print("UNSATISFIALE")
		exit()
	counter = (N * (N - 1) * (5 * N - 1)) / 3
	counter += N

	# Printing File header which is in the DIMACS CNF Format
	file.write("p cnf {0:d} {1:d}\n".format((N * N), int(counter)))

	printRowClauses(N)
	printColomnClauses(N)
	printDiagonallyClauses(N)

	file.close()

	
	exe = "minisat "+ "input.cnf" + " " + "output.txt"
	os.system(exe)

def printRowClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1
	global file

	for i in range(1, lim):
		file.write("{0:d} ".format(i))
		if i % N == 0:
			file.write("0\n")
			

	# loop which will go through all the squares of the board
	for i in range(1, lim):
		row = ceil(i / N)  # determining the row number based on the square number

		# loop to print the clauses present
		for j in range(i, row * N + 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))


def printColomnClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1

	# loop which go through all the squares of the board present
	for i in range(1, lim):

		# loop which print the clauses
		for j in range(i, lim, N):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))


def printDiagonallyClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1

	# loop which go through all the squares of the board
	for i in range(1, lim):
		# getting row and column
		row = ceil(i / N)
		col = i % N

		if col == 0: col = N

		# loop which print the Left to Right Diagonal clauses
		for j in range(i, min(((N - col + row) * N + 1), lim), N + 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))

	# loop which go through all the squares of the board
	for i in range(1, lim):
		# loop which print the Right to Left Diagonal clauses
		for j in range(i, lim, N - 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			elif ceil((j - (N - 1)) / N) == ceil(j / N):
				break
			file.write("-{0:d} -{1:d} 0\n".format(i, j))

main()
