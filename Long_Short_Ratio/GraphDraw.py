import matplotlib.pyplot as plt
import LongShortRatio
import OpenInterest

from matplotlib import style

ratio = LongShortRatio.get_ratio()
timelist_ratio = LongShortRatio.get_timelist()

open_interest = OpenInterest.get_open_interest()
timelist_openinterest = OpenInterest.get_timelist()

plt.plot(timelist_openinterest , open_interest )

plt.show()






