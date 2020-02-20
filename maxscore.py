#get data
file = open("a_example.txt", 'r')
data = [line.strip('\n').split(' ') for line in file.readlines()]
for i in range(len(data)):
		data[i] = list(map(int, data[i]))

#bestof3
listoflib = [0]*data[0][1]

#get max-score point 1
bookscore = list(map(int, data[1]))
scoreperlib = []
for i in range(3,len(data),2):
	sum = 0
	for j in range(len(data[i])):
		sum = sum + bookscore[data[i][j]]
	scoreperlib.append(sum)
listoflib[scoreperlib.index(max(scoreperlib))] = scoreperlib.index(max(scoreperlib)) + 1

#signup days point 2
scoresignup = []
for i in range(2,len(data),2):
	scoresignup.append(data[i][2])
listoflib[scoresignup.index(min(scoresignup))] = scoresignup.index(min(scoresignup)) + 1

#books/shipping point 3
scoreforship = []
for i in range(2,len(data),2):
	scoreforship.append(data[i][2])
listoflib[scoreforship.index(min(scoreforship))] = scoreforship.index(min(scoreforship)) + 1

print(listoflib)
