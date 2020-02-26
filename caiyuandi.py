import os.path


def count_char(fn):
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:  # open打开文件，给返回的结果一个名字叫fh
            total = 0
            words = 0
            for line in fh:
                words = line.split(None)
                """
                split() 通过指定分隔符对字符串进行切片 str.split(str="", num=string.count(str)).
                str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
                num -- 分割次数。默认为 -1, 即分隔所有。分隔 num+1 个子字符串
                """
                print(words)  # 试一下
                total += len(words)  # 总单词数
            return total

count = count_char('C:/Users/thinkpad/Desktop/work2/tmp/SES2020spring/unit2/readme.md')
print(f'The total number of the words is {count}' )