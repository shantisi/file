banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("question3.txt","a")
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i=i+1
