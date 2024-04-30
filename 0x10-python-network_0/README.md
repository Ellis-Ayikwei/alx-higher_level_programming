
# Question 0: cURL body size
./0-body_size.sh 0.0.0.0:5000

# Question 1: cURL to the end
./1-body.sh 0.0.0.0:5000/route_1

# Question 2: cURL Method
./2-delete.sh 0.0.0.0:5000/route_3

# Question 3: cURL only methods
./3-methods.sh 0.0.0.0:5000/route_4

# Question 4: cURL headers
./4-header.sh 0.0.0.0:5000/route_5

# Question 5: cURL POST parameters
./5-post_params.sh 0.0.0.0:5000/route_6

# Question 6: Find a peak
python3 6-peak.py

# Question 7: Only status code
./100-status_code.sh 0.0.0.0:5000
./100-status_code.sh 0.0.0.0:5000/nop

# Question 8: cURL a JSON file
./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
./101-post_json.sh 0.0.0.0:5000/route_json my_json_1
./101-post_json.sh 0.0.0.0:5000/route_json my_json_2

# Question 9: Catch me if you can!
./102-catch_me.sh

