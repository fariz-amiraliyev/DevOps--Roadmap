#!/usr/bin/env python

# Scope: Use scripts to generate base templates for Kubernetes per environment
# sample usage:
# python bin/kube_generate.py \
# --service_name test-service \
# --docker_version_tag nginx \
# --environment staging
# Author: Infrastructure Squad
# Date: 04/04/2018

import logging
import argparse
import os
from jinja2 import Environment

THIS_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(level=logging.INFO)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--service_name", "-s", help="Enter Service Name", required=True
    )
    parser.add_argument(
        "--docker_version_tag",
        "-d",
        help="Enter Docker Image Version Tag",
        required=True,
    )
    parser.add_argument(
        "--environment", "-e", help="Enter Environment Name", required=True
    )
    return parser.parse_args()


class ServiceTemplate:
    HOSTED_ZONES = {
        "production": ".internal.earnest.com",
        "staging": ".staging.earnest.com",
        "development": ".earnest.io",
    }

    def __init__(self, name, docker_version_tag, environment):
        self.name = name
        self.image = f"earnest/{name}:{docker_version_tag}"
        self.environment = environment
        self.hostname = f"{name}{self.HOSTED_ZONES[environment]}"

    def render(self):
        template_path = os.path.join(
            THIS_FILE_PATH, f"../templates/jsonnet-service.jsonnet.j2"
        )

        with open(template_path, "r") as f:
            template = f.read()

        return Environment().from_string(template).render(**self.__dict__)


if __name__ == "__main__":
    args = get_args()

    # create service folder
    service_env_path = os.path.join(THIS_FILE_PATH, f"../{args.environment}")
    service_path = os.path.join(service_env_path, f"{args.service_name}.jsonnet")

    # check if path exists
    if not os.path.exists(service_env_path):
        os.makedirs(service_env_path)

    template = ServiceTemplate(
        args.service_name, args.docker_version_tag, args.environment
    )

    with open(service_path, "w") as f:
        f.write(template.render())

    logging.info("service manifet created in:")
    logging.info(service_path)
