# 5602-Mozilla x Group 4
by: Mikhaila Friske, Dianna Radpour, & Abbie Zimmerman-Niefield

## Getting Started
The project consists of 3 html files (index.html, details.html, and scatter.html), a zipped data file (data.zip) and a python file (run.py).

### Prerequisites
To run the python file, you need the following python modules as well as `python3`
```
http.server
socketserver
zipfile
```

### Running the Project
To run the project, you can call the python script using python3
```
python3 run.py
```
if you would like, you may unzip the data.zip and run the files yourself using the following commands

```
unzip data.zip
python3 -m http.server 8000
```
**You must run the project using the csv and json in the data.zip as we have cleaned a lot of the countries and some ascii errors that were in the original csv**

## What are the visualizations
Our project consists of two main visualizations (the world/choropleth map and the ordinal, categorical plot) and a single country detail view (the 6 question stacked bar graphs).

Our first visualization comes in the form of **a chorepleth map**, with the lightest countries being the ones with most respondents, getting darker as the number of responses decreases (essentially, the darker the shade gets the more desolate the data as the gradient legend shows.) If you hover over a countries borders, you will get a tooltip that gives you the country name and the total respondents from that country. Upon clicking on a country on the map (given that there were survey responses from that country), you will be directed to that country’s details page which contains some **stacked bar graphs** that show the percentage of each answer to the survey questions. This was designed to make it easy to view the relative differences in responses and to visualize which answers are most prevalent for each country (e.g. for China you can quickly see that they are most excited about life being made easier through technology and that their biggest concern is a loss of privacy.) 

Moreover, we had a hunch that maybe the more people know about technology, the more fearful they are and that perhaps ignorance (i.e. self-proclaimed luddite status) may equal bliss. We created a **categorical scatterplot** that displays fear and technical savviness, both as ordinal categorical variables, and how they related to one another. The x-axis displays the levels of technical proficiency of respondents, with the values being the answers to the first question from the survey - *"I consider myself:"* The y-axis has the five responses to the third question from Mozilla’s survey *"Thinking about a future in which so much of your world is connected to the internet leaves you feeling:"* It starts from no fear at the bottom, i.e. optimism about the future, to scared senseless. The bigger the bubbles are, the greater the proportion of that particular country’s respondents who gave the particular response pairing (e.g. being an ultra nerd and being scared senseless). Within this chart, we did some additional cleaning of the data--we removed any data point where the answer to one or both of the questions was left blank. Additionally, the position within a categorical pairing is not relavent, as we randomized offset to allow multiple points to be shown. However, because of the Gestalt principle of proximity, we do notice the distinct groups that appear for each paired responses.

Via the tooltip, you can hover over a bubble to see the country and how many people gave that response (as well as the total number of respondents from that country.) Clicking on a bubble will direct you back to the stacked bar charts to see more details about that particular country’s responding patterns. Our chart shows that many respondents hover around the middle on both spectrums (fear and technical savviness), and that ignorance =/= bliss. The average user seems to be wary/on the fence. 

### Wishes that we didn't get to
We really wanted to inspect privacy and data laws in each country as well and prices on different technologies. However, we did not have time to collect that data for the 232 different countries and regions that were in the Mozilla survey data. Our thoughts around using this additional information was to be able to explore some of the biases that most likely exist in this survey data. 

## Design Process
In order to familiarize ourselves with the data, we all took the survey, read the accompanying blog posts, and looked through the csv. We suspected that the phrasing of the survey questions and answers might have produced a geographical differences in the responses. For example, their description of "most technically savvy" involved having built a computer, which feels like a cultural phenomenon. We also thought we might see interesting variation from country to country in the products people used due to price and popularity. We wondered whether this would impact people’s responses to questions. 

This initial conversation made us realize pretty quickly we wanted to build an explorable map. We implemented the map and coded the countries by color according to how many survey respondents we had. It took us several iterations to clean the data with the following changes: (1) Respondent-reported "Country or Region" was an optional field, so if this was blank we used the automatically populated "Country" field (2) Some countries had different names in the survey data, and (3) the survey data did not match the map data exactly. We added a tooltip to the map so when the user mouses over a country, they can see the name of the country and the number of respondents. Though the data might still be a little messy, after what cleaning we did, we were able to better group and read the data from the csv.

Next, we decided clicking on a country would yield visualizations specific to that country’s data. We all sketched potential visualizations at the country level, and then decided to implement the stacked bar graphs to show the details of the 6 single-answer questions. We started by getting one stacked bar graph working (the whole bar representing 100% of the answers), once that was working, we worked on getting all 6 questions/answers to display. While debugging this visualization, we realized that the apostrophes within the original csv were a little wonky, so we did a search and replace on the odd encoding with an apostrophe.

We wanted to add a second overview visualization. Where our map is meant not only to show who was taking the survey, but also to show the Western focus within the data, we wanted a plot to see if our hunches around tech savviness and fear of tech futures were linked. To implement this graph, we started by looking at the **Shakespeare Data** example from class, but we wanted to use categorical data, so we used a `scaleBand()`. We manually ordered the data for the x and y axis to the "0" point is where the respondent has no tech savviness and is not fearful. Then fear increases as you go up the y axis, and tech savviness increases as you move right on the x axis. When we got the plot to render for the first time, we realized that we had overlooked that due to the categorical nature of the variables, there was a lot of overlap of data pairings that rendered the scatterplot to look nearly empty. To fix this, we added a random offset from the "center" point of that pairing. This created the rectangular groups in our plot. Lastly, we wanted to get a sense for how many people answered a way. To avoid the issue of countries with the most respondents having the largest dots, we used proportions (i.e. respondents in country for that pairing/total respondents for the country * 30). Though this works at normalizing the countries with many more respondents, it gives countries with one respondent always a dot of 30px (i.e. 1/1*30).

To link this visualization with the country detail, we again implemented the feature of clicking on a point and going to that country's detail page. Lastly, we included a side navigation on our visualizations to allow someone to easily jump between the two main visualizations or get back after entering the details page.

### Roles of Team Members
**Abbie:** Clean the csv file with Mikhaila so the data matches with the world_countries.json and can be graphed to the geographical data. Wrote the tooltip code that was reused on each of the pages and the mouseover, mouseleave, click event handlers. Wrote the design process in the readme.

**Dianna:** Concept development for geographical visualization, concept development and implemented base for scatter.html. Prototyped visualizations for the bubble chart with Mikhaila. Wrote the descriptions of the visualizations in the readme. 

**Mikhaila:** Collected resources to help use as examples in creating the visualizations. Implemented the base for geographical map visualization and worked with Abbie to clean the csv file so that the world_countries.json matched more of the countries in the Mozilla survey. Prototyping/sketching different visualizations for the 6 questions with radio answers in survey with Abbie. Worked with Dianna to implement the categorical scatterplot (helped reorganize the data and built in some randomized offsets so you could see more of the points). Added a simple navigation bar to move between pages.

## Sources
Here are a list of sources we used as examples and base code to help us make our visualizations. 

- http://bl.ocks.org/micahstubbs/8e15870eb432a21f0bc4d3d527b2d14f
- https://bl.ocks.org/mjfoster83/7c9bdfd714ab2f2e39dd5c09057a55a0
- https://bl.ocks.org/EfratVil/484d0555f6f818ca6eea3de549a21e86
- http://learnjsdata.com/group_data.html
- Shakespearedata.html from class
