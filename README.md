<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/artus15/Aspen-Project">
<!--     <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Welcome to War Battle !</h3>

  <p align="center">
    A very basic, nonetheless awesome, Django - Heroku - Docker project !
    <br />
    <a href="https://github.com/artus15/Aspen-Project/wiki/War-Statistics"><strong>Explore the war battle statistics</strong></a>
    <br />
    <a href="https://github.com/artus15/Aspen-Project/issues">Report Bug</a>
    <br />
    <a href="https://github.com/artus15/Aspen-Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#run-the-app">Run the app</a></li>
    <li><a href="#different-api-calls">Different API calls</a></li>
    <li><a href="#run-the-tests">Run the Tests</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project is mainly built in python-Django linked to a postgresSQL database-Heroku, and can be run as a container using Docker. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Django][DjangoB]][Django]
* [![Heroku][HerokuB]][Heroku]
* [![Docker][DockerVM]][Docker]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

  - have Python installed ([Follow this](https://www.python.org/downloads/))
  - have Docker installed, if you want to run the application as a container ([Follow this](https://docs.docker.com/get-docker/))
 
### Installation

1. Create a Python virtual environment:
  ```sh
  python -m venv ./venv --prompt NAME_VENV
  ```
2. Activate the new virtual environment (this works on MacOS and Linux):
  ```sh
  source venv/bin/activate
  ``` 
  
  On Windows, using gitbash:
  ```sh
  source venv/Scripts/activate
  ``` 
  
3. Install backend dependencies to the virtual environment (this may take a few minutes):
  ```sh
  python -m pip install -r backend/requirements.txt 
  ```
  > Note: Make sure that the name of the virtual environment is in the ```.gitignore``` to avoid pushing package binaries to the repository. Common names such as .env, .venv, env, venv are already included by default.
4. Source the database URL (this works on MacOS, Linux, and gitbash terminal in Windows):
 ```sh
 source backend/image.env 
 ```
 
 The server will run on your localhost at port 8000.
 
 http://127.0.0.1:8000 will give you access to a basic html page where you can get the lifetime number of wins of the different players available.
 
 You can also play a game of War by entering the name of the two players, an alert will pop up with the name of the winner and it's lifetime number of wins.
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
## Run the app

  1. cd into the backend folder:
  ```sh
  cd backend 
  ```
  2. run the backend:
  ```sh
  python manage.py runserver
  ```

## Different API calls

The calls can be made using any API platform. I can recommend using [Postman](https://www.postman.com/downloads/).

 ```sh
  http://127.0.0.1:8000/players/ 
  ```
  > This is a GET method which returns all the players stored in the database
  
   ```sh
  http://127.0.0.1:8000/updatePlayer/ID/
  ```
  > This is a PATCH method which returns the updated player. To update the info of a player, you need to pass, as a JSON object, a 'name', a 'password' and a number of 'wins'. Don't forget to mention the ID of the player you want to update.
  
  ```sh
  http://127.0.0.1:8000/createPlayer/
  ```
  > This is a POST method which returns the created player. To create the player, you need to pass, as a JSON object, a 'name', a 'password' and a number of 'wins' (usually 0). 
  
  ```sh
  http://127.0.0.1:8000/playWar/
  ```
  > This is a PATCH method which makes two players play War and returns the name of the winner and his lifetime wins. To play War, you need to pass, as a JSON object, the name of the first player as 'name1', and the name of the second player as 'name2'.
  
  ```sh
  http://127.0.0.1:8000/deletePlayer/ID/
  ```
  > This is a DELETE method which deletes the player with ID from the database. Don't forget to include the ID of the player you want to delete.

## Run the Tests

### Unit tests for War rules (The server doesn't need to be running for the unit tests):

from root folder

 ```sh
 cd test
 ```

 ```sh
 python NAME_test.py
 ```
 > Note: You can also use the testing functionality in your favorite IDE.

 
### Acceptance tests for API calls (The server needs to be running for the acceptance tests):

from root folder

```sh
cd backend/testBackend
```
```sh
python -m robot PlayerTests.robot
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Run the server as a docker container

from root folder (you need to have docker installed)

 ```sh
 cd backend
 ```

 ```sh
 docker-compose up
 ```
 > Note: The image will be built.TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/artus15/Aspen-Project.svg?style=for-the-badge
[contributors-url]: https://github.com/artus15/Aspen-Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/artus15/Aspen-Project.svg?style=for-the-badge
[forks-url]: https://github.com/artus15/Aspen-Project/network/members
[stars-shield]: https://img.shields.io/github/stars/artus15/Aspen-Project.svg?style=for-the-badge
[stars-url]: https://github.com/artus15/Aspen-Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/artus15/Aspen-Project.svg?style=for-the-badge
[issues-url]: https://github.com/artus15/Aspen-Project/issues
[license-shield]: https://img.shields.io/github/license/artus15/Aspen-Project.svg?style=for-the-badge
[license-url]: https://github.com/artus15/Aspen-Project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[DjangoB]: https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=django&logoColor=white
[Django]: https://www.djangoproject.com/
[DockerVM]: https://img.shields.io/badge/Docker-0047AB?style=for-the-badge&logo=docker&logoColor=61DAFB
[Docker]: https://www.docker.com/
[HerokuB]: https://img.shields.io/badge/Heroku-8A2BE2?style=for-the-badge&logo=heroku&logoColor=61DAFB
[Heroku]: https://www.heroku.com/
