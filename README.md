#Highchat

## Overview
Web service that takes requests with plain text containing urls and returns json with urls' titles. The service handles 1000 concurrent requests.

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
python -m tornado.testing highchat/tests.py
```