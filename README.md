# Website-Fingerprinting
2023-2 Machine Learning project

## Contributors
<table border="1" cellspacing="0" cellpadding="0" width="90%">
    <tr width="100%">
        <td width="15%" align="center"><a href= "https://github.com/yhjune">윤효정</a></td>
        <td width="15%" align="center"><a href= "https://github.com/spig0126">정연희</a></td>
        <td width="15%" align="center"><a href= "https://github.com/geeoneee">김지원</a></td>
        <td width="15%" align="center"><a href= "https://github.com/hehehe9986"></a>이다예</td>
        <td width="15%" align="center"><a href= "https://github.com/emily9949">황수민</a></td>
        <td width="15%" align="center"><a href= "https://github.com/justamoment">안건희</a></td>
    </tr>
    <tr width="100%">
        <td width="15%" align="center"><img src = "https://github.com/yhjune.png"></td>
        <td width="15%" align="center"><img src = "https://github.com/spig0126.png"/></td>
        <td width="15%" align="center"><img src = "https://github.com/geeoneee.png"/></td>
        <td width="15%" align="center"><img src = "https://github.com/hehehe9986.png"></td>
        <td width="15%" align="center"><img src = "https://github.com/emily9949.png"/></td>
        <td width="15%" align="center"><img src = "https://github.com/justamoment.png"/></td>
    </tr>
    <tr width="100%">
        <td width="15%" align="center">github, data pre processing </td>
        <td width="15%" align="center">SVM </td>
        <td width="15%" align="center">Gradient Boost</td>
        <td width="15%" align="center">Random Forest</td>
        <td width="15%" align="center">Result and Presentation </td>
        <td width="15%" align="center">Result and Presentation</td>
   </tr>
</table>

## Folder Structure
```os
.
├── data
│   ├── feature_extraction_monitored.py
│   ├── feature_extraction_unmonitored.py
│   ├── mon2.pkl
│   ├── store_mon_standard_pickle.ipynb
│   ├── store_unmon_standard_pickle.ipynb
│   └── unmon2.pkl
├── git_commit.ipynb
├── gradient_boost
│   ├── gradientBoost_closed_multi_class.ipynb
│   ├── gradientBoost_open_binary.ipynb
│   └── gradientBoost_open_multi_class.ipynb
├── random_forest
│   ├── randomForest_closed_multi_class (1).ipynb
│   ├── randomForest_open_binary.ipynb
│   └── randomForest_open_multi_class.ipynb
├── README.md
└── svm
    ├── svm_closed_multi_class.ipynb
    ├── svm_open_binary.ipynb
    └── svm_open_multi_class.ipynb

4 directories, 19 files
```

## HOW TO USE
1. Downlod the project into your Google Drive. Note that the project should be in the `GitHub` folder.
3. Run the models with the file name: `*_closed_multi_class.ipynb`, `*_open_binary.ipynb`, `*_open_multi_class.ipynb`
4. Before running the models, check the file path with the load pickle data(`mon2.pkl` and `unmon2.pkl` in `data`) in the model
   ```python
   with open('/content/drive/MyDrive/GitHub/Website-Fingerprinting/data/mon2.pkl', 'rb') as file:
    df_m= pickle.load(file)
   ```
   The default folder structrue sholud be like this:
   ```
   GitHub
   |--Website-Fingerprinting
   |--|--data
   |--|--gradient_boost
   |--|--svm
   |--|--random_forest
   ├──└── readme.md
    ...
   ```
  5. After chaning the path, Run the code step by step from the top.
  7. Get 9 Results as below
    
### Sample Result : randomFroest_open_multi_class.ipynb
1. Checking the file path with the load pickle data
<img width="800" alt="image" src="https://github.com/yhjune/Website-Fingerprinting/assets/77730511/7bf9d473-74b0-4506-bc8c-bd6586fe7e8a">

2. Get Result
<img width="354" alt="image" src="https://github.com/yhjune/Website-Fingerprinting/assets/77730511/b33c6792-f3e6-41cf-ac47-0c22a319ee7c">

## Model Background
In monitored data, all the samples are classified with (0~49), but the unmonitored samples are labeled with -1. 

|case|classification|Devide train & test set|
|-|-|-|
|Closed Multi Class|classifiyed the multi claesses|in the monitored data|
|Open Binary|classifiyed the Binary|set all the labels `1` in monitored data <br>in the monitored&unmonitored data|
|Open Multi Class |classifiyed the multi claesses|in the monitored&unmonitored data|

## Data Pipe Line
you can run the model using the datas in `data`, but here's some more detailed pipe line from the origianl datas in case you need to modify them.

**Order : original data -> `store_*_pickle.ipynb` -> `feature_extraction_*.py` -> result data**

1. using the original data and makes the dataframes into pickle files:
  - `unmon_df1.pkl`, `unmon2_df.pkl` in `store_unmon_standard_pcikle.ipynb`
  - `mon_df1_contiuous.pkl`, `mon_df2_contiuous.pkl`,`mon_df3_categorical` in `store_mon_standard_pcikle.ipynb`
  - DO NOT RUN the functions that creates a data frame at once: RUNTIME ERROR could be occurs because of the RAM.

