import sys

def readFile(filename):
	dic = {}
	chars = []
	with open(filename, 'r') as f:
		data = f.read()
		for char in data:
			if char in dic:
				dic[char]+=1
				chars.append(char)
			else:
				dic[char]=0
				chars.append(char)
	f.close()
	return dic, chars

if __name__ == "__main__":
	filename = sys.argv[1]
	print readFile(filename)