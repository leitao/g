import os

def init():
	gitdir = os.getcwd() + "/.git"
	print("Initialized empty Git repository in ", gitdir)

	# Create base directory
	os.makedirs(gitdir, exist_ok=True)


	# Create directories
	for dir in ["objects/info", "refs/heads", "refs/tags", "branches", "info"]:
		os.makedirs(gitdir + "/" + dir, exist_ok=True)

	# Create .git/HEAD file
	HEADfile = open(gitdir + "/HEAD", "w")
	HEADfile.write("ref: refs/heads/master\n")
	HEADfile.close()
