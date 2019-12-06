from geopy.geocoders import Nominatim

prlist = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA',
          'MA', 'MD', 'ME', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'ND', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR',
          'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'NC']
gps = Nominatim()
for i in prlist:
    location = gps.geocode(i)
    try:
        print('Location[\'' + i + '\']=[' + str(location.latitude) + ',' + str(location.longitude) + ']')
    except Exception as e:
        pass