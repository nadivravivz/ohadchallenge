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
* [Python3](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/get-docker/)
if the installation doesn't include docker-compose, you will have to install it manually.
* [MiniKube](https://minikube.sigs.k8s.io/docs/start/)

## Implementation options
* [CLI](#cli)
* [Docker](#docker)
* [Web API](#web-api)
* [MiniKube](#minikube)

## CLI
blabllba

## Docker
lablalbla

## Web API
flsfklsdkf

## MiniKube
sdfsdfsdf