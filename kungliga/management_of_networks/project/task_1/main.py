import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

data = pd.read_csv("X.csv", delimiter=',')

# 1
runq_sz_mean = data["runq-sz"].mean()
runq_sz_min = data["runq-sz"].min()
runq_sz_max = data["runq-sz"].max()
runq_sz_25th_percentile = data["runq-sz"].quantile(.25)
runq_sz_90th_percentile = data["runq-sz"].quantile(.90)
runq_sz_stddev = data["runq-sz"].std()
print("runq-sz mean: %.2f" % runq_sz_mean)
print("runq-sz min: %.2f" % runq_sz_min)
print("runq-sz max: %.2f" % runq_sz_max)
print("runq-sz 25th_percentile: %.2f" % runq_sz_25th_percentile)
print("runq-sz 90th_percentile: %.2f" % runq_sz_90th_percentile)
print("runq-sz stddev: %.2f" % runq_sz_stddev)

memused_mean = data["%%memused"].mean()
memused_min = data["%%memused"].min()
memused_max = data["%%memused"].max()
memused_25th_percentile = data["%%memused"].quantile(.25)
memused_90th_percentile = data["%%memused"].quantile(.90)
memused_stddev = data["%%memused"].std()
print("memused mean: %.2f" % memused_mean)
print("memused min: %.2f" % memused_min)
print("memused max: %.2f" % memused_max)
print("memused 25th_percentile: %.2f" % memused_25th_percentile)
print("memused 90th_percentile: %.2f" % memused_90th_percentile)
print("memused stddev: %.2f" % memused_stddev)

procs_mean = data["proc/s"].mean()
procs_min = data["proc/s"].min()
procs_max = data["proc/s"].max()
procs_25th_percentile = data["proc/s"].quantile(.25)
procs_90th_percentile = data["proc/s"].quantile(.90)
procs_stddev = data["proc/s"].std()
print("proc/s mean: %.2f" % procs_mean)
print("proc/s min: %.2f" % procs_min)
print("proc/s max: %.2f" % procs_max)
print("proc/s 25th_percentile: %.2f" % procs_25th_percentile)
print("proc/s 90th_percentile: %.2f" % procs_90th_percentile)
print("proc/s stddev: %.2f" % procs_stddev)

cswch_mean = data["cswch/s"].mean()
cswch_min = data["cswch/s"].min()
cswch_max = data["cswch/s"].max()
cswch_25th_percentile = data["cswch/s"].quantile(.25)
cswch_90th_percentile = data["cswch/s"].quantile(.90)
cswch_stddev = data["cswch/s"].std()
print("cswch/s mean: %.2f" % cswch_mean)
print("cswch/s min: %.2f" % cswch_min)
print("cswch/s max: %.2f" % cswch_max)
print("cswch/s 25th_percentile: %.2f" % cswch_25th_percentile)
print("cswch/s 90th_percentile: %.2f" % cswch_90th_percentile)
print("cswch/s stddev: %.2f" % cswch_stddev)

all_user_mean = data["all_%%usr"].mean()
all_user_min = data["all_%%usr"].min()
all_user_max = data["all_%%usr"].max()
all_user_25th_percentile = data["all_%%usr"].quantile(.25)
all_user_90th_percentile = data["all_%%usr"].quantile(.90)
all_user_stddev = data["all_%%usr"].std()
print("all_%%usr mean: %.2f" % all_user_mean)
print("all_%%usr min: %.2f" % all_user_min)
print("all_%%usr max: %.2f" % all_user_max)
print("all_%%usr 25th_percentile: %.2f" % all_user_25th_percentile)
print("all_%%usr 90th_percentile: %.2f" % all_user_90th_percentile)
print("all_%%usr stddev: %.2f" % all_user_stddev)

ldavg1_mean = data["ldavg-1"].mean()
ldavg1_min = data["ldavg-1"].min()
ldavg1_max = data["ldavg-1"].max()
ldavg1_25th_percentile = data["ldavg-1"].quantile(.25)
ldavg1_90th_percentile = data["ldavg-1"].quantile(.90)
ldavg1_stddev = data["ldavg-1"].std()
print("ldavg-1 mean: %.2f" % ldavg1_mean)
print("ldavg-1 min: %.2f" % ldavg1_min)
print("ldavg-1 max: %.2f" % ldavg1_max)
print("ldavg-1 25th_percentile: %.2f" % ldavg1_25th_percentile)
print("ldavg-1 90th_percentile: %.2f" % ldavg1_90th_percentile)
print("ldavg-1 stddev: %.2f" % ldavg1_stddev)

totsck_mean = data["totsck"].mean()
totsck_min = data["totsck"].min()
totsck_max = data["totsck"].max()
totsck_25th_percentile = data["totsck"].quantile(.25)
totsck_90th_percentile = data["totsck"].quantile(.90)
totsck_stddev = data["totsck"].std()
print("totsck mean: %.2f" % totsck_mean)
print("totsck min: %.2f" % totsck_min)
print("totsck max: %.2f" % totsck_max)
print("totsck 25th_percentile: %.2f" % totsck_25th_percentile)
print("totsck 90th_percentile: %.2f" % totsck_90th_percentile)
print("totsck stddev: %.2f" % totsck_stddev)

