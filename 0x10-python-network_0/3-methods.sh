#!/bin/bash
# prints all allowd http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
