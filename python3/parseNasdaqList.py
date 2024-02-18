infile = open('nasdaqList.txt')
outfile = 'nasdaqSymbols.txt'

# reading the file as a list line by line
content = infile.readlines()

# closing the file
infile.close()
#print(content)

tickers = []
for x in content:
    a = x.split('|')[0]
    tickers.append(a)

print(tickers)
