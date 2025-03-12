# s3-proxy

A fastapi based server to fetch from s3 bucket.
* this way you do not need to expose your bucket on internet if you want to access it's content on-prem.

## Run development server

```sh
cd ./src
uvicorn app.main:fapp --reload
```

### Docker compose

```yaml
services:
  api:
    build: .
    ports:
    -  8000:80
    restart: always
```