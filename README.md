# putio-bh
An updated dockerized putio client to use as a blackhole service.

## Usage

Most directory locations are configurable via env variables. Make sure your config.json paths match what you use in your Docker image.

## Configuration

Add your putio OAUTH token in the relevant section of config.json. The only other thing you need to setup is the directories you want to search on putio and their relevant IDs. I've set my sampe up with 1 dir per media type. The script will then scan each of those directories on putio and download anything within them and stash the results in the relevant subdir for the complete dir.

The idea is to use your watch directory as a blackhole with each media type (tv, movies, music) added to relevant subdirectories. Then each media manager can watch the relevant destination directory and pick up the downloads for only that media type and avoid potential collisions with e.g. Sonarr and Radarr trying to read the same path.

## To Do

* I likely should add some more error handling into the script but as a first release this has been pared down as simply as possible.
  * Confirmed that disconnects mid-transfer are not a concern though.
* Improved managing of the incomplete directory if the transfer is iunterrupted
  * If you're downloading big directories (e.g. a whole season or series in 1 directory) then the next connection may not pick up on that directory, especially if other transfers have completed on putio first. This means you can end up with a lot of files in your incomplete directory until everything catches up.
* Generate starter config.json if not found with default values populated.
* Look into better handling of the putio directory ids and possible options to avoid having to hard-code the ids in the config.
