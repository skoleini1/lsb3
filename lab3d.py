#!/usr/bin/env python3

# Author ID: skoleini1

import subprocess
def free_space():


	p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	output = p.communicate()

	stdout = output[0].decode('utf-8').strip()
	return stdout
result = free_space()
print(result)



