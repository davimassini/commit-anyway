from git import Repo
import sys
import random
import requests

PATH_ACTUAL = sys.argv[0].replace("\pick_a_number.py", "")
PATH_FOLDER = sys.argv[1]
RANDOM = random.randint(0, 20)

def open_and_write():
    with open(r'{}\ascii_art.txt'.format(PATH_ACTUAL), "r+") as ascii_art:
        with open(r'{}\README.md'.format(PATH_FOLDER), "a+") as readme_md:
            content = ascii_art.read()
            ascii_art.seek(0)
            ascii_art.truncate()
            
            readme_md.write(content[:1])
            ascii_art.write(content[1:])

def get_quote():
    response = requests.get("https://api.quotable.io/random").json()
    return response["content"] + " | " +  response["author"]

def git_push():
    try:
        repo = Repo(r'{}\.git'.format(PATH_FOLDER))
        repo.git.add(update=True)
        repo.index.commit(get_quote())
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

for _ in range(RANDOM):
    open_and_write()
    git_push()