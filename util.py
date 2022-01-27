import os
import json

def get_content():
	try:
		fname = "./Readme.md"
		_ = open(fname, "rb").read().decode()
		return json.loads(_)
	except:
		return None
	
def get_tasks(year, CTF):
	try:
		fname = "./writeup/{year}/{CTF}/Readme.md".format(year = year, CTF = CTF)
		_ = open(fname, "rb").read().decode()
		return json.loads(_)
	except:
		return None



if __name__ == "__main__":
	_ = get_tasks("2021", "TestCTF")
	print(_)
	_ = get_content()
	print(_)
