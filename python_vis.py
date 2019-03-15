'''
plot the amount of consumption in each brand everytime.
plot two lines, each line represents one brand'''
groups = both.groupby('brand')
fig, ax = plt.subplots(figsize=(20,10))
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.order, group.minimum_distance, linestyle='-',marker='o', ms=3, label=name, lw=0.8)
for item in day_interval['order']:
    plt.axvline(x=item, alpha=0.7, color='black',linestyle='--', lw=0.8)
ax.legend()
plt.title('customer A', fontsize=20)
plt.show()


'''
plot the amount of consumption in each brand everytime.
plot two lines, each line represents one brand
indexed by time.'''
import matplotlib.dates as mdates
dataC = C[['timestamp','minimum_distance']]
dataF = F[['timestamp','minimum_distance']]
dataC.set_index('timestamp',inplace=True)  #set date as index
dataF.set_index('timestamp',inplace=True)
#plot data
fig, ax = plt.subplots(figsize=(20,10))
dataC.plot(ax=ax, linestyle='solid', color='navy', marker='o')
dataF.plot(ax=ax, linestyle='solid', color='orange', marker='o')
ax.xaxis.set_major_locator(mdates.DayLocator())
plt.legend(('brand1','brand2'))
plt.title('customer A', fontsize=20)
txt = None


'''
plot basic bar plot
x-axis displays each category'''
import matplotlib.pyplot as plt
%matplotlib inline
ax = df['st_weekday'].value_counts().sort_index().plot(kind='bar',
                                    figsize=(8,4),
                                    title="Sessions happened on different weekdays")
ax.set_xlabel("st_weekday")
ax.set_ylabel("Frequency")



'''
two subplots in one plot
each plot is for one group'''
num_bins = 20
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,4),sharex=True, sharey=True)
ax1, ax2 = axes.flatten()
ax1.hist(eda[eda['label']==0]['last5day_count'], num_bins, normed=1, alpha=0.5, rwidth=0.9, color='red',label='user who did not purchase')
ax2.hist(eda[eda['label']==1]['last5day_count'], num_bins, normed=1, alpha=0.5, rwidth=0.9, color='blue',label='user who purchased')
ax1.legend(loc="upper right")
ax2.legend(loc="upper right")
ax1.set_title('Count of session in last 5 days')
ax2.set_title('Count of session in last 5 days')
ax1.set_xlabel('Counts')
ax2.set_xlabel('Counts')
ax1.set_ylabel('Density')
ax1.set_xlim([0, 80])
ax2.set_xlim([0, 80])
txt = None









