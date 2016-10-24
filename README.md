# Highchat

## Overview
Highchat is a web service that takes requests with plain text containing urls and returns json with urls' titles. Highchat handles ~1000 concurrent requests.

## Benchmark
Testing machine configuration: Intel Core i5-5200U CPU 2.20GHz × 4, 8 GB 1600 MHz DDR3

Test execution time (1000 connections, 1 link per connection) : ~50s

## Installation
```
git clone https://github.com/dmitry-yakutkin/highchat
cd highchat
docker-compose up
```

By default, application is available locally on port :9000.

## API
Request:
```
POST /analyze
"Olympics are starting soon; http://www.nbcolympics.com. See more at https://www.olympic.org"
```

Response:
```
{
  "links": [
    {
      "url": "http://www.nbcolympics.com",
      "title": "2016 Rio Olympic Games | NBC Olympics"
    },
    {
      "url": "https://www.olympic.org",
      "title": "Olympics | Rio 2016 Schedule, Medals, Results &amp; News"
    }
  ]
}
```

## Testing
Tests execution is done with Tornado's testing framework:
```
docker exec -it highchat_tornado_1 python -m tornado.testing highchat.tests
```
