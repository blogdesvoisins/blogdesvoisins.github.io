import os
import sys

from path import Path

def add(file,texte):
	content = open(file).readlines()
	try:
		indice = content.index('				<li><a href="index.html">Accueil</a></li>\n')+1
	except ValueError:
		print(f"{file.name} malformed")
	if content[indice] == texte:
		print(f"{file.name} was good")
		return
	content.insert(indice,texte)
	with open(file,"w") as f:
		f.write(''.join(content))
	print(f"{file.name} processed")



def main():
	texte = '				<li><a href="'+sys.argv[1]+'">'+sys.argv[2]+'</a></li>\n'
	path = Path(os.getcwd())
	for file in path.files():
		if file.ext == ".html" and file.name != "index.html":
			add(file,texte)


if __name__ == '__main__':
	main()