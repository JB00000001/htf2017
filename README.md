# htf2017
This file contains the information of a big data challenge at a hackaton event. This is an event to introduce students with no prior experience to the big data domain by giving them hands-on experience on AWS. THe dataset used is the landsat 8 satellite data set containing over 1 million images and the csv file containing the metadata of these images (see pdf for the exact steps in this lab). I want to explicitly talk Liam De Lee for  installing the necessary python libraries and sharing his AWS skills.
## Setting up the EMR cluster
We will spin up an EMR cluster m3xlarge consisting of 1 master node and 2 slaves. We choose the installation that includes Hadoop 2.7.3- Zeppelin 0.7.3 (notbook) and Ganglia 3.7.2 (for monitoring the memory use of the cluster), and Spark 2.2.0(the parallel computing framework).To install all necessary python package,  bootstrapping script is used. We were charged for this cluster and found the charges to be about 0.75 $/hour- so around 10$ / day of work.
## Files included
### Big data Hackaton 2017_0.2.pdf
The pdf with the purpose of this one day lab explained in a step-by-step guide.
### bashscript.sh
This is the bootstrapping script used to do the necessary installations on the master node of the EMR cluster. THe script will install alls necessary components to be able to display graphics on the master node (first 4 lines starting with X). Next it installs miniconda - a more compact version of anaconda (the python libraries for large-scale data processing, predictive analytics, and scientific computing). This is a prerequisite for the installation of several packages required to load our satellite data (using the conda install commands).
### s3 python pyspark boto commands.txt
This contains the commands to explore the data a bit: the commands to list and download the satellite image from s3, next some commands to load the data into panda dataframes on a local station (not using emr nor spark), and finally the pyspark commands to load the data on hdfs and do some simple queries and calculations using the cloudcover column. Finally the boto3 package is used to write the data to dynamodb.
### Note.json
THe json extract from the zeppelin notebook that was used to fire off the pyspark commands (very similar to the s3 python pyspark boto commands.txt file).
### showgeo_Antwerp.py
A python code that makes use of the gdal libraries installed by the bootstrapping script to show a satellite image of Antwerp. Note that when working under Windows an xming installation is required.
## Acknowledgements
I want to explicitly talk Liam De Lee for installing the necessary python libraries and sharing his AWS skills to set up the EMR cluster.
