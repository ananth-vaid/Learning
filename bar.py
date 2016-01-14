import re
print(sum([int(list_val) for list_val in (re.findall('[0-9]+',open(input("Enter file ")).read()))]))



