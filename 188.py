class Solution():
    def max_profit(self,k,prices):
        has_stock = False
        in_price = 0
        def max_profit_inner():
            pass

        for in_day, price in enumerate(prices):
            has_stock  =True
            in_price = price
            for out_day,out_price in enumerate(price,start=in_day):
                if out_price > in_price:
                    continue
                

            
            pass

        
        pass