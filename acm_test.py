        
        
def get_input():
    string = input()
    nums = [int(x) for x in string.split()]
    return nums


def solve(data):
    res = 0
    for i in range(data[-1]):
        res += data[0]**(0.5**i)
    return round(res,2)

def output(data):
    print(data)

while True:
    try:
        data = get_input()  # 获取输入数据，可以是输入一个数或者字符串，也可以是更复杂的形式
        result = solve(data)  # 用你的算法解题得出需要的答案
        output(result)  # 按题目要求输出结果
    except EOFError:  # 如果try块中发生了EndOfFile错误，就执行break退出循环
        break  # 关于EOFError在下文讲解 作者：__Kn__ https://www.bilibili.com/read/cv15996133 出处：bilibili
