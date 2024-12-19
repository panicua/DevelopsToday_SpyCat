# DevelopsToday_SpyCat

A RESTful API for managing spy cats, missions, and targets. Allows for CRUD operations on cats, missions, and targets, with features such as note-taking, target completion, and mission assignment. Built to simplify the spying work processes of the Spy Cat Agency.

## Technologies Used

- **Python3.11**
- **Django REST Framework**
- **PostgreSQL**
- **Redis**
- **Docker / Docker Compose**

## Documentation
All API endpoints are documented in this Postman collection:
[SpyCats API Collection](postman/SpyCats API.postman_collection.json).
Import the `.json` file into Postman to use the API.

## Installation (Docker, Local):
1. Clone the repository
    ```bash
    git clone https://github.com/panicua/DevelopsToday_SpyCat.git
    ```

2. Create an `.env` file in the root of the project directory. You can use the `.env.example` file as a template. Don't forget to replace the placeholders with your own values:
   ```sh
   cd TT_DevelopsToday_SpyCat
   cp .env.example .env
   ```

3. Build docker image and start containers (**migrations** are already included in docker-compose.yml):
   ```sh
   docker-compose build
   docker-compose up
   ```
   
## Notes
It was not required in the task, but writing tests is always a good practice. However, to save time, tests and custom JWT permissions were not included in the repository.
