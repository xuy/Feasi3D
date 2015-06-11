#!/bin/sh

wget http://cython.org/release/Cython-0.22.tar.gz
tar -zxvf Cython-0.22.tar.gz
rm -rf  Cython-0.22.tar.gz
cd Cython-0.22
python setup.py install
