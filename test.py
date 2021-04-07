from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys
import math

images = []

#image of suit
suit = Image.open('suit.png')

f = ImageFont.truetype("fonts\\consolab.ttf",38)
text =  "This is some smoooooooooooooooooooooth test text, if it works I will be happy"
# length = len(text)-4
wrapped = False
counter = 0
offsetX = 0
offsetY = 0

xOrigin = 110
yOirign = 0


#half the pixel length of a single char
offsetXoffset = 10.5

#.139 is the ratio of x:y at an 8 degree angle
offsetYoffset = offsetXoffset*.139


if(len(sys.argv)>1):
	text = sys.argv[1]



firstChars = text[0:4]

text = text +" " + firstChars

# first_word = text.split()[0]
# text = text + " " + first_word

length = len(text) - len(firstChars)


imgHeight = int(math.sin(math.radians(8))*(21*(length+4)))
imgWidth = 21*(length+4)

while(not(wrapped)):

	#yoffset = int(counter*0.5)


	#image of empty helmet
	face = Image.open('empty.png')

	#create new image with desired text
	txt = Image.new("L",(imgWidth,imgHeight))


	d = ImageDraw.Draw(txt)
	d.text( (0, 0), text,  font=f,fill=255)
	w=txt.rotate(8,  expand=1)

	#print(d.textlength(text,font=f))
	#w.save("debug3.png")
	yOirign = (21+10+86) - (math.sin(math.radians(8))*d.textlength(text,font=f))

	#add text to helmet image
	face.paste( ImageOps.colorize(w, (0,0,0), (115,229,255)), (int(110-offsetX),int(yOirign+offsetY)),  w)

	#overylay the suit image
	face.paste(suit, (0, 0), suit)

	face.save("images\\test"+str(counter)+".png")
	images.append(face)

	counter+=1

	offsetX+=offsetXoffset
	offsetY+=offsetYoffset
	# if(counter%2==0):
	# 	text = text[1::]

	#if(counter*offset>=f.getlength(text)):
	#	wrapped = True 
	if(counter>=length*2):
		wrapped = True
images[0].save('test.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)