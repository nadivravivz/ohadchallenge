# yaml-extract tool

## About
This tool acts like JSONPath but for YAMLS.<br />
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
cd CLI
pip install -r requirements.txt
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
lablalbla

## Web API
flsfklsdkf

## MiniKube
sdfsdfsdf