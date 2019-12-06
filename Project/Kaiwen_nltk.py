import csv
from rake_nltk import Metric, Rake
from textblob import TextBlob

Location = {}
Location['China'] = [36.05, 104.59]
Location['United States'] = [40.858, -96.772]
Location['Russia'] = [65.55, 97.18]
Location['Ireland'] = [52.946, -7.983]
Location['Australia'] = [-23.53, 134.59]
Location['United Kingdom'] = [56.596, -4.175]
Location['New Zealand'] = [-41.1, 172.4]
Location['Belgium'] = [50.633, 4.647]
Location['France'] = [48.0, 4.0]
Location['Italy'] = [42.943, 11.953]
Location['Canada'] = [63.4, -110.4]
Location['Netherlands'] = [52.51, 5.51]
Location['Germany'] = [51.147, 10.386]
Location['Israel'] = [31.524, 34.871]
Location['Switzerland'] = [46.816, 8.236]
Location['Kuwait'] = [29.224, 47.719]
Location['Singapore'] = [1.3114, 103.8222]
Location['Greece'] = [38.393, 24.17]
Location['Romania'] = [45.875, 24.939]
Location['Hong Kong'] = [22.3336, 114.1919]
Location['Romania'] = [45.875, 24.939]
Location['Saudi Arabia'] = [24.886, 44.209]
Location['Sweden'] = [62.67, 16.61]
Location['Turkey'] = [39.3, 34.014]
Location['Spain'] = [39.977, -3.12]
Location['South Africa'] = [-30.52, 24.87]
Location['United Arab Emirates'] = [23.826, 54.404]
Location['India'] = [22.59, 80.6]

doc = open('out.txt', 'w')

keys = Location.keys()
print(keys)

for country in keys:
    count = 0
    reviews = ''
    with open('C:/work/Hotel_Reviews.csv') as file:
        content = csv.reader(file)
        for row in content:
            countrynow = " " + country + " "
            if row[5] == countrynow:  # 国家名前后各有一个空格
                reviews = reviews + row[6] + row[9]
                count += 1
            if count >= 3000:
                break

    r = Rake(ranking_metric=Metric.WORD_DEGREE,
             max_length=4)  # Uses stopwords for english from NLTK, and all puntuation characters.
    keywords = r.extract_keywords_from_text(reviews)
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
    print(country + ': ', file=doc)
    print(keywords2.noun_phrases, file=doc)

doc.close()
