import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "otter-grader",
	version = "0.0.11",
	author = "UC Berkeley Division of Data Science and Information",
	author_email = "cpyles@berkeley.edu",
	description = "Jupyter Notebook Autograder",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/ucbds-infra/otter-grader",
	license = "BSD-3-Clause",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
	],
	install_requires=["gofer-grader==1.0.3", "nb2pdf==0.0.2"],
	scripts=["bin/otter"]
)