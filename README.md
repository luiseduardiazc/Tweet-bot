# Bot tweet
## Getting Started 🚀
This bot takes one article every 12 hours from hacker news and make a tweet
### Prerequisites
create into root directory a file named env_file  to sored credentials from twitter
``` 
    CONSUMER_KEY=
    CONSUMER_SECRET=
    ACCESS_TOKEN=
    ACCESS_TOKEN_SECRET=
```
### create image
```
docker build --no-cache . -t tweet-bot
```
### tests
``` 
docker run -it --env-file env_file  tweet-bot
```
### Deployment
#### run in background
``` 
docker run -d -it --env-file env_file  tweet-bot
```
#### list containers
``` 
docker container ls
```
#### containers logs
``` 
docker container logs <id>
```

#### stop containers
``` 
docker container stop <id>
```