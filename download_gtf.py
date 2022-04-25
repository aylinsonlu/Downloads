import os
from re import S
import sys
import ftputil
import shutil

#base_path = "/Users/aylin/Desktop/"
base_path = "/cta/users/abircan/GTFs_release_106/"
host = ftputil.FTPHost('ftp.ensembl.org','anonymous','password')

host.chdir('/pub/release-106/gtf/')
species_directories = host.listdir(host.curdir)

for species_directory in species_directories:
    host.chdir('/pub/release-106/gtf/' +species_directory + '/')
    gtf_files = host.listdir(host.curdir)
    for gtf_file in gtf_files:
        #print(gtf_file)
        if "106.gtf.gz"  in gtf_file:
            os.chdir(base_path)
            #os.mkdir(os.path.join(base_path))
            host.keep_alive()
            host.download('/pub/release-106/gtf/' +species_directory+ '/' +gtf_file, os.path.join(base_path,gtf_file))
     