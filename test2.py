n = int(input())
nums = [int(x) for x in input().split()]

indexes = [index for index,x in enumerate(nums) if x < 0]
pres = [indexes[0]]
pres.extend(indexes[i]-indexes[i-1]-1 for i in range(len(indexes)) if i != 0)
pres.append(len(nums)-1-indexes[-1])

# 黑魔法K种
res = 0
K = len(indexes)-1 if len(indexes)%2 == 0 else len(indexes)
for i in range(1,K+1):
    if i % 2==0:
        continue
    for start in range(len(pres)-i):
        end = start + i
        temp = 1 + pres[start] + pres[end] + pres[start]*pres[end]
        res += temp

print(res)
        
    
    