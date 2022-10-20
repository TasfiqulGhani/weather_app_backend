


#### Weather App


Django web application that can show the current weather for any city in a JSON API.
User can enter the city name  which he wants to know the current weather.

##### Features:

- Real time current weather info.
- Supports Multi-Language,
	- English
	- German
	- French
- All cities are available.
- Standard JSON API
- Information list,
	 - Requested City Name
	 - Temperature: Min , Max, Current.
	 - Humidity
	 - Pressure
	 - Wind Speed
	 - Wind Direction
	 - Description

##### Technology Used:
- Django
- MongoDB
- Redis
- Swagger
- Asyncio
- Docker


##### Installation:
- Clone the repo from github.

				git clone https://github.com/TasfiqulGhani/future_academy.git


- Run docker.


				sudo docker-compose build
				
				 sudo docker-compose up


- If you want to create super admin to change the cachhing settings run this.


				docker exec -it [container_id] python manage.py createsuperuser
				


##### API Doc:
Follow the link for the API Documentation :

