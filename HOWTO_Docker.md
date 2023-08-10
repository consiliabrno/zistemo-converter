# HowTo install & run

## Login to remote & clone
`ssh ubuntumaster`

`git clone git@github.com:davidConsilia/zistemo_converter.git`

`cd zistemo_converter`

## Build and run

### a. Docker Compose (preferred)

Run the container:

`docker compose up --build -d`

Stop the container:

`docker compose down`

Remove the container:

`docker compose rm`

### b. Docker

Build:

`docker build . -t zistemo-converter`

Run:

`docker run --detach --restart unless-stopped --publish 5000:5000 --name zistemo-converter zistemo-converter`

Stop and remove:

`docker stop zistemo-converter`

`docker rm zistemo-converter`

# General tips

> Container removal is useful when you want to apply new code changes in the container and using the Docker method (b). If you're using Docker Compose, the container is built automatically on each restart, so it's not necessary. Generally, if you're doing anything and Docker complains there is already a container with that name you can remove it to fix this issue.

> The Docker compose file (a) and `docker run` command (b) are set up so that the container automatically restarts on failure or system reboot.

> If you want to update the app, use `git pull` followed by container restart (stop and run), if you're using the (a) method. In (b), you have to stop, remove, rebuild and then run.
