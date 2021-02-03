# -*- coding: utf-8 -*-
"""
Default organizer for bioinfoinformatics project directiories - RNA-Seq based model
"""
import os 
import sys

#main path

curr_path = os.getcwd()
print("\nYour current directory is: " + curr_path + "\n\nIt contains the following files and directories:\n\n" + str(os.listdir("."))) # displays the current directory and list it subdirectories

project_path = input(str("\nPath of the directory where you want to start your project: "))

path_to = os.chdir(project_path) # change to the desired directory to start the project

response = input(str("Are you ready to start a new bioinformatics project? (Y or N): " ))
project = input(str("Project name: " if response == "Y" else print("\nThat's ok, you can try it later.") + sys.exit()))

os.mkdir(project) # cria um diretório para o trabalho de raiz de cana

os.chdir(project) # muda para o diretorio sugarcane_raiz (igual ao cd)

#print(os.getcwd()) # mostra o diretório atual

data = os.mkdir("data")
raw_data = os.mkdir("data/raw_data")
processed_data = os.mkdir("data/processed_data")
genome_references = os.mkdir("data/genome_references")
programs = os.mkdir("programs")
analysis = os.mkdir("analysis")
data_pre_process = os.mkdir("analysis/data_pre_process")
assembly = os.mkdir("analysis/assembly")
annotations = os.mkdir("analysis/annotations")
alignements = os.mkdir("analysis/alignements")
quantification = os.mkdir("analysis/quantifications")
results = os.mkdir("results")
logs = os.mkdir("results/logs")
output = os.mkdir("results/output")
html = os.mkdir("results/html")
errors_out = os.mkdir("results/errors_out")
notebook = os.mkdir("notebooks")
scripts = os.mkdir("scripts")

print("\n\n-- Your directories are ready to keep your project organized. --")

print("\n\nThe current main project diretory has the following subdirectories:\n", os.listdir("."))
print("\nThe diretory data has the following subdirectories:\n", os.listdir("results"))
print("\nThe diretory analysis has the following subdirectories:\n", os.listdir("analysis"))
print("\nThe diretory results has the following subdirectories:\n", os.listdir("results"))

print("\n\n ---------- Enjoy your research! :) ----------")

