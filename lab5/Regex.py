import re

# 1
def matches(s):
    ma = r"^ab*$"
    if re.match(ma, s):
        return True
    return False

list1 = ["a", "ab", "acc" , "abc", "abbbbbb"]
for str in list1:
    if matches(str):
        print(str)

# 2
def matches1(s):
    ma = r"^ab{2,3}$"
    if re.match(ma, s):  
        return True
    return False

list2 = ["a", "abb", "acc" , "abc", "abbbbbb", "abbb"]
for str in list2:
    if matches1(str):
        print(str)

# 3
def sequence(s):
    seq = r'[a-z]+(_[a-z]+)*'  
    if re.match(seq, s):
        return True
    return False

list3 = "some_example with find_sequence another_example"
words = list3.split()
for mat in words:
    if sequence(mat):
        print(mat)

# 4
def sequence1(s):
    seq1 = r'[A-Z][a-z]*' 
    if re.match(seq1, s):
        return True
    return False

list4 = "Some Example with find Sequence"
words = list4.split()  
for mat in words:
    if sequence1(mat):  
        print(mat)

