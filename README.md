# open-citibikes-lambda
Quick Python lambda to get the open Citibikes near me via Siri invocation. Source of this data is from Citibike GBFS available here https://citibikenyc.com/system-data. 

I wrote this primarily to get a quick summary of the Citibike dock availability near my area. I'm happy to extend this functionality if anyone is interested, feel free to create a ticket in the repo.

## Request
Send an HTTP GET to `http://open-citibikes-lambda.vercel.app/api`

## Response
Response is `text/plain` and will return the number of open Citibike docks using the hardcoded stations in [api/index.py](https://github.com/andrewwong97/open-citibikes-lambda/blob/main/api/index.py).

Example response:
```
7 Train has 4 open docks
Trader Joes has 10 open docks
4545 Center has 22 open docks
Court Square S has 4 open docks
Court Square N has 4 open docks
```

## Code
The lambda invocation source code is in `api/index.py` and will be run every time a GET request is sent to the endpoint. The  files in `/` root: [get_hardcode_data.py](https://github.com/andrewwong97/open-citibikes-lambda/blob/main/get_hardcode_data.py) returns the closest station information given a lat/long pair, which is what is hardcoded into the lambda invocation. The reasoning for this setup is that the GBFS JSON is pretty big, and the retrieval process requires a linear reading of the data as well as a full sorting of all entries, so we want to minimize invocation runtime overhead as much as possible.
