'''
The MIT License (MIT)

Copyright (c) 2015 Anand Sudhanaboina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import core, os

# Try to fetch email and username from git config
author_name = (os.popen('git config --global user.name').read()).rstrip()
author_email = (os.popen('git config --global user.email').read()).rstrip()

# Fallback for email and username if not found in git config
if not (author_email and author_name):
	print "Enter your details, to avoid this set your email to git config."
	if not author_email:
		author_email = str(raw_input("Email: "))
	if not author_name:
		author_name = str(raw_input("Username: "))

# Read the message
print "Enter the message you want to display in your Github profile: (This will be trimmed to 8 chars)"
message = str(raw_input())

# Trigger the build
git_dir =  core.init(message, author_name, author_email)

# Print the response
print "\nGit commit history generated, now:\ncd " + git_dir + "\ngit remote add origin https://github.com/example/yourrepo.git\ngit push origin master"