## 0. What's my status? #0
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status)
- **Requirements:**
  - You must use the package `urllib`
  - You are not allowed to import any packages other than `urllib`
  - The body of the response must be displayed like the following example (tabulation before `-`)
  - You must use a `with` statement
- **File:** [0-hbtn_status.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/0-hbtn_status.py)

## 1. Response header value #0
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
- **Requirements:**
  - You must use the packages `urllib` and `sys`
  - You are not allowed to import packages other than `urllib` and `sys`
  - The value of this variable is different for each request
  - You don’t need to check arguments passed to the script (number or type)
  - You must use a `with` statement
- **File:** [1-hbtn_header.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/1-hbtn_header.py)

## 2. POST an email #0
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- **Requirements:**
  - The email must be sent in the `email` variable
  - You must use the packages `urllib` and `sys`
  - You are not allowed to import packages other than `urllib` and `sys`
  - You don’t need to check arguments passed to the script (number or type)
  - You must use the with statement
  - Please test your script in the sandbox provided, using the web server running on port 5000
- **File:** [2-post_email.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/2-post_email.py)

## 3. Error code #0
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
- **Requirements:**
  - You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
  - You must use the packages `urllib` and `sys`
  - You are not allowed to import other packages than `urllib` and `sys`
  - You don’t need to check arguments passed to the script (number or type)
  - You must use the with statement
  - Please test your script in the sandbox provided, using the web server running on port 5000
- **File:** [3-error_code.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/3-error_code.py)

## 4. What's my status? #1
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status)
- **Requirements:**
  - You must use the package `requests`
  - You are not allowed to import packages other than `requests`
  - The body of the response must be display like the following example (tabulation before `-`)
- **File:** [4-hbtn_status.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/4-hbtn_status.py)

## 5. Response header value #1
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
- **Requirements:**
  - You must use the packages `requests` and `sys`
  - You are not allowed to import other packages than `requests` and `sys`
  - The value of this variable is different for each request
  - You don’t need to check script arguments (number and type)
- **File:** [5-hbtn_header.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/5-hbtn_header.py)

## 6. POST an email #1
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
- **Requirements:**
  - The email must be sent in the variable `email`
  - You must use the packages `requests` and `sys`
  - You are not allowed to import packages other than `requests` and `sys`
  - You don’t need to error check arguments passed to the script (number or type)
  - Please test your script in the sandbox provided, using the web server running on port 5000
- **File:** [6-post_email.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/6-post_email.py)

## 7. Error code #1
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- **Requirements:**
  - If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
  - You must use the packages `requests` and `sys`
  - You are not allowed to import packages other than `requests` and `sys`
  - You don’t need to check arguments passed to the script (number or type)
  - Please test your script in the sandbox provided, using the web server running on port 5000
- **File:** [7-error_code.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/7-error_code.py)

## 8. Search API
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes in a letter and sends a POST request to [http://0.0.0.0:5000/search_user](http://0.0.0.0:5000/search_user) with the letter as a parameter.
- **Requirements:**
  - The letter must be sent in the variable `q`
  - If no argument is given, set `q=""`
  - If the response body is properly JSON formatted and not empty, display the id and name like this: `[<id>] <name>`
  - Otherwise:
    - Display `Not a valid JSON` if the JSON is invalid
    - Display `No result` if the JSON is empty
  - You must use the package `requests` and `sys`
  - You are not allowed to import packages other than `requests` and `sys`
  - Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.
- **File:** [8-json_api.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/8-json_api.py)

## 9. My GitHub!
- **Mandatory**
- **Score:** 0.0% (Checks completed: 0.0%)
- **Task:** Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
- **Requirements:**
  - You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
  - The first argument will be your username
  - The second argument will be your password (in your case, a personal access token as password)
  - You must use the package `requests` and `sys`
  - You are not allowed to import packages other than `requests` and `sys`
  - You don’t need to check arguments passed to the script (number or type)
- **File:** [10-my_github.py](https://github.com/alx-higher_level_programming/0x11-python-network_1/blob/main/10-my_github.py)

