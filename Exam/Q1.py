

def calcprofit(stockvalues): 
    dobuy=[1]*len(stockvalues) # 1 for buy, 0 for sell
    prof=0
    m=0
    for i in reversed(range(len(stockvalues))):
        ai=stockvalues[i] # shorthand name
        if m<=ai:
            dobuy[i]=0
            m=ai
        prof+=m-ai
    return (prof,dobuy)



def maximumProfit(price):
    saving=0
    maximum=0
    for num in reversed(price):
        if maximum<=num:
            maximum=num
        saving+=maximum-num
    return saving
        
print(maximumProfit([1,2,100]) )

            
    

