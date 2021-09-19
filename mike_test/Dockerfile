# Use alpine 3.14 as our base
FROM alpine:3.14

# install the needed binaries/libs
RUN apk add python3 py3-pip
RUN pip3 install flask

# create the dir and copy the bits to the image
WORKDIR /srv/mike_test
COPY . .

# Expose this on port 8000
EXPOSE 8000
# Tell flask which script to run
ENV FLASK_APP run.py

# run flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "-p", "8000"]