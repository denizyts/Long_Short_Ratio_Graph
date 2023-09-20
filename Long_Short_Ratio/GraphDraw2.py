import matplotlib.pyplot as plt
import LongShortRatio
import OpenInterest
import TopTraderRatio

from matplotlib import style

ratio = LongShortRatio.get_ratio()
timelist_ratio = LongShortRatio.get_timelist()

open_interest = OpenInterest.get_open_interest()

top_trader_ratio = TopTraderRatio.get_ratio()

fig, ax = plt.subplots()


ax.plot(timelist_ratio, ratio, label='Ratio', marker='o')


ax.plot(timelist_ratio, open_interest, label='Open Interest', marker='x')

ax.legend()

plt.show()






