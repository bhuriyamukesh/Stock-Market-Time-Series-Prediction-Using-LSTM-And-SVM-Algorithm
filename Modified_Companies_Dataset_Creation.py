import pandas as pd

files = ['AAPL','AMZN','MSFT','GOOG','IBM','ORCL','INTC','HPQ','LNVGY','NDAQ']

for file in files:
	file = file+'.CSV'
	xl = pd.read_csv(file)
	date = xl['Date']
	Close = xl['Close']
	AD_Position = Close.copy()
	Change = [0]* len(date)
	Momentum = [0]* len(date)

	dates = [i.split(' ', 1)[0] for i in date]

	reference = dates[0]

	for i in range (1,len(date)):
	    if Close[i] > Close[i-1] :
	        Momentum[i] = "1"
	        Change[i] = (Close[i]-Close[i-1])/Close[i-1]
	    else :
	        Momentum[i] = "0"
	        Change[i] = (Close[i-1] - Close[i]) / Close[i - 1]



	xl = pd.DataFrame({'Date':date, 'Close':Close,'Change':Change,'Momentum':Momentum}) # a represents closing date b represents closing value c represents close change and d represents momentum

	if (file == "AAPL.CSV"):
		xl.to_csv("Apple_Modified.CSV",index=False,header=True)
	if (file == "AMZN.CSV"):
		xl.to_csv("Amazon_Modified.CSV",index=False,header=True)
	if (file == 'GOOG.CSV'):
		xl.to_csv("Google_Modified.CSV",index=False,header=True)
	if (file == 'HPQ.CSV'):
		xl.to_csv("HP_Modified.CSV",index=False,header=True)
	if (file == 'IBM.CSV'):
		xl.to_csv("IBM_Modified.CSV",index=False,header=True)
	if (file == 'ORCL.CSV'):
		xl.to_csv("Oracle_Modified.CSV",index=False,header=True)
	if (file == 'INTC.CSV'):
		xl.to_csv("Intel_Modified.CSV",index=False,header=True)
	if (file == 'LNVGY.CSV'):
		xl.to_csv("Lenovo_Modified.CSV",index=False,header=True)
	if (file == 'MSFT.CSV'):
		xl.to_csv("Microsoft_Modified.CSV",index=False,header=True)
	if (file == 'NDAQ.CSV'):
		xl.to_csv("Nasdaq_Modified.CSV",index=False,header=True)