#!/usr/bin/python3
import random

def main():
	#print("Keep it logically awesome.")
	#print("Saket")
	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()
	#print(len(quotes))
	last = 13
	rnd = random.randint(0,last)
	print(quotes[rnd])

if __name__ == "__main__":
	main()
