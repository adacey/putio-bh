# putio-bh
An updated dockerized putio client to use as a blackhole service.

## Usage

Most directory locations are configurable via env variables. Make sure your config.json paths match what you use in your Docker image.

## Configuration

Add your putio OAUTH token in the relevant section of config.json. The only other thing you need to setup is the directories you want to search on putio and their relevant IDs. I've set my sampe up with 1 dir per media type. The script will then scan each of those directories on putio and download anything within them and stash the results in the relevant subdir for the complete dir.

The idea is to use your watch directory as a blackhole with each media type (tv, movies, music) added to relevant subdirectories. Then each media manager can watch the relevant destination directory and pick up the downloads for only that media type and avoid potential collisions with e.g. Sonarr and Radarr trying to read the same path.

## To Do

I likely should add some more error handling into the script but as a first release this has been pared down as simply as possible.
