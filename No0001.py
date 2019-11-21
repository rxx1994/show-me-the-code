# -*- coding: utf-8 -*-
import io
import sys
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 改变标准输出的默认编码

# 方法一：直接用内置模块
code_list = random.sample(range(1000,10000),200)

# 先生成一组随机数列
code_list = [random.randint(1000,10000) for i in range(200)]
# 列表去重
code_list = list(set(code_list))
# for 循环的循环对象得可迭代，所以这里不能用for循环
# 当列表的长度小于200时，生成新的随机数并在确定非重之后将其添加至列表
while len(code_list) < 200:
    add_number = random.randint(1000,10000)
    if  add_number not in code_list:
        code_list.append(add_number)
print(code_list)
