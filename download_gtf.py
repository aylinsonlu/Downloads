import os
from re import S
import sys
import ftputil
import shutil

def download_gtf(base_path):

    host = ftputil.FTPHost('ftp.ensembl.org','anonymous','password')

    host.chdir('/pub/release-106/gtf/')
    species_directories = host.listdir(host.curdir)

    for species_directory in species_directories:
        host.chdir('/pub/release-106/gtf/' +species_directory + '/')
        gtf_files = host.listdir(host.curdir)
        for gtf_file in gtf_files:
            #print(gtf_file)
            if "106.gtf.gz"  in gtf_file:
                species_name = gtf_file.split(".")[0]
                os.makedirs(base_path+species_name)
                download_path = base_path+species_name
                os.chdir(download_path)
                #os.mkdir(os.path.join(base_path))
                host.keep_alive()
                host.download('/pub/release-106/gtf/' +species_directory+ '/' +gtf_file, os.path.join(download_path,species_name+".gtf"))
    

if __name__ == "__main__":
    base_path = sys.argv[1]
    download_gtf(base_path)
