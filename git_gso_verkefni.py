#Gsö verkefni
#Arnar Ólafsson
#26.01.17

text = open("texti.txt","w")
text.write("halló heimur ")
text.close()
text = open("texti.txt", "a")
text.write("Þetta er lína 1 ")
text.write("þetta er lína 2 ")
text.write("þetta er lína 3 ")
text.close()


