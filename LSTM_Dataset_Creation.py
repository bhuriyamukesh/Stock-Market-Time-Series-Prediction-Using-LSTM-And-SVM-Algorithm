import pandas as pd

file1 = "Input_Dataset.CSV"

xl1 = pd.read_csv(file1)
Stock_Price_Volatility = xl1['Stock_Price_Volatility']
Close = xl1['Close']
Change = xl1['Change']
Stock_Momentum = xl1['Stock_Momentum']
Index_Volatility = xl1['Index_Volatility']
Index_Momentum = xl1['Index_Momentum']
Sector_Momentum = xl1['Sector_Momentum']

Moment = [0]* len(Change)


for i in range(len(Change)):
    if(Change[i] == 0): Moment[i] = -1
    else: Moment[i] = 1


xl = pd.DataFrame({'Close':Close,'Index_Momentum':Index_Momentum,'Index_Volatility':Index_Volatility,'Sector_Momentum':Sector_Momentum,'Stock_Momentum':Stock_Momentum,'Stock_Price_Volatility':Stock_Price_Volatility,'Change':Moment}) # a represents closing date b represents closing value c represents close change and d represents momentum
#
xl.to_csv("LSTM_Input.CSV",index=False,header=False)