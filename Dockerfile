# using the lastest version of Ubuntu 22.04 as a base for the Docker image
FROM ubuntu:22.04

# installing Python and Unzip
RUN apt-get update && apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip libgomp1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# creating the root folder
RUN mkdir -p /mlops-classification-project

# copying all the files within this folder to the newly created folder
COPY . /mlops-classification-project

# setting the curreting directory to be the folder containing the files
WORKDIR /mlops-classification-project

# deleting the notebooks folder and keeping only the code version, which will
# be used by the API
RUN rm -r /mlops-classification-project/*.ipynb

# installing the requirements
RUN uv sync --locked
