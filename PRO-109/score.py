import pandas as pd
import statistics

df = pd.read_csv('test_score.csv')

Math_score = df['math score'].tolist()

Mean = statistics.mean(Math_score)
Median = statistics.median(Math_score)
Mode = statistics.mode(Math_score)
sd = statistics.stdev(Math_score)

sd1start, sd1end = Mean - sd, Mean + sd
sd2start, sd2end = Mean - (2*sd), Mean + (2*sd)
sd3start, sd3end = Mean - (3*sd), Mean + (3*sd)

data_within_sd1 = [ data for data in Math_score if data > sd1start and data < sd1end]
data_within_sd2 = [ data for data in Math_score if data > sd2start and data < sd2end]
data_within_sd3 = [ data for data in Math_score if data > sd3start and data < sd3end]

print('{}% of data lies within 1sd'.format(len(data_within_sd1)*100/len(Math_score)))
print('{}% of data lies within 2sd'.format(len(data_within_sd2)*100/len(Math_score)))
print('{}% of data lies within 3sd'.format(len(data_within_sd3)*100/len(Math_score)))