string='''The apple doesn't fall. ...
All that glitters are not gold. ...
A picture is worth a thousand words. ...
Beggers can't be choosers. ...
A bird in the hand. ...
Better safe than sorry. ...
An apple a day keeps doctor away. ...
Blood is thicker than water. ...'''
str1=string.split(" ...")
print("Total number of lines:",len(str1))
count=0
for i in str1:
    str2=i.split()
    for j in str2:
        if j[0]=="B":
            count=count+1
print("Number of Sentences that start with letter B :",count)

