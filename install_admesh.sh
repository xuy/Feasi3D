#!/bin/sh

wget https://github.com/admesh/admesh/releases/download/v0.98.2/admesh-0.98.2.tar.gz
tar -zxvf admesh-0.98.2.tar.gz
rm -rf  admesh-0.98.2.tar.gz
cd admesh-0.98.2
./configure
make
make install
