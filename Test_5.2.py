OldServerValues = {
    "Numbers":[1,2,3,4,5,6,7,8,9,10]
}

NewServerValues = {
    "Numbers":[1,2,3,4,5],
    "Letters":["w","a"]
}

OldServerValues.update(NewServerValues)

print(OldServerValues)