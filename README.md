# PhoneBank
I have no clue what I'm doing

requires:

* flask
* redis
* phonenumbers


## Examples

Retrieving
```
$ curl -i http://localhost:5000/api/v1.0/numbers/+16048675309
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Sun, 28 Jan 2018 03:32:26 GMT

{
  "Name": "Jenny"
}
```

Setting
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"e164":"+5551234567", "name":"No One"}' http://localhost:5000/api/v1.0/numbers
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Sun, 28 Jan 2018 03:34:23 GMT

{
  "Name": "No One"
}
```

Adding a call:
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"e164":"+16048675309"}' http://localhost:5000/api/v1.0/calls
HTTP/1.0 201 CREATED        
Content-Type: application/json                          
Content-Length: 49          
Server: Werkzeug/0.14.1 Python/3.6.4                    
Date: Sun, 28 Jan 2018 12:40:02 GMT                     

{                           
  "Time Stamp": "2018-01-28 04:40:02.432735"            
}                           
```

Retrieving calls:
```
$ curl -i http://localhost:5000/api/v1.0/calls/+16048675309                               
HTTP/1.0 201 CREATED        
Content-Type: application/json                          
Content-Length: 159         
Server: Werkzeug/0.14.1 Python/3.6.4                    
Date: Sun, 28 Jan 2018 12:40:50 GMT                     

{                           
  "Calls": [                
    "2018-01-28 04:38:52.666644",                       
    "2018-01-28 04:38:55.065851",                       
    "2018-01-28 04:38:56.048959",                       
    "2018-01-28 04:40:02.432735"                        
  ]                         
}                           
```
