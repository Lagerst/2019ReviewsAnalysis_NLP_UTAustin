from summa import keywords
import csv
from rake_nltk import Metric, Rake
from textblob import TextBlob

reviews = {}
cnt = {}
doc = open('USout.txt', 'w', encoding='utf-8')

for i in [1]:
    with open('C:/work/USReviews.csv', encoding='UTF-8') as file:
        content = csv.reader(file)
        for row in content:
            if row[18] == '' or len(row[18]) != 2:
                continue
            elif row[18] not in reviews.keys():
                reviews[row[18]] = ''
                cnt[row[18]] = 0
            if cnt[row[18]] >= 3000:
                pass
            cnt[row[18]] += 1
            reviews[row[18]] = reviews[row[18]] + row[14]

print(reviews.keys())

for j in reviews.keys():
    r = Rake(ranking_metric=Metric.WORD_DEGREE,
             max_length=4)  # Uses stopwords for english from NLTK, and all puntuation characters.
    keywords = r.extract_keywords_from_text(reviews[j])
    phrases = r.get_ranked_phrases()  # To get keyword phrases ranked highest to lowest.
    scores = r.get_ranked_phrases_with_scores()  # To get keyword phrases with scores

    # print(len(scores),len(phrases))
    i = 0
    for score in scores:
        if score[0] < 20:
            del phrases[i:-1]
            break
        i += 1
    # print(phrases)

    keywords2 = TextBlob(",".join(phrases))
    print(j + ': ', file=doc)
    print(keywords2.noun_phrases, file=doc)

doc.close()
