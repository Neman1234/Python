OldWebsiteusers = {
"Bilgates": "Ceo",
"Elon Musk": "Normal"
}


NewWebsiteUsers = {
    "Neel": "Co Founder",
    "Bilgates": "Ceo",
    "Elon Musk": "Normal"
}

print(OldWebsiteusers.get("Neel"))

(OldWebsiteusers.update(NewWebsiteUsers))
print(OldWebsiteusers)

print(OldWebsiteusers.keys())
print(OldWebsiteusers.values())
print(OldWebsiteusers.items())