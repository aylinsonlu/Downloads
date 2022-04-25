import os
from re import S
import sys
import ftputil
import shutil


base_path = "/cta/users/abircan/Genomes_release_106/"
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
                    os.chdir(base_path)
                    #os.mkdir(os.path.join(base_path))
                    host.keep_alive()
                    host.download('/pub/release-106/fasta/' +genomes_directory + '/dna/'+dna_file, os.path.join(base_path,dna_file))
                elif  "dna_sm.toplevel.fa.gz" in dna_file:
                    os.chdir(base_path)
                    #os.mkdir(os.path.join(base_path))
                    host.keep_alive()
                    host.download('/pub/release-106/fasta/' +genomes_directory + '/dna/'+dna_file, os.path.join(base_path,dna_file))
               

