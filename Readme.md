#Fullscreen Exercise 2 - Restaurant Reviews

Files:
1. analysis.py - Python script that process the Yelp reviews. ONLY run this if
  you have downloaded the yelp datasets.
2. d3pie.min.js - D3 Javascript Library
3. ratings.html - Displays the restaurant ratings
4. ratings.js - json data after processing the sentiments. In a real world
  scenario, this should be either in the web server or fetch from a database.
5. Readme.txt - This file
6. reviews.txt - Reviews extracted from the yelp datasets. This file was generated
  by "analysis.py" script

NOTE: If you run "analysis.py" script, you must have the yelp dataset and match
the settings in analysis.py to the location in your hard drive.

These are the procedure and steps that I undertook to display a review
of a restaurant that has over 5,000 reviews.

1. Find and download data:
I found a dataset on yelp.com where it contains a huge amount of data
containing business entities, checkins, tips, users and reviews. Download this
file from https://www.yelp.com/dataset_challenge and extract to your local
directory.

2. Finding a business with more than 5,000 reviews.
The file "yelp_academic_dataset_business.json" contains the characteristics
of businesses reviewed by yelp users. It contains the business id, name,
addresses, reviews count and much more.
I only need to loop over the records and find the json record where the
review count > 5,000. Luckily, there was only one restaurant that has this
much reviews. I've written down the business id of this establishment.

With the business id from the previous step, I load and read the file
"yelp_academic_dataset_review.json". The script loops over each line and look
for business id with the business id gathered from step 2.

if the business id is the same, then append the review from the 'text' field
to a python list. Do this until the end of the json file. Then write the data
to "reviews.txt"

3. Sentiment and Analysis of the Reviews.
I used "TextBlob" natural language library (i.e. using NLTK) to process
each line. Each line is process further with sentiment polarity to view the
negativity or positiveness of the line. Each sentiment value is stored into a
different python list storage. There are five storage depending on the values:

excellent:  1.0 to 0.7
good:       0.6 to 0.3
average:    0.2 to -0.2
below avg:  -0.3 to -0.6
poor:       -0.7 to -1.0

The result is then encoded into a json data and exported to a file.

4. Plotting the Result.
I used d3js and d3pie libraries to plot a piechart that displays the ratings
of restaurant "Mon Ami Gabi"

Ferdinand Enario
ftenario@yahoo.com
