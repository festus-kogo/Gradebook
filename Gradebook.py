# Create Some Lists:

subjects = ["physics", "calculus", "poetry", "history"]
# print(subjects)

grades = [98, 97, 85, 88]
# print(grades)

gradebook = [
    ["physics", 98], 
    ["calculus", 97], 
    ["poetry", 85], 
    ["history", 88]]

print(gradebook)
# Output
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

gradebook.append(["computer science", 100])
print(gradebook)
# Output
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100]]

gradebook.append(["visual arts", 93])
print(gradebook)
# Output
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 93]]

gradebook[-1][-1] += 5
print(gradebook[-1][-1])
# Output
# 98
# print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 98]]

gradebook[2].remove(85)
# print(gradebook)
# Output
# [['physics', 98], ['calculus', 97], ['poetry'], ['history', 88], ['computer science', 100], ['visual arts', 98]]

gradebook[2].append("Pass")
# print(gradebook)
# Output
# [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
# Output
# [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65], ['physics', 98], ['calculus', 97], ['poetry', 'Pass'], 
# ['history', 88], ['computer science', 100], ['visual arts', 98]]