# An Empirical Study on Managing Energy and Accuracy Requirements of Location Based Android Applications
This research paper was accepted by and presented at the [International Conference on Software Engineering & Knowledge Engineering (SEKE) 2019](http://ksiresearch.org/seke/seke19.html). 
Our research paper is available [here](http://ksiresearch.org/seke/seke19paper/seke19paper_179.pdf).

# Abstract
The improper use of GPS and location-related APIs may result in abnormal battery drain in Android applications. Over the last few years, the developers’ discussions on improving energy efficiency have increased. In this paper, we mine [StackOverflow](https://stackoverflow.com) to analyze and summarize the characteristics of developers’ discussions of managing energy and accuracy-related requirements of location-based Android applications. We extracted 11,911 questions from StackOverflow and filtered 320 relevant questions to answer four research questions. We conducted a manual _thematic analysis_ of relevant questions. Our study shows that the developers are concerned about energy consumption, but are unclear about their preferences as energy and accuracy evolved as conflicting requirements.

# Approach
The data presented in StackOverflow is availble as a data dump at the [StackExchange Data Explorer](https://data.stackexchange.com). We extracted the data by composing and running an [SQL Query](/SQLQuery.rtf). The query includes the keywords _android, location, gps_ used on the _tag_ field of the dataset. The query produced a csv file [Dataset-Query-Results](/Dataset-Query-Results.xlsx) containing 11,911 questions. The dataset contains information about 
_Title, Body, Ac- cepted Answer, Score, Views Count, Favorites Count, Created Date_ and other relevant information. The second step is a [semi-automated method](/Filter.py) to filter the questions that are specific to _energy_ and _accuracy_-related issues of location-based Android applications. During this filtering process, we used keyword matching on the _Body_ field of the questions and obtained a [filtered dataset](/Dataset-Filtered.xlsx) with 651 relevant questions. The questions with neg- ative and zero scores were removed from successful and ordinary categories as they were insignificant to our study. This reduced the dataset to 399 relevant questions. We man- ually read the title and body fields of the questions to verify its relevance to energy and accuracy-related requirements during which 79 false positives were found and removed resulting in 320 questions being considered for thematic analysis.
The popularity of a question, used for answering the preseted research questions, was calculated using a simple [python program](/Popularity.py).

# Contributors
- Marimuthu C (cs15fv08.muthu@nitk.edu.in)
- Sanjana Palisetti (sanjana.palisetti@gmail.com)
- K. Chandrasekaran (kchnitk@ieee.org)
