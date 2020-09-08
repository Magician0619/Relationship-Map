import re

restr = '\n小妹。小米。小麦。小刚。大红。大绿。'
# pattern = re.compile('[\n。].*占地[\n。]*[。]')
# pattern = re.compile('[\n。][^。]*占地[^。]*[。]')
# pattern = re.compile('[^\n。]*占地[^。]*[。]')
w = "小刚"
pattern = re.compile('[^\n。]*'+w+'[^。]*[\n]')
search = re.findall(pattern,restr)
print(search)
print(str(search))

# 结果
# ，占地15万平方米。

