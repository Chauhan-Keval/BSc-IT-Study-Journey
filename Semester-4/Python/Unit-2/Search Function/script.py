import re
s = "GeeksforGeeks: A computer science portal for geeks";
match = re.search("portal", s)
print("Start Index:", match.start())
print("End Index:", match.end())