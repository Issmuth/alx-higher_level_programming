#!/bin/bash
# displays body of response with status code 200
curl -s -f $1 -o res && cat res
