import os

# Import PyFyre's core modules
pyfyre_path = os.path.join("pyf-modules")
with open(os.path.join(pyfyre_path, "pyfyre.py")) as file:
	exec(file.read())
with open(os.path.join(pyfyre_path, "widgets", "__init__.py")) as file:
	exec(file.read())
with open(os.path.join(pyfyre_path, "ajax", "__init__.py")) as file:
	exec(file.read())

# Import user's `src/main.py` file
with open(os.path.join("src", "__init__.py")) as file:
	exec(file.read())