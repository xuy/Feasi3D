FROM python:2.7
MAINTAINER Eric Xu, xy@1001hao.com

# use base python image with python 2.7
ENV PYTHONUNBUFFERED 1

# Make sure we have git and other handy tools
RUN apt-get install -y git
 
# Install admesh
ADD install_admesh.sh /tmp/
RUN /tmp/install_admesh.sh

# Install Cython
ADD install_cython.sh /tmp/
RUN /tmp/install_cython.sh

# Deploy folder
RUN mkdir /app
WORKDIR /app

# add requirements.txt to the image
ADD requirements.txt /app/

RUN pip install -r requirements.txt

# Additional requirements
ADD test.py /app/
ADD test.stl /app/

ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /app
COPY feasi3d /app
RUN python test.py test.stl
