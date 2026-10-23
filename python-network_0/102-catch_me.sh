#!/bin/bash
# Make a request to an endpoint to get a specific response bypassing restrictions.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
