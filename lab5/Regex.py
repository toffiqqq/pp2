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

#5
def matches2(s):
    ma = r'a.*b$'
    if re.match(ma, s):
        return True
    return False

list5 = ["a", "aaaacb", "abc"]
for str in list5:
    if matches2(str):
        print(str)

#6
def replace(s):
    rep = r'[ .,]'
    result = re.sub(rep, ":", s)
    return result

list6 = "Some Example with replace all occurrences."
print(replace(list6))

#7
def convert1(s):
    com = s.split('_')
    camelCase = com[0] + ''.join(word.capitalize() for word in com[1:])
    return camelCase

list7 = "example_of_snake_string"
print(convert1(list7))

#8
def splitAtUppercase(s):
    spl = r'[A-Z][^A-Z]*'
    result = re.findall(spl, s)
    return result

list8 = "ThisIsAStringWithUppercaseLetters"
print(splitAtUppercase(list8))

#9
def spaces(s):
    sp = r'[a-z][A-Z]'
    result = re.sub(sp, r'\1 \2', s)
    return result

list9 = "ThisIsAStringWithCapitalLetters"
print(spaces(list9))

#10
def convert2(s):
    con = r'[a-z][A-Z]'
    result = re.sub(con, r'\1_\2', s).lower()
    return result

list10 = "exampleOfCamelString"
print(convert2(list10))