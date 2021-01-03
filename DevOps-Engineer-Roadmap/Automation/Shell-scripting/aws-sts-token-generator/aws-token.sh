#!/usr/bin/env bash

docker run -it --rm -v $HOME/.aws/:/root/.aws/ xxxx/aws-sts-token-generator:2.0.0 "$@"
