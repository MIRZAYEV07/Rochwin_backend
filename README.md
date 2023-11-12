   ## Rest API for Rochwin task
Rest Api built with Django Rest Framework. The main functionalities are to save and represent data about product , employee , client, statistcs and individual statistics of every clients and employees , statistics of most active employees who sold most products.


----




Folder Structure Conventions
============================

> Folder structure options and naming conventions for the current project

### A typical top-level directory layout

    .
    ├── .envs                   # Environment veriables
    ├── core                    # Project configuration files
    ├── main                    # Project applicateions directory ('apps'>client|employee|order|product|statistic) 
    ├── docker-compose.yaml     # docker-compose (running in local)
    ├── Dockerfile.yml 
    ├── requirements.txt
    └── README.md


----

## How to use it
`GET` List of products:
```
http://localhost:8000/products/products/
```
Parameters: `page_size` , `type` , `search`

Response: http 200
```json
{
    "page": 1,
    "count": 2,
    "page_size": 2,
    "results": [
        {
           "id": 1,
           "name": "ring", 
           "quantity": 25,
           "price": 300.0
        },
        {
           "id": 2,
           "name": "bell", 
           "quantity": 28,
           "price": 300.0
        }
    ]
}
```
----
`GET` product detail:
```
http://localhost:8000/products/products/<int:pk>/
```
Response: http 200
```json
{
   "id": 1,
   "name": "ring", 
   "quantity": 25,
   "price": 300.0
}
```
Response: http 404
```json
{
    "detail": "Not found."
}
```
----

`GET` List of statistics of employees:
```
http://localhost:8000/statistics/statistics/employees/
```
Payload: `date`

Response: http 200
```json
[
    {
        "employee_id": 1,
        "full_name": "John Doe",
        "number_of_clients": 9,
        "number_of_products": 38,
        "sales_amount": 6000.00
    },
    {
        "employee_id": 2,
        "full_name": "John Wick",
        "number_of_clients": 6,
        "number_of_products": 13,
        "sales_amount": 600.00
    }
]
```
Response: http 400
```json
{
    "success": false,
    "message": " Something went wrong !!"
}
```

---

`GET` Detail of statistic of employee:
```
http://localhost:8000/statistics/statistics/employee/<int:id>/
```

Payload:
```json
{
        "employee_id": 1,
        "full_name": "John Doe",
        "number_of_clients": 9,
        "number_of_products": 38,
        "sales_amount": 6000.00
}
```



Response: http 400
```json
{
    "success": "False",
    "message": " Something went wrong !!"
}
```
---

`GET` Detail of statistic of clients:
```
http://localhost:8000/statistics/statistics/client/<int:id>/
```

Payload:
```json
{
   "client_id": 1,
   "full_name": "John Doe",
   "number_of_purchased_goods": 36,
   "sales_amount": 39454.00
}
```

 














