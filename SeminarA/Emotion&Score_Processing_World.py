import csv
from pyecharts import Map, Page
from textblob import TextBlob

total_score = {}
score2017 = {}
score2016 = {}
score2015 = {}
cnt2017 = {}
cnt2016 = {}
cnt2015 = {}
cnt = {}
value = []
value2017 = []
value2016 = []
value2015 = []
attr2017 = []
attr2016 = []
attr2015 = []
gre = {}
sub = {}
grevalue = []
subvalue = []
progress = 0

with open('C:/work/Hotel_Reviews.csv') as file:
    content = csv.reader(file)
    for row in content:
        progress += 1
        if row[5][1:-1] not in total_score.keys():
            total_score[row[5][1:-1]] = 0
            cnt[row[5][1:-1]] = 0
            score2017[row[5][1:-1]] = 0
            score2016[row[5][1:-1]] = 0
            score2015[row[5][1:-1]] = 0
            cnt2017[row[5][1:-1]] = 0
            cnt2016[row[5][1:-1]] = 0
            cnt2015[row[5][1:-1]] = 0
            gre[row[5][1:-1]] = 0
            sub[row[5][1:-1]] = 0
        analysis = TextBlob(row[6] + '. ' + row[9] + '.')
        gre[row[5][1:-1]] += analysis.polarity
        sub[row[5][1:-1]] += analysis.subjectivity
        total_score[row[5][1:-1]] += float(row[12])
        cnt[row[5][1:-1]] += 1
        if '2017' in row[2]:
            score2017[row[5][1:-1]] += float(row[12])
            cnt2017[row[5][1:-1]] += 1
        elif '2016' in row[2]:
            score2016[row[5][1:-1]] += float(row[12])
            cnt2016[row[5][1:-1]] += 1
        elif '2015' in row[2]:
            score2015[row[5][1:-1]] += float(row[12])
            cnt2015[row[5][1:-1]] += 1
        if progress % 10000 == 0:
            print('Progress : ' + str(2 * progress // 10000) + '%')

attr = total_score.keys()

for i in attr:
    value.append(total_score[i] / cnt[i])
    print(str(i) + ':' + str(total_score[i] / cnt[i]))
    grevalue.append(gre[i] / cnt[i])
    subvalue.append(sub[i] / cnt[i])
    if cnt2017[i] != 0:
        attr2017.append(i)
        value2017.append(score2017[i] / cnt2017[i])
    if cnt2016[i] != 0:
        attr2016.append(i)
        value2016.append(score2016[i] / cnt2016[i])
    if cnt2015[i] != 0:
        attr2015.append(i)
        value2015.append(score2015[i] / cnt2015[i])
score_display_range = [7, 10]

print(total_score)
print(cnt)
print(score2017)
print(cnt2017)
print(score2016)
print(cnt2016)
print(score2015)
print(cnt2015)

page = Page()

map0 = Map("WorldMap", width=1200, height=600)
map0.add("Overall", attr, value, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=score_display_range)
map0.add("Year 2017", attr2017, value2017, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=score_display_range)
map0.add("Year 2016", attr2016, value2016, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=score_display_range)
map0.add("Year 2015", attr2015, value2015, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=score_display_range)
page.add(map0)

map1 = Map("WorldMap", width=1200, height=600)
map1.add("Polarity", attr, grevalue, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=[-0.6, 0.6])
map1.add("Subjectivity", attr, subvalue, type="effectScatter", maptype="world", geo_emphasis_color='#F5D0A9',
         is_visualmap=True, visual_text_color='#000', visual_range=[0, 0.6])
page.add(map1)

page.render(path="./OverallMap.html")
