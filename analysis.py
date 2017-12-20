from textblob import TextBlob
import simplejson as json
from simplejson import JSONEncoder

#Declare list storage
debug = 0
data = []
excellent = []
good = []
average = []
below_avg = []
poor = []

# Get the business info from yelp_academic_dataset_business.json
biz = '/Users/ftenario/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json'

# Get the reviews info from yelp_academic_dataset_reviews.json
rev = '/Users/ftenario/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'

#Get all the lines from business.json and append to list
data = []
with open(biz) as f:
    for line in f:
        data.append(json.loads(line))

name = ''
bid = ''
count = ''
city = ''
# Get the business id with review count > 5000
for d in data:
    if d['review_count'] > 5000:
        name = d['name']
        bid = d['business_id']
        count = d['review_count']
        city = d['city']


# Get the reviews from reviews.json and append to list
reviews = []
with open(rev) as f:
    for line in f:
        reviews.append(json.loads(line))

# Open a file for writing
out = open("reviews.txt", 'w')
#Loop thu the reviews and find the business id
for r in reviews:
    # business id of "4bEjOyTaDG24SY5TxsaUNQ":
    if bid == r['business_id']:
            out.write(r['text'].encode('utf-8'))

out.close()

# Read the reviews.txt. Look for non-empty lines
# and append to the data list
f_data = []
with open("reviews.txt") as f:
    for line in f:
        if line != "":
            f_data.append(line)

# Go over the data list
for f in f_data:
    # Run TextBlob opn each line. Decode using utf-8
     d = TextBlob(f.decode("utf-8"))

     # Get the sentiment polarity for each line. -1.0 to 1.0
     # for negativity to positive
     sent = d.sentiment.polarity

     # append each sentiment polarity to a list
     # according to the range value

     # for excellent reviews
     if sent >= 0.7:
         excellent.append('{0:.2f}'.format(float(sent)))

     # For good reviews
     elif sent >= 0.3 and sent <= 0.6:
         good.append('{0:.2f}'.format(float(sent)))

     # For average reviews
     elif sent >= -0.2 and sent <= 0.2:
         average.append('{0:.2f}'.format(float(sent)))

     # for below average reviews
     elif sent <= -0.3 and sent >= -0.6:
         below_avg.append('{0:.2f}'.format(float(sent)))

     # for poor reviews
     elif sent <= -0.7 and sent >= -1.0:
         poor.append('{0:.2f}'.format(float(sent)))
         if debug:
             print(d)
             print("Sentiment Score: " + str(sent))

# Get the total number of lines
total = len(excellent) + len(good) + len(average) + \
    len(below_avg) + len(poor)

ex = '{0:.2f}'.format( (float(len(excellent)) / total ) * 100)
go = '{0:.2f}'.format( (float(len(good)) / total ) * 100)
av = '{0:.2f}'.format( (float(len(average)) / total ) * 100)
be = '{0:.2f}'.format( (float(len(below_avg)) / total ) * 100)
po = '{0:.2f}'.format( (float(len(poor)) / total ) * 100)


if debug:
    print("Total Reviews: " + str(total))
    print("excellent: " + str(len(excellent)) + " = " + str(ex) + "%")
    print("good: " + str(len(good)) + " = " + str(go) + "%")
    print("average: " + str(len(average)) + " = " + str(av) + "%")
    print("below avg: " + str(len(below_avg)) + " = " + str(be) + "%")
    print("poor: " + str(len(poor)) + " = " + str(po) + "%")

jsonData = JSONEncoder().encode({
    "excellent": len(excellent),
    "good": len(good),
    "average": len(average),
    "below average": len(below_avg),
    "poor": len(poor),
    "name": name,
    "city": city
})
jsonData = 'var data = ' + jsonData + ';'

# write the json to ratings.json
f=open("ratings.js", "w")
f.write(jsonData)
f.close()
