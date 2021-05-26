#--- part 1 c--- 

#--- reading data for 1 and c without sql -- Part b and Part d
import time
import json
startTime = time.time()
#inculde tiem for reading the file.
filePath = 'E:/DPU/winter 2020/DSC 460/assignment4/TweetData.txt'
fd = open(filePath, 'r', encoding="utf-8")
lineData = fd.readlines()
print("\n\nReading Data From text file")
listInsert = []
for tweet in lineData:
    try:
        objectt = json.loads(tweet)
        id_string = objectt['id_str']
        if id_string is not None:
            if '777' in id_string or '88' in id_string:
                listInsert.append(objectt)
    except ValueError:
        None

EndTime = time.time()

TotalTime = EndTime - startTime
print("\n\nTotal time for Reading from file for query 1b is "+str(TotalTime))

#--- part 1 d --- 




startTime = time.time()
#inculde tiem for reading the file.
filePath = 'E:/DPU/winter 2020/DSC 460/assignment4/TweetData.txt'
fd = open(filePath, 'r', encoding="utf-8")
lineData = fd.readlines()
print("\nReading Data From text file")

listDistinctInsert = []
for tweet in lineData:
    try:
        objectt = json.loads(tweet)
        inReplyUserId = objectt['in_reply_to_user_id']
        if inReplyUserId is not None:
            if inReplyUserId not in listDistinctInsert:
                listDistinctInsert.append(objectt)
    except ValueError:
        None

EndTime = time.time()

TotalTime = EndTime - startTime
print("\n\nTotal time for Reading from file for query 1D is "+str(TotalTime))

import matplotlib.pyplot as plt
texts = []
names = []


for tweet in lineData:
    try:
        objectt = json.loads(tweet)
        text = objectt['text']
        userName = objectt['user']['name']
        if text is not None and userName is not None:
            texts.append(len(text))
            names.append(len(userName))
    except ValueError:
        None

text_40 = texts[:40]
userName_40 = names[:40]

plt.scatter(text_40,userName_40)
plt.xlabel('Length of 40 texts')
plt.ylabel('Length of 40 user Name')
plt.title('Scatter plot for the length of texts vs user name',color="blue")
plt.show()

fd.close()
fd.close()
