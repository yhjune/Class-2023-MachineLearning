import pickle
import pandas as pd
import numpy as np

# mon 1
with open('Website-Fingerprinting/data/unmon_df1_continuous.pkl', 'rb') as file:
     unmon_1 = pickle.load(file)

time_seq = 'time_seq'
size_seq = 'size_seq'
cumlative_seq = 'cumlative_seq'
burst_seq = 'burst_seq'

for index, row in unmon_1.iterrows():
     time_seq_list = row[time_seq]
     cumlative_seq_list = row[cumlative_seq]
     burst_seq_list = row[burst_seq]
     
     cumlative_std = np.std(cumlative_seq_list)
     cumlative_mean = np.mean(cumlative_seq_list)
     cumlative_var = np.var(cumlative_seq_list)
     burst_std = np.std(burst_seq_list)
     burst_mean = np.mean(burst_seq_list)
     burst_var = np.var(burst_seq_list)
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
     unmon_1.at[index, 'cumlative_std'] = cumlative_std
     unmon_1.at[index, 'cumlative_mean'] = cumlative_mean
     unmon_1.at[index, 'cumlative_var'] = cumlative_var
     unmon_1.at[index, 'burst_std'] = burst_std
     unmon_1.at[index, 'burst_mean'] = burst_mean
     unmon_1.at[index, 'burst_var'] = burst_var

     unmon_1.at[index, 'duration'] = duration
     unmon_1.at[index, 'duration_per_packet'] = duration_per_packet
     unmon_1.at[index, 'time_mean'] = time_mean
     unmon_1.at[index, 'time_std'] = time_std
     unmon_1.at[index, 'time_var'] = time_var
     unmon_1.at[index, 'size_mean'] = size_mean
     unmon_1.at[index, 'size_std'] = size_std
     unmon_1.at[index, 'size_var'] = size_var

#ununmon_1 2
with open('Website-Fingerprinting/data/unmon_df2_categorical.pkl', 'rb') as file:
     unmon_2 = pickle.load(file)

for index, row in unmon_2.iterrows():
     outgoing_ratio = (row["total_outcome"] / row["packet_num"])
     incoming_ratio = (row["total_income"] / row["packet_num"])
     unmon_2.at[index, 'outgoing_ratio'] = outgoing_ratio
     unmon_2.at[index, 'incoming_ratio'] = incoming_ratio

new_data = pd.DataFrame({
     'label': unmon_1['label'],
     'packet_num': unmon_2['packet_num'],  
     'total_income': unmon_2['total_income'], 
     'total_outcome': unmon_2['total_outcome'], 
     'outgoing_ratio': unmon_2['outgoing_ratio'], 
     'incoming_ratio': unmon_2['incoming_ratio'], 
     'duration': unmon_1['duration'],
     'duration_per_packet': unmon_1['duration_per_packet'],
     'time_mean': unmon_1['time_mean'],
     'time_std': unmon_1['time_std'],
     'time_var': unmon_1['time_var'],
     'size_mean': unmon_1['size_mean'],
     'size_std': unmon_1['size_std'],
     'size_var': unmon_1['size_var'],
     'cumlative_std': unmon_1['cumlative_std'],
     'cumlative_mean': unmon_1['cumlative_mean'],
     'cumlative_var': unmon_1['cumlative_var'],
     'burst_std': unmon_1['burst_std'],
     'burst_mean': unmon_1['burst_mean'],
     'burst_var': unmon_1['burst_var'],
})
print(new_data.head())

new_data.to_pickle('unmon2.pkl')