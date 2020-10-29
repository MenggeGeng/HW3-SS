import sys
sys.path.append(r'D:\\pycharm\\New project\\FE595HW3\\merge_files.py')
import merge_files as mf
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#invoke merge_files.py to get the combined txt
combine = mf.merge_files()

#replace all the turning symbols with point
combine1 = combine.replace("\n",". ")

sentences = tokenize.sent_tokenize(combine1)
print(sentences)

#sentiment analysis
sid = SentimentIntensityAnalyzer()
score = []
for sen in sentences:
    print(sen)
    s = sid.polarity_scores(sen)
    score.append(s)
    for k in sorted(s):
        #print(sen)
        print('{0}:{1}'.format(k,s[k]),end='')
    print()


