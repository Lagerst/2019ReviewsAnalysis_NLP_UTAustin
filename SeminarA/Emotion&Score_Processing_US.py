import folium
import csv
import pandas as pd
from textblob import TextBlob

total_score = {}
cnt = {}
value = []
gre = {}
sub = {}
grevalue = []
subvalue = []
progress = 0
prlist = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA',
          'MA', 'MD', 'ME', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'ND', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR',
          'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'NC']

with open('C:/work/USReviews.csv', encoding='utf-8') as file:
    content = csv.reader(file)
    for row in content:
        progress += 1
        if len(row[13]) != 1 or row[18] not in prlist:
            continue
        if row[18] not in total_score.keys():
            total_score[row[18]] = 0
            cnt[row[18]] = 0
            gre[row[18]] = 0
            sub[row[18]] = 0
        analysis = TextBlob(row[14])
        gre[row[18]] += analysis.polarity
        sub[row[18]] += analysis.subjectivity
        total_score[row[18]] += float(row[13])
        cnt[row[18]] += 1

attr = total_score.keys()

for i in attr:
    value.append(total_score[i] / cnt[i])
    grevalue.append(gre[i] / cnt[i])
    subvalue.append(sub[i] / cnt[i])
score_display_range = [7, 10]

print(total_score)
print(cnt)

doc = open('US_Unemployment_Oct2012.csv', 'w')
print('State,Unemployment', file=doc)
for i in range(0, 50):
    print(list(attr)[i] + ',' + str(subvalue[i]), file=doc)
doc.close()

state_geo = r'USStateMap.json'
state_unemployment = r'US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)
# LetFolium determine the scale

map = folium.Map(location=[48, -102], zoom_start=3)
map.geo_json(geo_path=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='polarity (*/1)')
map.create_map(path='us_states.html')
