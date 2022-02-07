# yaml-extract tool

## About
This tool mimic JSONPath but for YAMLS.

The tool gets as input:
* A valid YAML text
* A filter expression that represents the value to be extracted:

Exmaple:

```yaml
root:
    child1:
        list:
            - element1
            - element2
        listOfdicts:
            - key1: element1
              key2: element2
    child2:
        child2t: "text"
```
* Expression examples

```shell
root.child1.list[0]            ---> "element1"
root.child1.list[1]            ---> "element2"
root.child1.listOfdicts[0].key1 ---> "element1"
```
## Prerequisitess
First, git clone the repo:
```sh
git clone https://github.com/nadivravivz/ohadchallenge.git
``` 

Tools:
* [Python](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/get-docker/) - make sure docker-compose inlucded, if not - install it manually.
* [MiniKube](https://minikube.sigs.k8s.io/docs/start/)

## Implementation options
* [CLI](#cli)
* [Docker](#docker)
* [Web API](#web-api)
* [MiniKube](#minikube)

## CLI
### CLI Help , -h
```sh
usage: yaml-extract.py [-h] -f FILE -e EXPR

Tool that extracts a value from a YAML text based on a path expression

required arguments:
  -f FILE, --file FILE
                        The name of a yaml file.
                        If the file name is `-`, then it is read from stdin
  -e EXPR, --expr EXPR
                        The expression to extract.
                        Please write the expression with double quotes, example: --expr "root.child1.list[0]"
```
### Steps
In order to run the CLI you will need to have Python.

After installing Python, run these commands from the repo folder:
```sh
$ cd CLI
$ pip install -r requirements.txt
```
Next you will have 2 ways to use the CLI tool:

### 1. Using a File
Test files are located in the tests folder.

```
# Example from file
$ python yaml-extract.py -f tests/test.yaml --expr "root.child1.list[0]"
$ element1
```

### 2. Using Standard Input (Stdin)
```
# Example from stdin
$ cat tests/data/test.yaml | yaml-extract -f - --expr "root.child1.list"
$ ["element1", "element2"]
```



## Docker
To use the tool with docker you will first need to build the docker image.

Type these commands to build the image:
```
$ cd docker
$ docker build -t yaml-extract .
```
There are 2 ways to use the tool with docker:
### 1. Using a File with Docker Mount
Test with docker mount
```
# Example docker with mount
# Run the commands from the main folder
# Command exmaple: docker run -v <absolute yaml file path>:/app/test.yaml yaml-extract:latest -f ./test.yaml -e "<your expression>"

$ docker run -v ${PWD}/tests/test.yaml:/app/test.yaml yaml-extract:latest -f ./test.yaml -e "root.child1.list[0]"
$ element1
```

### 2. Using Standard Input (Stdin)
Test with Docker Stdin
```
# Example docker with 
# Command exmaple: cat <yaml files> | docker run -i yaml-extract:latest -f - -e "<your expression>"
# Run the commands from the main folder

$ cd tests
$ cat test.yaml | docker run -i yaml-extract:latest -f - -e "root.child1.list[0]"
$ element1
```

## Web API
The Web API implemented using docker-compose.
Current API's are /health and /api/yaml-extract
To implement the Web Api, follow these lines of code:
```
# Run commands from main folder
$ cd web
$ docker-compose up --build
```
Following this the web server should be running.

### Testing
On your web-browser, navigate to localhost:5123/health / 127.0.0.1:5123/health

If you see the message Health is good then proceed, else the implementation failed.

The yaml-extract API takes Json file with the message structure
```
{
    "text": "<YAML_TEXT>",
    "expr": "<EXPR>"
}
```
and returns
```
{"data": <JSON_RESULT>}
```

* To test the yaml-extract API, follow this:
```
# Run commands from main folder
$ curl http://localhost:5123/api/yaml_extract --data-binary "@./tests/request.json" -H "Content-Type: application/json"
$ {"data":"element1"}
```

## MiniKube
To implement with MiniKube run the following commands:
```
# Run commands from main folder
$ minikube start
$ cd web
$ eval $(minikube docker-env)
$ docker build -t yaml-extract-web .
$ cd ..    # return to main folder
$ minikube addons enable ingress
$ kubectl apply -f ./yamls
$ minikube service yaml-extract-service --url
```
Navigate to the IP displayed and check with /health if the minikube loadbalancing between the two Pods.

### Testing
Same as Web API tests but with different host
```
# Run commands from main folder
$ curl http://<your host>/api/yaml_extract --data-binary "@./tests/request.json" -H "Content-Type: application/json"
$ {"data":"element1"}
```