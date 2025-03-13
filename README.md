# s3-proxy

A fastapi based server to fetch from s3 bucket.
* this way you do not need to expose your bucket on internet if you want to access it's content on-prem.

## Docker run 

```sh
docker run \
    --name s3-proxy \
    -p 8080:80 \
    -e s3_proxy_access_key=XXXX \
    -e s3_proxy_secret_key=XXXX \
    -d ghcr.io/apandey-oss/s3-proxy:latest
```
