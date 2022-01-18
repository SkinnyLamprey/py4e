text = 'X-DSPAM-Confidence: 0.8475'
str = text.find(':')
#print(str)
num = text[str+1:]
num = float(num)
print(num)