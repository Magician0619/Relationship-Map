import re

restr = '小妹。小米。小麦。小刚。大红。大绿。AefgB。A。B'
# pattern = re.compile('[\n。].*占地[\n。]*[。]')
# pattern = re.compile('[\n。][^。]*占地[^。]*[。]')
# pattern = re.compile('[^\n。]*占地[^。]*[。]')
w = "小刚"
# pattern = re.compile('[^\n。]*'+w+'[^。]*[\n]')
# pattern = re.compile('[[^。]*[^。]]*'+ w +'[^。]*[。]')
# pattern = re.compile("[^[^。]*[。]]" + "*" + "[^[^。]*[^。]]")
a = '[^。]*[。]' 
b = '[。]*[。]'
c = '(?<=。).*?。'
# pattern = re.compile('[^。]*[^。]*[^。]')
# pattern = re.compile('[^。]*[。]')
pattern = '[^。]+。小刚。[^。]+。'
search = re.findall(pattern,restr)
print(search)

# 结果
# ，占地15万平方米。

