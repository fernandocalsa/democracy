docker build -t local/democracy -f Dockerfile .
docker run --rm -p 5000:5000/tcp -p 7473:7473/tcp -p 7474:7474/tcp local/democracy:latest