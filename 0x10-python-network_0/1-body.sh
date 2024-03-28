#!/bin/bash
# displays body of response with status code 200
curl -s -o response.txt -w '%{http_code}' $1 | grep '200' > /dev/null cat response.txt
