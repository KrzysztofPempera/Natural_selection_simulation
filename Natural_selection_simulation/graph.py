import matplotlib.pyplot as plt
import numpy as np

def plot(wolfCount, rabbitCount, foodCount, id):
    
    x = range(0,len(wolfCount))
    plt.plot(x, foodCount, color = 'orange', label = 'Food count')
    plt.plot(x, rabbitCount, color = 'black', label = 'Rabbit count')
    plt.plot(x, wolfCount, color = 'red', label = 'Wolf count')
    plt.ylabel('Object count')
    plt.xlabel('Turn')
    plt.legend()
    plt.savefig('plots/plot_'+str(id)+'.png')
