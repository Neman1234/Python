#create variablese an 
story = "in the quiet, mist-wrapped town of Elmridge,n wherold clocktower stood frozen at 3:17 and ignored by wary townsfolk who feared its whispers,\n twelve-year-old Mira—skeptical of ghost tales—followed the tower’s eerie midnight call, crept across the foggy square with flashlight in hand,\n ascended the spiral stairs as whispers grew louder with every step, discovered her name carved into the wood beside a keyhole, reached instinctively into her pocket to find a key she never knew she had, and with a trembling hand turned it, awakening the slumbering gears, ringing the bells, stirring the fog, and unlocking not just the hands of time, but the lost memories and buried truths of a town held still for over a hundred years."

#print story and the story length
print(story)
print(len(story))
print("The length of the story is  :" , len(story))

#check the last word in the story to make sure i got it correct
print(story.endswith("years."))

#count how many commas are there
print("There are" , story.count(",") , "commas in this story")

#Capitalize Lettersin the story
print(story.capitalize())

#Find a word in the story
print(story.find("feared"))

#replace a word for another word in the story
print(story.replace("Elmridge", "ashburn"))