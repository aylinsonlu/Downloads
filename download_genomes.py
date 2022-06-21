import os
from re import S
import sys
import ftputil
import shutil




def download_genomes(base_path):
    host = ftputil.FTPHost('ftp.ensembl.org','anonymous','password')

    host.chdir('/pub/release-106/fasta/')
    genomes_directories = host.listdir(host.curdir)

    for genomes_directory in genomes_directories:
        host.chdir('/pub/release-106/fasta/' +genomes_directory + '/')
        sub_genomes_directories = host.listdir(host.curdir)
        for sub_genomes_directory in sub_genomes_directories:
            if sub_genomes_directory == "dna":
                host.chdir('/pub/release-106/fasta/' +genomes_directory + '/dna/')
                dna_files = host.listdir(host.curdir)
                for dna_file in dna_files:
                    if ".dna_sm.primary_assembly.fa.gz" in dna_file:
                        species_name = dna_file.split(".")[0]
                        os.makedirs(base_path+species_name)
                        download_path = base_path+species_name
                        os.chdir(download_path)
                        #os.mkdir(os.path.join(base_path))
                        host.keep_alive()
                        host.download('/pub/release-106/fasta/' +genomes_directory + '/dna/'+dna_file, os.path.join(download_path,species_name+".fa.gz"))
                        bashCommand ="gunzip " +species_name+".fa.gz"
                        os.system(bashCommand)
                    elif  ".dna_sm.toplevel.fa.gz" in dna_file:
                        species_name = dna_file.split(".")[0]
                        os.makedirs(base_path+species_name)
                        download_path = base_path+species_name
                        os.chdir(download_path)
                        #os.mkdir(os.path.join(base_path))
                        host.keep_alive()
                        host.download('/pub/release-106/fasta/' +genomes_directory + '/dna/'+dna_file, os.path.join(download_path,species_name+".fa.gz"))
                        bashCommand ="gunzip " +species_name+".fa.gz"
                        os.system(bashCommand)
                
if __name__ == "__main__":
    base_path = sys.argv[1]
    download_genomes(base_path)

