n = int(4)

used = [False]*n
temp_res = []
res = 0

words = ["jing", "dong", "zhuan", "qian"]


def is_corr(words):
    max_temp = len(words[-1])
    for word in words:
        if len(word) > max_temp:
            return False

    return True


def get_res_inner(words):
    global res
    if len(temp_res) == n:
        if is_corr(temp_res):
            print(temp_res)
            res += 1
        return
    for i in range(len(words)):
        if used[i]:
            continue
        used[i] = True
        temp_res.append(words[i])
        get_res_inner(words)
        temp_res.pop()
        used[i] = False


def get_res(n, words):
    if n == 1:
        return 0
    get_res_inner(words)
    return res


print(get_res(n, words))
