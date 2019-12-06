data = {}

data['OH'] = [['Room Size'], ['Staff Service'], ['Breakfast']]
data['OK'] = [['Free Breakfast'], ['Clean Room'], ['Staff Service']]
data['OR'] = [['Clean Bed'], ['Nice Gardens'], ['Breakfast']]
data['PA'] = [['Breakfast'], ['Location'], ['Comfortable Rooms']]
data['RI'] = [['Location'], ['Toilet ?'], ['Breakfast']]
data['SC'] = [['Location'], ['smelly'], ['Comfortable Room']]
data['SD'] = [['Price'], ['Comfortable Room'], ['Furniture']]
data['TN'] = [['Comfortable Room'], ['Coffee'], ['Breakfast']]
data['TX'] = [['Comfortable Room'], ['furnishings'], ['Wifi']]
data['UT'] = [['Staff Service'], ['Breakfast'], ['Location']]
data['VA'] = [['Elevator'], ['Location'], ['Breakfast']]
data['VT'] = [['Restaurants'], ['Comfortable Room'], ['Staff Service']]
data['WA'] = [['Comfortable Room'], ['Staff Service'], ['Location']]
data['WI'] = [['Comfortable Room'], ['Quiet'], ['friendly']]
data['WV'] = [['Staff Service'], ['furniture'], ['Breakfast']]
data['AK'] = [['staff Services'], ['service'], ['Comfortable room']]
data['AL'] = [['staff Services'], ['breakfast'], ['location']]
data['AR'] = [['breakfast'], ['Comfortable room'], ['staff Services']]
data['AZ'] = [['Comfortable room'], ['location'], ['breakfast']]
data['CA'] = [['Comfortable room'], ['service'], ['breakfast']]
data['CO'] = [['Comfortable room'], ['breakfast'], ['service']]
data['CT'] = [['staff Services'], ['price'], ['Comfortable room']]
data['DE'] = [['Comfortable room'], ['staff Services'], ['breakfast']]
data['FL'] = [['Comfortable room'], ['breakfast'], ['service']]
data['GA'] = [['breakfast'], ['Comfortable room'], ['staff Services']]
data['HI'] = [['breakfast'], ['noise'], ['Comfortable room']]
data['IA'] = [['Comfortable room'], ['breakfast'], ['location']]
data['ID'] = [['facilities'], ['breakfast'], ['Comfortable room']]
data['IL'] = [['location'], ['Comfortable room'], ['breakfast']]
data['IN'] = [['breakfast'], ['Comfortable room'], ['service']]
data['KS'] = [['Comfortable room'], ['breakfast'], ['staff Services']]
data['KY'] = [['location'], ['Comfortable room'], ['breakfast']]
data['LA'] = [['breakfast'], ['Comfortable room'], ['staff Services']]
data['MA'] = [['Comfortable room'], ['facilities'], ['breakfast']]
data['MD'] = [['staff Services'], ['Comfortable room'], ['price']]
data['ME'] = [['pool'], ['consistent'], ['staff Service']]
data['MI'] = [['stmosphere'], ['price'], ['clean']]
data['MN'] = [['Comfortable room'], ['staff Service'], ['comfortable']]
data['MS'] = [['feel free'], ['breakfast'], ['Comfortable room']]
data['MO'] = [['staff Service'], ['Comfortable room'], ['quiet']]
data['MT'] = [['service'], ['staff Service'], ['atmosphere']]
data['NE'] = [['furnishings'], ['service'], ['Comfortable room']]
data['ND'] = [['location'], ['pickup service'], ['hotel computer']]
data['NH'] = [['breakfast'], ['Comfortable room'], ['view']]
data['NJ'] = [['clean'], ['breakfast'], ['staff Service']]
data['NM'] = [['breakfast'], ['furnishings'], ['access']]
data['NV'] = [['breakfast'], ['staff Service'], ['furnishings']]
data['NY'] = [['breakfast'], ['Comfortable room'], ['sleep']]
data['OH'] = [['Room Size'], ['availability'], ['Location']]
data['OK'] = [['Comfortable room'], ['long check'], ['staff Service']]
data['OR'] = [['expedia'], ['gardens'], ['pool']]
data['PA'] = [['breakfast'], ['location'], ['view']]

cnt = {}

for i in data:
    for j in data[i]:
        for k in j:
            if k.lower() not in cnt.keys():
                cnt[k.lower()] = 0
            cnt[k.lower()] += 1

print(cnt)