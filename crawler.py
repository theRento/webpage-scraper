import urllib
import re
url = raw_input("Enter URL")
link = urllib.urlopen('"'+url+'"')
html = link.read()
text = [k.start() for k in re.finditer('<img src="', html)]
links = []
for i in text :
	string = ""
	j = 10
	while True :
		if html[i+j] == '"' :
			break
		else :
			string += html[i+j]
			j += 1
	links.append(string)
j = 0
for i in links :
	image = urllib.URLopener(i)
	image.retrieve(i, j, hook())
	j += 1

def hook(num_of_blocks, block_size, file_size) :
	print "%s percent of the image file downloaded"%(num_of_blocks*block_size*100/file_size)