2. using the result from `store_*_pickle.ipynb` and make the result data:
  - `mon2.pkl` from feature_extraction_monitored.py
  - `unmon2.pkl` from feature_extraction_unmonitored.py


## Problem Definition
Website Fingerprinting(WF) is a technique that can infer user’s online activities by analyzing patterns of data traffic generated when users browse the web. Since traffic pattern generated by users while browsing have distinct characteristics by users and websites, it is called as ‘Fingerprints’.

In specific, this is achieved by analyzing distinctive features in the packet sizes, timings, or other characteristics unique to different websites and contents, allowing the adversary to build a "fingerprint" or profile of the user's browsing habits. It involves the monitoring of network packets, such as those sent over an encrypted connection like HTTPS, to identify specific websites or web pages a user visits, even if the content itself is encrypted and inaccessible to the eavesdropper. It also collects device setup information, browser and operating system (OS) versions, installed application details, and active plug-ins. Attackers use the machine learning classifier to match websites that users browsed and collected data.
       
By collecting and analyzing these fingerprints, an adversary can infer which websites a user is visiting, potentially compromising their privacy. To avoid WFP, users can use Tor browser so that they can protect themselves against such an online tracking and surveillance, using proxy and onion routing. However, Website fingerprinting (WF) attacks on Tor allow an adversary who can observe the traffic patterns between a victim and the Tor network to predict the website visited by the victim. (Giovanni Cherubin , Rob Jansen, Carmela Troncoso, 2022).

To avoid this kind of severe privacy security concern, there are much research about WFP. Mitigating website fingerprinting attacks is challenging, as it requires techniques to obscure or obfuscate the patterns in network traffic, making it difficult for adversaries to accurately determine the websites a user is visiting. In spite of this situation, researchers and developers have studied about specific classification models and explored various countermeasures, such as traffic padding and the use of Tor to anonymize browsing habits. However, the arms race between privacy-preserving technologies and fingerprinting techniques continues, highlighting the ongoing need for improved privacy protection in the digital age.

From a machine learning perspective, WF is a classification problem: the adversary trains a classifier on a set of sites, extracting network traffic features that are unique to each website. To deploy the attack, the adversary uses the classifier to match traces of a victim to one of those sites. The effectiveness of WF depends heavily on both the classifier algorithm and the set of features used.(Deep Fingerprinting: Undermining Website Fingerprinting Defenses with Deep Learning,2018). 

Therefore, purpose of this project is testing efficient features and machine learning models by experiments, and finding weakness of this kind of things by analyzing experiments so that can attribute defending WFP.

### Original Data Analysis
Data consists of closed-world data(monitored) and open-world data(unmonitored). In the closed-world setting, we assume that users can visit websites that we are interested in. In contrast, in an open-world setting, we should consider not only websites that we are interested in but also the ones that we are not.

The dataset consists of monitored and unmonitored network traffic data with 19000 and 10000 samples respectively. The two both contain information regarding timestamps, direction, and size. The timestamp is the record of the date and time when the network packet was observed or captured. Direction is also crucial in network traffic analysis differentiating incoming and outgoing traffic. Lastly, size refers to the amount of data transmitted in a network packet or communication. In this dataset, the size for all packets is set to 512. However, monitored and unmonitored data differ in the presence of the labels for websites. Only monitored data has the website labels that correspond to each packet’s information.

For the closed-world data, we’ll load the dataset, ensuring it's well-structured and correctly labeled. In the open world data, we’ll load the dataset with labels for both monitored and unmonitored websites, assigning '1' for monitored websites (positive samples) and '-1' for unmonitored websites (negative samples). Next, we’ll perform a data split into training and testing sets, ensuring a balanced distribution of traffic traces for each monitored website. We then proceed to extract relevant features from the network traffic traces. Finally, we’ll choose a machine learning model suitable for multi-class classification.

## Candidate Features
Our most-voted candidate features are the size of the packets and the direction of the packets. These features are of paramount importance in understanding web traffic patterns and are instrumental in the field of website fingerprinting. Further, it is the most widely used feature with Inter-packet timing. (Wang, T., Zhang, (2020). Traffic Sliver: Fighting Website Fingerprinting Attacks with Traffic Splitting, ACM.) The size of packets can help us gauge the volume of data being transmitted, while the direction (incoming or outgoing) of the packets plays a crucial role in distinguishing the user’s requests from the web server’s responses. Also, it can be a good feature to observe because of distinctive traffic patterns by websites and their contents.
  
There are other candidates suggested. The first one is ‘the number of the packets’. In the case of a number of packets, there are many tries such as simply counting the number of packets(Hayes, J., & Danezis, G. (2016). k-fingerprinting: A Robust Scalable Website Fingerprinting Technique. University College London. Presented at USENIX.) They said that it is more efficient because though it is one of the most significant data in traffic analysis, it is not as complex as watching other packet-regarding features. Secondly, 'Total incoming packets' and 'Total outgoing packets' are also suggested. These features offer valuable insights into network traffic patterns when users access different websites. The quantity and size of packets exchanged with a website can reveal unique patterns for each site. By considering both incoming and outgoing traffic, we can capture a more comprehensive view of network behavior.
