# Changelog
## Version 1.0.5
* Docker now using [Alpine Linux](https://alpinelinux.org/) image, which is *much* smaller than [Debian](https://www.debian.org/) image
* Docker is now also using *gunicorn* web server (instead of *NGINX*)
## Version 1.0.4
* Documentation links changed
## Version 1.0.3
* Added `/` endpoint (for browser users), which redirects to [documentation](https://rstular.github.io/lopolis.html)
* Dockerfile performance fix
## Version 1.0.2
* Setting checkouts (via `/setcheckouts` endpoint)
* Updated tests
## Version 1.0.1
* Getting checkouts (via `/getcheckouts` endpoint)
* Introduced changelog
## Version 1.0.0
* Getting & setting menus
* Getting access token