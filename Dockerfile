FROM python:3.13-slim-bookworm
# Debian 12 release (bookworm)

ADD requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt
ADD src /

CMD ["uvicorn", "app.main:fapp", "--host", "0.0.0.0", "--port", "80"]
