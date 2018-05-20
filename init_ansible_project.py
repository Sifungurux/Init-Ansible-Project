


import argparse
import os
from pathlib import Path
from subprocess import call

parser = argparse.ArgumentParser(description="Init of ansible projects")
parser.add_argument('-p', '--project', help='Set project name',required=True)
parser.add_argument('-d', '--development', help='Set delvelopment platform', choices=['vagrant', 'docker'])

args = parser.parse_args()

print("Initilizing project {} - using {}".format(args.project, args.development))
print()

projectname = args.project

home = str(Path.home())
projecthome = "{}/{}".format(home, 'Projects')
try:
    try:
        os.listdir(projecthome)
    except:
        os.mkdir(projecthome)

    try:
        projectfolder = "{}/{}".format(projecthome, projectname)
        if os.path.isdir(projectfolder) == False:
            os.mkdir(projectfolder)

    except OSError:
            print ("Creation of the directory {} failed".format(projectname))

    folder_structure = ['tasks', 'default', 'var', 'handlers', 'meta', 'templates']

    for folder in folder_structure:
        try:
            if os.path.isdir("{}/{}".format(projectfolder, folder)) == False:
                os.mkdir("{}/{}".format(projectfolder, folder))	
                open("{}/{}/main.yml".format(projectfolder,folder),"w+")


        except OSError:
            print ("Creation of the directory {} failed".format(projectname))

    if args.development:
        try:
            if os.path.isdir("{}/tests".format(projectfolder)) == False:
                os.mkdir("{}/tests".format(projectfolder))
                os.chdir("{}/tests".format(projectfolder))
                if args.development == 'vagrant':
                    call(["vagrant", "init"])
        except OSError:        
            print("failed")
except:
    print("failed to initilize project")
else:
    print()
    print ("Successfully initilize {} project".format(folder))

