## Library with fastApi + mysql

you need docker and docker compose installed in your os
# build

if you use justfile you can simply run `build` command

or if using command line follow steps:

1) run this command in root of project
```bash docker-compose -f "docker-compose.yaml" up -d --build```

it will pull mysql 8.0 and build backend image 

after finishing build if you want to be sure build was successful you can run this command:

```bash docker image ls```

you must see `fastapi-proj_backend` and `mysql` image

| :warning: WARNING     |
|:---------------------:|
| all docker and docker compose commands need root permission if you are'nt a admin user in your os you must add `sudo` before of all commands |

# Run

as same if you use justfile you can simply run `run` command
or if using command line just run this command:

```bash docker-compose -f "docker-compose.yaml" up```

if everything right you will able see documents of api in 

localhost:8000/docs(http://localhost:8000/docs)



# Exploring Saved Data in mysql database

first you must enter the mysql container with container id (for example `aaad82ef8124`)
for getting mysql container id run this command:

```bash docker container ls```

for finding mysql image row:
```bash docker container ls | grep mysql```

get container id and run this command to enter to mysql container

```bash docker exec -it CONTAINER_ID /bin/bash```

in mysql container shell you need to login to your mysql database with this command:

```bash mysql -uroot --p```

and enter password (password is in docker-compose.yaml default is `aTh5ao8oLi9guizu`)

after login to mysql select database `books` with this command:

```bash USE books;```

if you want to see list of all tables run:

```bash SHOW TABLES;```

or if you want to see all records od a specific table run:

```bash SELECT * FROM TABLE_NAME;```

enjoy!


