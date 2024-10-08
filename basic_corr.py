import pandas as pd




class Data :
    
    def __init__(self) :
        yield_curve_file = [
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (2).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (3).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (4).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (5).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (6).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (7).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (8).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (9).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (10).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (11).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (12).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (13).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (14).csv',
               '/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/yield curve per day/daily-treasury-rates (15).csv',
               ]  

        GDP_2010_to_2024 = pd.read_excel('/Users/coolguy/Desktop/貨幣銀行學資料/貨銀資料分析/GDP.xls')
        self.GDP_2010_to_2024 = Data.match_days(GDP_2010_to_2024)

        self.yield_curve_list = []

        for file in yield_curve_file :
            data_read = pd.read_csv(file)
            self.yield_curve_list.append(data_read)
            
            
        
        
    def get_data(self) :
        five_year_yield_curve = self.split_year_and_merge_GDP('5 YR')
        seven_year_yield_curve = self.split_year_and_merge_GDP('7 YR')
        ten_year_yield_curve = self.split_year_and_merge_GDP('10 YR')
        twenty_year_yield_curve = self.split_year_and_merge_GDP('20 YR')
        thirty_year_yield_curve = self.split_year_and_merge_GDP('30 YR')
    
        five = Data.corr(five_year_yield_curve)
        seven = Data.corr(seven_year_yield_curve)
        ten = Data.corr(ten_year_yield_curve)
        twenty = Data.corr(twenty_year_yield_curve)
        thirty =  Data.corr(thirty_year_yield_curve)
        
        return five,seven,ten,twenty,thirty
        
        
    def match_days(data_frame) :
    
        temp_list = []
        correct_amount_data = []

        data_frame_list = data_frame.values.tolist()

        if len(data_frame) == 196 :
            num = 7
        
        elif len(data_frame) == 56 :
            num = 2
            
            
        for item in data_frame_list :
            
            temp_list.extend(item)
            
            
            if len(temp_list) == num :
                
                data = pd.Series(temp_list)
                
                ########## Ensure that only numeric data is included in the mean calculation
                ########## apply是應用的意思
                ########## pd.to_numeric：將data的元素轉成數字
                ########## errors='coerce'：轉換失敗的換成NaN
                ########## .dropna()：將NaN刪掉
                average = data.apply(pd.to_numeric, errors='coerce').dropna()
                
                correct_amount_data.append(average)
                temp_list.clear()
        
        return correct_amount_data



    def split_year_and_merge_GDP(self,a) :
        yield_curve = []

        for data in self.yield_curve_list :
            condition = data[[a]]
            yield_curve.append(condition)

        yield_curve = pd.concat([data[[a]] for data in self.yield_curve_list], ignore_index= True,axis=0)
        
        self.GDP_2010_to_2024 = pd.Series(self.GDP_2010_to_2024)
        merged_data =  pd.concat([yield_curve, self.GDP_2010_to_2024], axis=1)
    
        return merged_data
        

    def corr(yield_curve) :
        yield_curve_corr = yield_curve.corr()
        print(yield_curve_corr)



data = Data()
data.get_data()
