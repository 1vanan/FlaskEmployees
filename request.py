import requests as requests

# requests.post("http://localhost:5000/employees",
#              json={"FirstName": "John", "SecondName": "Malcovich",
#                    "Experience": "Mid", "Salary": "4500"})

# requests.post("http://localhost:5000/employees",
#              json={"FirstName": "Bill", "SecondName": "Clinton",
#                    "Experience": "Senior", "Salary": "7000"})

# requests.post("http://localhost:5000/employees",
#              json={"FirstName": "Steve", "SecondName": "Buchemi",
#                    "Experience": "Junior", "Salary": "2000"})

requests.delete("http://localhost:5000/employees/1")
