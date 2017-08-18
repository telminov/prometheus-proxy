# prometheus-proxy
[![Build Status](https://travis-ci.org/telminov/prometheus-proxy.svg?branch=master)](https://travis-ci.org/telminov/prometheus-proxy)
# Usage
run server.py and visit http://localhost:9126/?target=`You resource`  
You can use these params:
 * `target`: The address of your site. This parameter is required (Example: `some.service.org:8000`)
 * `scheme`: The protocol scheme used for requests (default=`http`)
 * `path`: The HTTP resource path on which to fetch metrics from targets (default=`/metrics`)
 * `verify_ssl`: Disable or Enable validation of the server certificate (default=`True`)

You can also send the Authorization header to login to your resource

# Docker 
build image 
```text
docker build -t prometheus-proxy
```
or get image
```text
docker pull telminov/prometheus-proxy
```
