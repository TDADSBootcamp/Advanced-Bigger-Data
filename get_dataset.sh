#!/bin/bash

# fetches the dataset and stores it in the uncommitted directory

set -x # trace output - show each command as it runs
set -e # stop on error
set -u # stop if we reference an unset variable 
set -o pipefail # on error, set the script exit code to the errored set
# usually expressed as the one-liner 'set -euo pipefail'
# see https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail for a detailed explanation of options

# Zaker, Farzin, 2019, "Online Shopping Store - Web Server Logs", https://doi.org/10.7910/DVN/3QBYB5, Harvard Dataverse, V1
#DATASET_URL="https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/3QBYB5/NXKB6J"
# This dataset has been withdrawn in May 2021 as it may contain sensitive data!

# An anonymised version is available at
DATASET_URL="https://843328850426-access-log.s3.eu-west-2.amazonaws.com/access_masked.log.gz"

# get the directory the script is in
BASEDIR=$(dirname "$0")

# use BASEDIR to define other paths - other options have drawbacks:
# - using relative paths like './uncommitted' are relative to where the script is run - might not be where we expected
# - using absolute paths like '/foo/bar' means we have to make assumptions about the user's system and context
UNCOMMITTED=${BASEDIR}/uncommitted

# -p option creates parent directories where needed - but also doesn't fail if the dir already exists
mkdir -p ${UNCOMMITTED}

ACCESS_LOG_PATH=${UNCOMMITTED}/access.log.gz

# download the dataset
/usr/bin/time --output ${UNCOMMITTED}/download_time.txt wget ${DATASET_URL} -O ${ACCESS_LOG_PATH}

# decompress the dataset, keeping the original file
gunzip -k ${ACCESS_LOG_PATH}

echo "Dataset downloaded to ${UNCOMMITTED}/access_log"
