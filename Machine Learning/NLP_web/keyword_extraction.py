from jieba.analyse import extract_tags

text = """
股票00700走势如何
"""

print("keywords by textrank:")

keywords = extract_tags(text,allowPOS=["ns", "n", "vn", "v", "nr"])
print(keywords[:10])