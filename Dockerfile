FROM alpine

LABEL maintainer.name="rstular"
LABEL maintainer.website="https://rstular.github.io"
LABEL version="1.0.8"
LABEL description "Lopolis API hosted on Nginx + uWSGI + Flask based on Alpine Linux and managed by Supervisord"

# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt

# Install all necessary libraries/dependencies
RUN apk add --no-cache \
    python3 \
    nginx \
    uwsgi \
    uwsgi-python3 \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

# Copy the Nginx global conf
COPY config/nginx.conf /etc/nginx/
# Copy the Flask Nginx site conf
COPY config/flask-site-nginx.conf /etc/nginx/conf.d/
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY config/uwsgi.ini /etc/uwsgi/
# Custom Supervisord config
COPY config/supervisord.conf /etc/supervisord.conf

# Add app
COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord"]
