# https://blog.csdn.net/qq_35332332/article/details/123881359
# https://blog.csdn.net/Ampare1987/article/details/127306294

def number_C2E(ChineseNumber):
    """中文数字转整形"""
    map = dict(〇=0, 零=0, 一=1, 二=2, 三=3, 四=4, 五=5, 六=6, 七=7, 八=8, 九=9, 十=10)
    bit_map = dict(十=10, 百=100, 千=1000, 万=10000)
    size = len(ChineseNumber)
    if size == 0: return 0
    if size < 2:
        return map[ChineseNumber]

    ans = 0
    continue_flag = False  # 连续进两个的标志位
    for i in range(size):
        if continue_flag:
            continue_flag = False
            continue

        if i + 1 < size:
            if ChineseNumber[i + 1] in bit_map.keys():
                ans += map[ChineseNumber[i]] * bit_map[ChineseNumber[i + 1]]
                continue_flag = True
                continue
        ans += map[ChineseNumber[i]]
    return ans
print(number_C2E('九万零一百零一'))



import re
import Number_C2E
import os
# 请自行输入路径
# path = r'xxxxxxxxxxxxx'
path = r'./'


def chinese_name_to_number_name(txt):
    # \u8bfe是UNICODE码“课”
    # \u7ae0是UNICODE码“章”
    x = re.search("\u7ae0", txt)
    d = x.start()
    chinese = txt[1:d]
    number = Number_C2E.number_c2e(chinese)
    end = txt[d:]
    # new_txt = "第" + str(number) + end
    new_txt = "赘婿" + str(number) + end
    return new_txt


# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
print("fileList: ", fileList)
for name in fileList:
    OldName = path + os.sep + name
    NewName = path + os.sep + chinese_name_to_number_name(name)
    os.rename(OldName, NewName)  # 用os模块中的rename方法对文件改名
    print(OldName, '======>', NewName)
