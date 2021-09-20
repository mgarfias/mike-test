# Mike's Apple Test

## The App
* mike_test/ contains the flask app, along with the Docker file

### Build/Run via Docker
1. cd to mike_test and run `docker build -t mgarfias/mike-test .`
	1. Note: add `--platform linux/arm64` if you are targeting ARM64 as I did.
2. Run the Docker image: `docker run -p 8000:8000 mgarfias/mike-test`
3. Test it: `curl -v localhost:8000/bytes/20 | base64 -d | wc -c`

### To pull the image from Dockerhub and run it locally
1. `docker pull mgarfias/mike-test`
2. `docker run -p 8000:8000 mgarfias/mike-test`
3. Test: `curl -v localhost:8000/bytes/20 | base64 -d | wc -c`

### Kubernetes
#### Prereqs:
* A working k8s cluster
* a properly configured kubectl
* Docker image built and available locally.

1. Run `kubectl apply -f mike-test.yaml`
2. Wait until `kubectl get pods` shows STATUS as "Running"
3. Test via `curl <k8s external IP>:32000/bytes/25 2>/dev/null| base64 -d | wc -c`

### Just access the running thing without doing anything else:
1. `curl http://home.garfias.org:8000/bytes/20`