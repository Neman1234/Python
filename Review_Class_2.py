#String Slicing
 
story = '''The demand for expertise in AI and machine learning is growing rapidly. By enabling new technologies like self-driving cars and recommendation systems or improving old ones like medical diagnostics and search engines, AI is transforming how we live, work, and play. This series will enable you to take the first steps toward understanding programming fundamentals so you can solve important real-world problems and future-proof your career.
 
This professional certificate series combines CS50’s legendary Introduction to Computer Science course with a new program that takes a deep dive into the concepts and algorithms at the foundation of modern artificial intelligence. This series will lead you through the most popular undergraduate course at Harvard, where you’ll learn the common programming languages, then carries that foundation through CS50’s Introduction to Artificial Intelligence with Python. Through hands-on projects, you’ll gain exposure to the theory behind graph search algorithms, classification, optimization, reinforcement learning, and other topics in artificial intelligence.
 
By course’s end, student'''

#print variable
print(story[14:25])
print("The length is :" , len(story))
print(story.endswith("development"))
print("There are", story.count(","), "commas in the story")
print(story.capitalize())
print(story.find("and"))
print(story.replace("and", "or"))
