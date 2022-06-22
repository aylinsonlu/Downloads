import os
from re import S
import sys
import ftputil
import shutil
import re

def download_gtf(base_path,host,ftp_site):
    dirs = os.listdir(base_path)
    host = ftputil.FTPHost(host,'anonymous','password')

    host.chdir(ftp_site)
    species_directories = host.listdir(host.curdir)

    for species_directory in species_directories:
        host.chdir(ftp_site +species_directory + '/')
        gtf_files = host.listdir(host.curdir)
        for gtf_file in gtf_files:
            if ".".join(gtf_file.split(".")[-2:])=="gtf.gz":
                if re.match(r'^([\s\d]+)$', gtf_file.split(".gtf.gz")[0].split(".")[-1]):
                    species_name = gtf_file.split(".")[0]
                    if species_name in dirs:
                        continue
                    else:
                
                        os.makedirs(base_path+species_name)
                        download_path = base_path+species_name
                        os.chdir(download_path)
                        #os.mkdir(os.path.join(base_path))
                        host.keep_alive()
                        host.download(ftp_site +species_directory+ '/' +gtf_file, os.path.join(download_path,species_name+".gtf.gz"))
                        bashCommand ="gunzip " +species_name+".gtf.gz"
                        os.system(bashCommand)
    

if __name__ == "__main__":
    base_path = sys.argv[1]
    host = sys.argv[2]
    ftp_site = sys.argv[3]
    download_gtf(base_path,host,ftp_site)


