Superuser:
    username:admin
    password:admin

testuser:
    username:testuser
    password:testuser

{{ _.baseUrl }} : is the server URL endpoint (http://127.0.0.1:8000/)

POST:
    {{ _.baseUrl }}/auth/token/login/

    Body:
    
        Multipart form with username and password

POST:
    {{ _.baseUrl }}/auth/token/logout/

    Note: Bearer Token required to logout

POST:
    {{ _.baseUrl }}/api-token-auth/
    
    Body:
        Multipart form with username and password

POST:
    {{ _.baseUrl }}/api/menu/

    Body:
        {
		    "Title": "Burgers"
        }

    Note: Bearer Token required

GET:
    {{ _.baseUrl }}/api/menu

    Note: Bearer Token required

POST:
    {{ _.baseUrl }}/api/menu-items/

    Body:
        {
            "MenuID": 3,
            "Title": "cheese burger",
            "Price": 9,
            "Inventory": 35
        }

GET:       
    {{ _.baseUrl }}/api/menu-items

    Note: Bearer Token required

POST:
    {{ _.baseUrl }}/api/booking/
    {
        "Name": "Micheal",
        "No_of_Guests": 5,
        "BookingDate": "2023-08-11T14:30:00Z"
    }

GET:
    {{ _.baseUrl }}/api/booking/
    Note: Bearer Token required 