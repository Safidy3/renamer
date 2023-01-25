
import os, re


patern =  "\?"
newPatern = ""

def rename_file(p = './', depth = 0):

	counter = 0
	list = os.listdir()

	# contdition to print only matching patern file name
	for fichier in list:
		if re.search(patern, fichier):
			counter += 1
	if counter > 0:
		print(f"\n******* depth : {depth} *******")
		print(f"\t{p} :\n")

	# renaming matching patern file name
	for fichier in list:
		if not os.path.isdir(fichier) and re.search(patern, fichier):
			newname = re.sub(patern, newPatern , fichier)
			os.rename(fichier , newname)
			if counter > 0:
				print(newname)

	# recursive function for child directory
	for fichier in list:
		if os.path.isdir(fichier):
			os.chdir(fichier)
			depth += 1
			rename_file(fichier, depth)
			os.chdir('../')

rename_file()





