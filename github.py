import git, os, random

def init(dir):
	REPO_PATH = dir
	REPO = git.Repo.init(REPO_PATH)
	return REPO

def write_rand(rand_file):
	f = open(rand_file,'w')
	f.write(str(random.randrange(0,1000)))
	f.close()

def commit(REPO, date, dir, author):
	write_rand(dir+"/rand")
	REPO.index.add([dir+"/rand"])
	REPO.index.commit(message="commit-"+str(random.randrange(0,1000)),author_date=date, commit_date=date, author=author, committer=author)