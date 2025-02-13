
#%% [markdown]
# # HW OOP
# ## By: Jonas Agyekum Mintah
# ### Date: 2/12/2025


# %%
import os
#%%


#  ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######  
               
#%%
class Stock:
    """
    Stock class for a publicly traded stock on a major market.
    """

    def __init__(self, symbol, name, firstdate, lastdate, init_filepath):
        self.symbol = symbol.upper()
        self.name = name
        self.firstdate = firstdate
        self.lastdate = lastdate
        self.price_eod = []
        self.volumes = []
        self.dates = []
        self.delta1 = []
        self.delta2 = []

        self.import_history(init_filepath)
        self.compute_delta1_list()  
        self.compute_delta2_list()  

    def import_history(self, filepath):
        """
        Import stock history from CSV file with columns: date, eod_price, volume.
        Stores data into self.dates, self.price_eod, and self.volumes.
        """
        with open(filepath, 'r') as fh:  
            next(fh)  # Skip header row
            for aline in fh.readlines():  
                tmp = aline.strip().split(',')  
                date = tmp[0].strip()
                eod_price = float(tmp[1])  
                volume = int(tmp[2]) 
                self.dates.append(date)
                self.price_eod.append(eod_price)
                self.volumes.append(volume)

        print(f"Successfully imported {len(self.dates)} records from {filepath}")  

    def compute_delta1_list(self):
        """ Compute first derivative: daily stock price change. """
        if len(self.price_eod) < 2:
            self.delta1 = []
            return
        self.delta1 = [self.price_eod[i] - self.price_eod[i + 1] for i in range(len(self.price_eod) - 1)]
        print(f"Computed delta1 list (first 5 changes): {self.delta1[:5]}")

    def compute_delta2_list(self):
        """ Compute second derivative: rate of change of stock price change. """
        if len(self.delta1) < 2:
            self.delta2 = []
            return
        self.delta2 = [self.delta1[i] - self.delta1[i + 1] for i in range(len(self.delta1) - 1)]
        print(f"Computed delta2 list (first 5 changes): {self.delta2[:5]}")
#%%

 #  ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ###### 




 #  ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######  

#%% 
def compute_delta1_list(self):
        """ Compute first derivative: daily stock price change. """
        if len(self.price_eod) < 2:
            self.delta1 = []
            return
        self.delta1 = [self.price_eod[i] - self.price_eod[i + 1] for i in range(len(self.price_eod) - 1)]
        print(f"Computed delta1 list (first 5 changes): {self.delta1[:5]}")

def compute_delta2_list(self):
        """ Compute second derivative: rate of change of stock price change. """
        if len(self.delta1) < 2:
            self.delta2 = []
            return
        self.delta2 = [self.delta1[i] - self.delta1[i + 1] for i in range(len(self.delta1) - 1)]
        print(f"Computed delta2 list (first 5 changes): {self.delta2[:5]}")
#%%

 #  ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######



  ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######  
#%%
def insert_newday(self, newdate, newprice, newvolume):
    """
    Add a new data point at the beginning of lists.
    """
  
    self.dates.insert(0, newdate)
    self.price_eod.insert(0, newprice)
    self.volumes.insert(0, newvolume)

   
    if len(self.price_eod) > 1:
        new_delta1 = self.price_eod[0] - self.price_eod[1]
    else:
        new_delta1 = 0 

    self.delta1.insert(0, new_delta1)

    if len(self.delta1) > 1:
        new_delta2 = self.delta1[0] - self.delta1[1]
    else:
        new_delta2 = 0 

    self.delta2.insert(0, new_delta2)
    print(f"New data inserted: {newdate}, Price: {newprice}, Volume: {newvolume}")
    print(f"New delta1: {new_delta1}, New delta2: {new_delta2}")
    return self   
#%%
 
#  ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  



######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######  
#%%
def nday_change_percent(self, n):
        """
        Calculate the percentage change in stock price over the last n days.
        """
        if len(self.price_eod) < n + 1:
            print(f"Not enough data to calculate {n}-day change for {self.symbol}")
            return None 

        latest_price = self.price_eod[0]  
        old_price = self.price_eod[n]  

    
        change = latest_price - old_price
        percent = (change / old_price) * 100

        print(f"{self.symbol}: {n}-day percent change: {percent:.2f}%")
        return percent
#%%
#  ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  


######   QUESTION 5    ######   QUESTION 5   ######   QUESTION 5    ######   QUESTION 5    ######  
#%%
import os

filepath_aapl = os.path.join(os.getcwd(), 'AAPL_daily.csv')
filepath_msft = os.path.join(os.getcwd(), 'MSFT_daily.csv')
filepath_goog = os.path.join(os.getcwd(), 'GOOG_daily.csv')

aapl = Stock('AAPL', 'Apple Inc', '9/12/14', '9/12/19', filepath_aapl)
msft = Stock('MSFT', 'Microsoft Inc', '9/12/14', '9/12/19', filepath_msft)
goog = Stock('GOOG', 'Alphabet Inc', '9/12/14', '9/12/19', filepath_goog)
#%%
  
#  ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######  


 
#  ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######
#%%  
days_list = [50, 200, 600]
for days in days_list:
    print(f"\nStock performance over the last {days} days:\n")

    aapl_change = aapl.nday_change_percent(days)
    msft_change = msft.nday_change_percent(days)
    goog_change = goog.nday_change_percent(days)

    best_stock = max(aapl_change, msft_change, goog_change)
    best_performer = "AAPL" if best_stock == aapl_change else "MSFT" if best_stock == msft_change else "GOOG"

    print(f"Best performing stock in the last {days} days: {best_performer} with {best_stock}% change\n")
 
# %%


#  ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######  
#%%
aapl.insert_newday('9/13/19', 231.85, 32571922)

# Print results to verify
print('New dates:', aapl.dates[:5])  
print('New price_eod:', aapl.price_eod[:5])  
print('New volumes:', aapl.volumes[:5])  
print('New delta1:', aapl.delta1[:5])  
print('New delta2:', aapl.delta2[:5])  
print('Last two days change:', aapl.nday_change_percent(2))
#%%

#  ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  
