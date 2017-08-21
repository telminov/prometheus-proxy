# prometheus-proxy
[![Build Status](https://travis-ci.org/telminov/prometheus-proxy.svg?branch=master)](https://travis-ci.org/telminov/prometheus-proxy)
# Usage
run server.py and visit http://localhost:9126/?target=`Youresource`  
You can use these params:
 * `target`: The address of your site. This parameter is required (Example: `some.service.org:8000`)
 * `scheme`: The protocol scheme used for requests (default=`http`)
 * `path`: The HTTP resource path on which to fetch metrics from targets (default=`/metrics`)
 * `verify_ssl`: Disable or Enable validation of the server certificate (default=`1`)

You can also send the Authorization header to login to your resource

# Example config Prometheus

```text
- job_name: 'your resource name'
    bearer_token: '{{ settings.bearer_token }}'
    params:
        target: ['your resource']
        verify_ssl: ['0']
        path: ['/your_special_path']  # default: '/metrics'
        scheme: ['https']
    static_configs:
      - targets: ['proxy:9126']
```

# Docker 
build image 
```text
docker build -t telminov/prometheus-proxy
```
or get image
```text
docker pull telminov/prometheus-proxy
```
