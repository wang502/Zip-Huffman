import sys

def readBin(filename):
	result = ""
	with open(filename, 'r') as f:
		data = f.read()
		for char in data:
			bin = format(ord(char), 'b')
			if data.index(char) == len(data)-1:
				result += bin
				break
			if len(bin) < 8:
				bin = "0"*(8-len(bin)) + bin
			result += bin
	f.close()
	return result

if __name__ == "__main__":
	filename = sys.argv[1]
	binString = readBin(filename)
