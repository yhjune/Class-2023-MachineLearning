import pickle
import pandas as pd
import numpy as np

# mon 1
with open('Website-Fingerprinting/data/mon_df1_contiuous.pkl', 'rb') as file:
     mon_1 = pickle.load(file)

time_seq = 'time_seq'
size_seq = 'size_seq'
cumlative_seq = 'cumlative_seq'
burst_seq = 'burst_seq'

for index, row in mon_1.iterrows():
     time_seq_list = row[time_seq]
     size_seq_list = row[size_seq]
     
     count = len(time_seq_list)
     duration = max(time_seq_list)
     duration_per_packet = duration / count if count != 0 else 0
     time_mean = np.mean(time_seq_list)
     time_std = np.std(time_seq_list)
     time_var = np.var(time_seq_list)
     size_mean = np.mean(time_seq_list)
     size_std = np.std(time_seq_list)
     size_var = np.var(time_seq_list)
     
     # save new features
     mon_1.at[index, 'duration'] = duration
     mon_1.at[index, 'duration_per_packet'] = duration_per_packet
     mon_1.at[index, 'time_mean'] = time_mean
     mon_1.at[index, 'time_std'] = time_std
     mon_1.at[index, 'time_var'] = time_var
     mon_1.at[index, 'size_mean'] = size_mean
     mon_1.at[index, 'size_std'] = size_std
     mon_1.at[index, 'size_var'] = size_var

#mon 2
with open('Website-Fingerprinting/data/mon_df2_contiuous.pkl', 'rb') as file:
     mon_2 = pickle.load(file)


for index, row in mon_2.iterrows():
     cumlative_seq_list = row[cumlative_seq]
     burst_seq_list = row[burst_seq]
     
     cumlative_std = np.std(cumlative_seq_list)
     cumlative_mean = np.mean(cumlative_seq_list)
     cumlative_var = np.var(cumlative_seq_list)
     burst_std = np.std(burst_seq_list)
     burst_mean = np.mean(burst_seq_list)
     burst_var = np.var(burst_seq_list)

     # save new features
     mon_2.at[index, 'cumlative_std'] = cumlative_std
     mon_2.at[index, 'cumlative_mean'] = cumlative_mean
     mon_2.at[index, 'cumlative_var'] = cumlative_var
     mon_2.at[index, 'burst_std'] = burst_std
     mon_2.at[index, 'burst_mean'] = burst_mean
     mon_2.at[index, 'burst_var'] = burst_var

print('hello')
#mon 3
with open('Website-Fingerprinting/data/mon_df3_categorical.pkl', 'rb') as file:
     mon_3 = pickle.load(file)

for index, row in mon_3.iterrows():
     outgoing_ratio = (row["total_outcome"] / row["packet_num"])
     incoming_ratio = (row["total_income"] / row["packet_num"])
     mon_3.at[index, 'outgoing_ratio'] = outgoing_ratio
     mon_3.at[index, 'incoming_ratio'] = incoming_ratio

new_data = pd.DataFrame({
     'label': mon_1['label'],
     'packet_num': mon_3['packet_num'],  
     'total_income': mon_3['total_income'], 
     'total_outcome': mon_3['total_outcome'], 
     'outgoing_ratio': mon_3['outgoing_ratio'], 
     'incoming_ratio': mon_3['incoming_ratio'], 
     'duration': mon_1['duration'],
     'duration_per_packet': mon_1['duration_per_packet'],
     'time_mean': mon_1['time_mean'],
     'time_std': mon_1['time_std'],
     'time_var': mon_1['time_var'],
     'size_mean': mon_1['size_mean'],
     'size_std': mon_1['size_std'],
     'size_var': mon_1['size_var'],
     'cumlative_std': mon_2['cumlative_std'],
     'cumlative_mean': mon_2['cumlative_mean'],
     'cumlative_var': mon_2['cumlative_var'],
     'burst_std': mon_2['burst_std'],
     'burst_mean': mon_2['burst_mean'],
     'burst_var': mon_2['burst_var'],
     
})

print(new_data.head())
new_data.to_pickle('mon2.pkl')