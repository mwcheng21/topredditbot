# Daily Reddit Post Bot
Hackathon submission, see it here [https://devpost.com/software/daily-reddit-post-bot](https://devpost.com/software/daily-reddit-post-bot)

## Inspiration
Down the rabbit hole of youtube shorts I found myself scrolling through video after video of random movie facts. I soon found out there are a plethora of creators on this side of youtube, creating useless, random movie facts that I did not need to know. Thus was born DRP (Daily Reddit Post), the daily reddit post bot that no one needs.

## What it does
DRP maintains a database of users who want to subscribe to a subreddit. This can be the 3 suggested ones (Movie Details, Today I learned, or Jokes) or a custom subreddit. Once a day, DRP will get the top daily subreddit post at that time, and text it to you.

## How we built it
We let users subscribe through a flask website that is connected to a sqlite database. Every hour, a separate thread runs that gets the users in the database who are subscribed for that time. It then accesses the reddit api to get the top post, and texts it to them using twilio.

## Challenges we ran into
- Running a script hourly to send texts

## What we learned
- twilio
- reddit api
- python threading

## What's next for Daily Reddit Post Bot
- More customization (top n posts, more filters, tags, etc)

#Demo Video
[https://youtu.be/I2-zK4M14RA](https://youtu.be/I2-zK4M14RA)
