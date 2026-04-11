# Song vibe matcher



### Main Idea

User adds songs, we do analysis using LLM or dedicated ML models on the son underlying theme, subtext and entiment, and gives a Gen AI generated output in two forms- a cover image and a caption.



### Project structure



* A user would select a song, from youtube, or soundcloud, or last.fm or something like this.. 
* It can be an individual/ standalone song, or adding to an incremental indefinite playlist
* the App makes analysis and then creates an AI-generated Playlist cover and an Sentiment based caption or message to the songs. This can be complimented and described as Artist's taste and user's taste



### Application Architecture

* UI should be good interactive based. Techstack should be angular 21.
* Backend should be either of two options- Spring web and spring-boot framework using Java 21 ,OR, Django framework using Python3
* DB- I am not sure how can we add a database here, for storing some app and user data, we can use MongoDB. But not sure how we can add songs data. Some vectorized db.. maybe?
* An OSS GenAI model for image and picture generation.



### Project building

* We can start making the project in small-incremental steps
* Start with a very small, local song based model with text sentiment analysis, then increment to Image generation, then interactive UI and connecting to internet for all songs... This is an outlined idea
* The Idea is, to make some tangible-working application version in every working step



