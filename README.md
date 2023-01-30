# open-citibikes-lambda
Quick Python lambda to get the open Citibikes near me via Siri invocation. 

## How to make a request
Send an HTTP GET to `http://open-citibikes-lambda.vercel.app/api`

## Response
Response is `text/plain` and will return the number of open Citibike docks using the hardcoded stations in `api/index.py`.

Example response:
```
7 Train has 4 open docks
Trader Joes has 10 open docks
4545 Center has 22 open docks
Court Square S has 4 open docks
Court Square N has 4 open docks
```
