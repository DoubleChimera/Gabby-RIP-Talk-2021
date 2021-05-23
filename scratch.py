# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pathlib import Path



# Load Track Length Data
trackLength_input_dir = '.'
trackLength_input_filename = 'Gabby_RIP_Talk_2021_data_tdT_v_ht_trajLengths.csv'
trackLengths = pd.read_csv((Path(trackLength_input_dir) / trackLength_input_filename), sep=',')

# Plot distributions of tdTomato vs Halo Tag (Histogram, Violin Plot, )
fig1  = plt.figure(1)

ax1 = plt.subplot(131)
bins = np.arange(200, 1250, 100)
sb.histplot(trackLengths, x='Length', hue='Tag', bins=bins, stat='count', ax=ax1)

ax2 = plt.subplot(132)
sb.histplot(x=trackLengths.loc[trackLengths['Tag'] == 'tdTomato']['Length'], 
            bins=bins, line_kws={'color':'k'}, stat='density', alpha=0.5,
            color='C0', ax=ax2)
sb.histplot(x=trackLengths.loc[trackLengths['Tag'] == 'Halo']['Length'], 
            bins=bins, line_kws={'color':'k'}, stat='density', alpha=0.5,
            color='C1', ax=ax2)

ax3 = plt.subplot(133)
sb.violinplot(data=trackLengths, x='Tag', y='Length', saturation=0.75)
plt.setp(ax3.collections, alpha=.5)

plt.show()