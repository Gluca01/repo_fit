from fitparse import FitFile
import numpy as np
from tkinter import *
root = Tk()
root.geometry("1500x1500")
canvas = Canvas(root,width=1200,height=1200,bg="white")


# open the fit file
fitfile = FitFile('activity2.fit')
power = []


for record in fitfile.get_messages("record"):
    # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
    for data in record:
        # Print the name and value of the data (and the units if it has any)
        if data.name == 'power':
            power.append(data.value)


ndata = len(power)
print('lenght =',ndata)
print('average power =',np.mean(power))

x0 = []
for i in range(len(power)):
  x0.append(i)

P = []
maxv=1000
cont=1
n=0
value=0
for x1 in range(ndata):
    if ((x1+1)/ndata*maxv) < cont:
        value = value + power[x1]
        n = n + 1
    else:
        P.append(int(value/n))    
        n=1
        cont=cont+1
        value = power[x1]
        
        
        
print(P)       
print('average power =',np.mean(P))

# x= [0,100,200,300,400]
# y= [120,150,140,180,190]

for i in range(maxv-1):
    canvas.create_line(x0[i], 500-P[i], x0[i+1],500-P[i+1], width=1)

# borders



canvas.pack(expand=1)


root.mainloop()


