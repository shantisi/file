list=["rishabh - meerut","imtiyaz - delhi","nilima - cochin","rati - shimla",
"ayishah - delhi","raghu - shimla","naseer - kanpur","karthikeyan - delhi",
"salma - jaipur","pankaj - delhi","brijesh - delhi","govind - delhi","puneet - shimla",
"siddhi - delhi","suman - jaipur","rajeev - shimla","mohinder - delhi","rajendra - jaipur",
"priyanka - shimla","neela - delhi","sashi - jaipur","sarika - delhi","deepti - shimla",
"harshad - delhi","trishna - raipur","pradeep - jaipur","sekhar - delhi","nand - delhi",
"anoop - delhi","balwinder - tokyo"]
file = open("people1.txt","w")
i=0
while i<len(list):
    file.write(list[i])
    file.write("\n")
    i=i+1