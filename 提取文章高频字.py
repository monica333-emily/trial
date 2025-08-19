from jieba import lcut  
text = """春江潮水连海平，海上明月共潮生。滟滟随波千万里，何处春江无月明！

江流宛转绕芳甸，月照花林皆似霰；    空里流霜不觉飞，汀上白沙看不见。    江天一色无纤尘，皎皎空中孤月轮。

江畔何人初见月？江月何年初照人？    人生代代无穷已，江月年年只相似。   不知江月待何人，但见长江送流水。    白云一片去悠悠，青枫浦上不胜愁。    谁家今夜扁舟子？何处相思明月楼？    可怜楼上月徘徊，应照离人妆镜台。    玉户帘中卷不去，捣衣砧上拂还来。    此时相望不相闻，愿逐月华流照君。    鸿雁长飞光不度，鱼龙潜跃水成文。    昨夜闲潭梦落花，可怜春半不还家。    江水流春去欲尽，江潭落月复西斜。    斜月沉沉藏海雾，碣石潇湘无限路。    不知乘月几人归，落月摇情满江树。
"""

char_dict = {}
words = lcut(text)  

for word in words:
    for char in word:
        if '\u4e00' <= char <= '\u9fff':  
            char_dict[char] = char_dict.get(char, 0) + 1

sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

print("所有字符频率统计:")
for char, count in sorted_chars:
    print(f"{char}: {count}次")

top_3_chars = sorted_chars[:3]  
print("\n最高频的三个字:")
for i, (char, count) in enumerate(top_3_chars, 1):
    print(f"第{i}名: '{char}' 出现 {count} 次")