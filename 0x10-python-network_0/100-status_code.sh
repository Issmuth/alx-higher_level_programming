#!/bin/bash
# returns only the status code
curl -o /dev/null -s -w "%{http_code}\n" $1
