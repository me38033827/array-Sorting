
Web services sharing custom (different) header attributes

1.
Purpose: Return the number of cars parking at the parking lot within a time span.
Input
URL: /park/number?start=[startDate]&end=[endDate]
Method: GET
Headers: None

Output
Headers:
'number' represents the number of cars

Example:
Request: GET /park/number?start=2017-10-1&end=2018-1-1
Response: [number:21] in response headers


2.
Purpose: Return history total park time (hours) of all cars and total parking fee ($) within a time span
Input
URL: /park/income?start=[startDate]&end=[endDate]
Method: GET
Headers: None

Output
Headers:
'totaltime' represents the total park time
'income' represents the total parking fee

Example:
Request: GET /park/income?start=2017-10-1&end=2018-1-1
Response: [income:683; totaltime:439]


3.
Purpose: Return the usage rate of the parking lot within a time span, the formula is Time(minutes)/(number of park spots*24*60)
Input
URL: /park/usage?start=[startDate]&end=[endDate]
Method: GET
Headers: None

Output
Headers:
'usage' represents the usage rate

Example:
Request: GET /park/usage?start=2017-10-1&end=2018-1-1
Response: [usage:0.021]


4.
Purpose: Return the mean park time (minutes/day) for a user within a time span
Input
URL: /park/parktime
Method: GET
Headers: None

Output
Headers:
'meantime' represents the mean park time


Example:
Request: GET /park/parktime
Response: [parktime:124]


Web services sharing data in JSON format

5.
Purpose: Return cars real time coordinations
Input
URL: /park/positions
Method: GET
Headers: None

Output
Cars' coordinations in Json format


Example:
Request: GET /park/positions
Response:
{
   {
      "xCoord":137,
      "carId":"558AKV",
      "yCoord":232,
      "rot":0
   },
   {
      "xCoord":762,
      "carId":"584ARY",
      "yCoord":137,
      "rot":90
   }
}



6.
Purpose: Return real time weather provided by external web service in Json format
Input
URL: /park/weather
Method: GET
Headers:None

Output
Weather information in Json format

Example:
Request: GET /park/weather
Response:
{
   "wind":{
      "speed":4.7
   },
   "coord":{
      "lat":47.17,
      "lon":-122.52
   },
   "visibility":16093,
   "main":{
      "temp_max":64.4,
      "pressure":1024,
      "humidity":48,
      "temp_min":55.99,
      "temp":60.84
   },
   "weather":[
      {
         "main":"Clear",
         "description":"clear sky",
         "icon":"01n",
         "id":800
      }
   ],
   "name":"Tacoma"
}

Web service sharing data in XML format

7.
Purpose: Return the gas prices provided by external web service in xml format
Input
URL: /park/gas
Method: GET
Headers: None

Output
Gas prices in xml format

Example:
Request: GET /park/gas
Response:
<?xml version="1.0" encoding="UTF-8"?>
<gasPrices>
   <prePrice type="str">3.95</prePrice>
   <midPrice type="str">3.85</midPrice>
   <regPrice type="str">3.73</regPrice>
</gasPrices>


Web service using 'DELETE' HTTP method

8.
Purpose: Delete a user from the database, and user's car will be deleted as well
Input
URL: /park/delete
Method: DELETE
Headers:
'password' represents the password of the to be deleted user

Output
status code: 200

Example:
Request: DELETE /park/delete
Response: status code:200

Web service using 'PUT' HTTP method

9.
Purpose: Update the password of a user
Input
URL: /park/change
Method: PUT
Headers:
'oldpassword' represents the old password of a user
'newpassword' represents the new password of a user

Output
status code:200

Example:
Request: PUT /park/change
Response: status code:200



Web services integrating web service from other service providers

API 6
API 7

10.
Purpose: Send an email of history parking records to a user
Input
URL: /park/record
Method: GET
Headers: None

Output
Status code:200


11.
Purpose: Send a SMS of notification to a user for reminding the parking time
Input
URL: /
Method: GET
Headers: None

Output:
A message is sent to a user's phone automatically


Other APIs

12.
Purpose: Return the shortest path to an exit for a car (or a user)
Input
URL: /park/navigation(?user)
Method: GET
Headers: None

Output
Body:
Path of coordinations in the form of list

Example:
Request: GET /park/navigation
Response:
[[522, 297], [602, 297], [682, 297], [762, 297], [842, 297], [983, 232], [996, 65]]



13.
Purpose: Return a shortest path to the recommended park spot for a car
Input
URL: /park/recommend
Method: GET
Headers: None

Output
Body:
Path of coordinations in the form of list

Example:
Request: GET /park/recommend
Response:
[[522, 449]]