pgfree_mean = data["pgfree/s"].mean()
pgfree_min = data["pgfree/s"].min()
pgfree_max = data["pgfree/s"].max()
pgfree_25th_percentile = data["pgfree/s"].quantile(.25)
pgfree_90th_percentile = data["pgfree/s"].quantile(.90)
pgfree_stddev = data["pgfree/s"].std()
print("pgfree/s mean: %.2f" % pgfree_mean)
print("pgfree/s min: %.2f" % pgfree_min)
print("pgfree/s max: %.2f" % pgfree_max)
print("pgfree/s 25th_percentile: %.2f" % pgfree_25th_percentile)
print("pgfree/s 90th_percentile: %.2f" % pgfree_90th_percentile)
print("pgfree/s stddev: %.2f" % pgfree_stddev)

plist_mean = data["plist-sz"].mean()
plist_min = data["plist-sz"].min()
plist_max = data["plist-sz"].max()
plist_25th_percentile = data["plist-sz"].quantile(.25)
plist_90th_percentile = data["plist-sz"].quantile(.90)
plist_stddev = data["plist-sz"].std()
print("plist-sz mean: %.2f" % plist_mean)
print("plist-sz min: %.2f" % plist_min)
print("plist-sz max: %.2f" % plist_max)
print("plist-sz 25th_percentile: %.2f" % plist_25th_percentile)
print("plist-sz 90th_percentile: %.2f" % plist_90th_percentile)
print("plist-sz stddev: %.2f" % plist_stddev)

filenr_mean = data["file-nr"].mean()
filenr_min = data["file-nr"].min()
filenr_max = data["file-nr"].max()
filenr_25th_percentile = data["file-nr"].quantile(.25)
filenr_90th_percentile = data["file-nr"].quantile(.90)
filenr_stddev = data["file-nr"].std()
print("file-nr mean: %.2f" % filenr_mean)
print("file-nr min: %.2f" % filenr_min)
print("file-nr max: %.2f" % filenr_max)
print("file-nr 25th_percentile: %.2f" % filenr_25th_percentile)
print("file-nr 90th_percentile: %.2f" % filenr_90th_percentile)
print("file-nr stddev: %.2f" % filenr_stddev)

# 2
# (a)
# The number of observations with CPU utilization (“all %%usr”) smaller than
# 90% and memory utilization (“%%memused”) smaller than 50%;

# I should have used query() but because the column name has %%, it ruins the query()
cpu_less_than_90 = data[data['all_%%usr'] < 90]['all_%%usr'].count()
print("the number of observations with CPU < 90%%: %d" % cpu_less_than_90)

mem_less_than_50 = data[data['%%memused'] < 50]['%%memused'].count()
print("the number of observations with memory usage < 50%%: %d"
      % mem_less_than_50)

# (b)
# The average number of used sockets (“totsck”) for observations with less than
# 60 000 context switches per seconds (“cswch/s”)
nums_socks = data[data['cswch/s'] < 60000]["totsck"].mean()
print("average sockets used for cswch < 60000: %.2f" % nums_socks)

# 3
# (a)
# Time series of memory usage (“%%memused”) and CPU utilization (“all %%usr”),
# both curves in a single plot. Box plot of both features in a single plot.

plt.subplot(2, 1, 1)
plt.plot(data["TimeStamp"], data["%%memused"], label='%%memused')
plt.plot(data["TimeStamp"], data["all_%%usr"], label='all_%%usr')
plt.legend()

# (b)
# Density plots of memory usage (“%%memused”) and CPU utilization (“all %%usr”), 
# Histograms of both these features (choose a bin size of 1%), four plots in all.

plt.subplot(2, 1, 2)
memused_bins = range(int(memused_min), int(math.ceil(memused_max)))
all_usr_bins = range(int(all_user_min), int(math.ceil(all_user_max)))

plt.hist(data["%%memused"], color='g', label='%%memused', bins=memused_bins,
         density=True, stacked=True)

plt.hist(data["all_%%usr"], color='b', label='all_%%usr', bins=all_usr_bins,
         density=True, stacked=True)

density_memused = ((1 / (np.sqrt(2 * np.pi) * memused_stddev)) *
                   np.exp(-0.5 * (1 / memused_stddev * 
                   (memused_bins - memused_mean))**2))

density_all_usr = ((1 / (np.sqrt(2 * np.pi) * all_user_stddev)) *
                   np.exp(-0.5 * (1 / all_user_stddev * 
                   (all_usr_bins - all_user_mean))**2))

plt.plot(memused_bins, density_memused, '--')
plt.plot(all_usr_bins, density_all_usr, '--')

plt.legend()
plt.show()
