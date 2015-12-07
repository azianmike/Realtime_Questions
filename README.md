Codename RQ (pending name)

The point of this app is to build a way for users to ask and bet people in real time events, like sports!

My thought process on the architecture of this app:
This will be eventually consistent if we want to work with this at scale. At scale, people will be betting/asking/answering questions,
kind of akin to twitter. We need to be handle all the processing and analytics (which we can do in near realtime with Apache Storm).
Right off the bat, we will assume everything is eventual consistency (BASE) and will be using NoSQL databases (for now, Mongo). Our main
bottleneck will be writes, because there can be just as many writes as reads (as people can view questions and stats but also bet/answer on them).
Slight variances but is safe to assume almost 1:1 read/write ratio. Because of this, eventual consistency is key to make the app run smoothly.

Current architecture is using Amazon Elastic Load Balancer (ELB), we'll send the load off to any one of the webserver running this apache/django setup
AND a MongoDB instance. These will all be sharded and hooked up to allow eventual data consistency. The main bottleneck will be disk so we can make do
with lots of small, underpowered servers (but then the fact of transferring data multiple times will be hard to deal with, another problem for another time
as small = cheap!)
