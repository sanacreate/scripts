# 一个生成随机数组的python脚本，给出了正确的排序结果
from random import randint


def generation():
    lenth = 10
    content = [ i*randint(1,100) for i in range(lenth)]
    right_content = sorted(content)
    print(right_content)
    with open("numbers.txt","w") as f:
        f.write(str(content))
    with open("correct_result.txt","w") as f:
        f.write(str(right_content))
    print("随机数组和排序结果已经写入完成")


generation()