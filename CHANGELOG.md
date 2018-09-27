# Changelog
## Version 1.0.8
* The app is now powered by [nginx](https://www.nginx.com/) (again) and [uWSGI](http://projects.unbit.it/uwsgi) for better performance
* Rate limiting (maximum of **5 r/s**)
* Simplified easter egg
* Fixed response `Content-Type` header
## Version 1.0.7
* Home page redirect
## Version 1.0.6
* Performance tweaks
* Refactoring code
* Easter egg
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