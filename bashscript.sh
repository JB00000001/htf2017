#!/bin/bash
sudo yum -y install xauth
sudo yum -y install xterm
sudo yum -y install xorg-x11-apps
sudo yum -y install xorg-x11-server-Xorg
cd /home/hadoop
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
yes yes | bash Miniconda2-latest-Linux-x86_64.sh -b
export PATH=~/miniconda2/bin:$PATH
conda config --add channels conda-forge
yes yes | conda install boto
yes yes | conda install pyspark
yes yes | conda install matplotlib
yes yes | conda install gdal
yes yes | conda install geos=3.4.2
yes yes | conda install xerces-c=3.1
yes yes | conda install gdal
yes yes | conda install poppler