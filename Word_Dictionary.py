#create Dictionary
Server = {
    "Neel": ("normal","Joined 5 years ago","Birthday is November 9th 2016"),
    "Elon Musk": (" Chief executive officer ","Joined 20 years ago","Birthday is November 9th 1978")
}

#print dictionary
#print(Server["Neel"])
#Server=str(Server)
#print(Server[0:68])
Server["Neel"]="normal"
Server["Elon Musk"]="ceo"
print(Server)