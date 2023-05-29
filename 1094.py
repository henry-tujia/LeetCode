
class Solution():
    def __init__(self,capacity,trips):
        self.capacity = capacity
        self.trips = trips
        self.stations = [capacity]*(max(x[-1] for x in self.trips)+1)
        self.pres = self.construct_pre_sums()
        for trip in self.trips:
            self.update(*trip)
    
    def construct_pre_sums(self):
        pre = [0]*len(self.stations)
        for i,num in enumerate(self.stations):
            if  i == 0:
                pre[i] = num
                continue
            pre[i] = num - self.stations[i-1]
        return pre
    
    def update(self,num,left,right):
        self.pres[left] -= num
        if right < len(self.stations)-1:
            self.pres[right+1] += num
    def construct_nums(self):
        for i,_ in enumerate(self.stations):
            if i == 0:
                continue
            self.stations[i] = self.stations[i-1] + self.pres[i]

    def get_num(self):
        self.construct_nums()
        return min(self.stations) >= 0

if __name__ == '__main__':
    solu = Solution(5, [[2,1,5],[3,3,7]])

    print(solu.get_num())
    