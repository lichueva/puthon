import matplotlib.pyplot as plt
import numpy as np

data = {'1991': 120.0,
        '1992': 1286.0,
        '1993': 4809.0,
        '1994': 2419.0,
        '1995': 22.0,
        '1996': 11.0,
        '1997': 10.0,
        '1998': 13.0,
        '1999': 12.0,
        '2000': 6.0,
        '2001': 5.0,
        '2002': 8.0,
        '2003': 12.0,
        '2004': 12.0,
        '2005': 12.0,
        '2006': 9.0,
        '2007': 9.0,
        '2008': 12.0,
        '2009': 10.0,
        '2010': 10.0,
        '2011': 13.0,
        '2012': 12.0,
        '2013': 12.0,
        '2014': 26.0,
        '2015': 43.0,
        '2016': 12.0,
        '2017': 14.0,
        '2018': 10.0,
        '2019': 5.0}

fig, ax = plt.subplots()
ax.pie(data.values(), radius=4, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, labels=data, labeldistance=None)

ax.set(xlim=(0, 8),
        ylim=(0, 8))

ax.legend(bbox_to_anchor=(1, 1),
            bbox_transform=fig.transFigure)
plt.title("Інфляція в Україні")
plt.show()
