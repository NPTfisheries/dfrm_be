# dfrm_be
Set-up instructions for DFRM backend django ORM services.

1. Install Postgresql 14 (or diff version)
	a. use postgresql stack to install PostGIS
2. Install QGIS 3.28 (or diff version)
3. Install git
4. Install Python 3.10 (of diff version)
	a. click install pip
	b. click add 'python' to environment path during installation setup
5. After python is installed:
	a. install 'virtualenv' using pip -m install virtualenv (maybe try to remove -m)
	b. the virtualenv package will help us set-up a virtual environment to run the application
		i. thus allowing us to install separate instances/versions of software for different application (eliminating some sources of dependency problems)
6. create the directory C://website/developement
	a. once the directory is created open cmd and change directories to the developement folder
	b. in the development folder create a virtual environment
		i. using the cmd prompt type: virtualenv venv
		ii. the name of the environement is "venv"
		iii. activate the virtual environment with the correct method for CMD or Powershell (make sure you are in the correct directory)
				Windows CMD: C:\website\development> venv\Scripts\activate.bat
				Powershell: C:\website\development> venv\Scripts\Activate.ps1
		iv. you should see the name of the environment to the left of the CMD prompt: (venv) C:\website\development>
7. in the cmd prompt run: pip install django
8. clone the existing django project
	a. inside the developement folder, and with the virtual environment running type the following in command prompt:
		i. git clone "https://github.com/ACCOUNT_NAME/REPO_NAME.git"
9. change directories into the project folder
10. now we need to install all the necessary packages to run the application
	a. before we install pkgs, check the requirements.txt file for a .whl file starting with GDAL, remove if it appears
	b. now run: pip install -r requirements.txt
11. paste in the .env file into the same directory as settings.py
	a. the settings.py file will be at: website/dfrm_be/website/
	b. the .env file is similar to a web.config file and housing secret information that should not be shared on GitHub, so we need to copy it over manually
12. Update the .env file with django's secret key and database information specific to your instances/versions
	a. get a new secret key and copy over the existing one in the .env file, do this from :https://djecrety.ir/
	b. paste in database name, user, pass, host and port information
13. In the settings.py file change the filepath for GDAL and GEOS to the bin folder in QGIS (e.g., Program Files/QGIS X.X.X/bin/gdal)
NEW DIRECTIONS BASED ON TROUBLESHOOTING incompatible software versions.....make sure all software and python packages are the same as development environment
14. Open pgAdmin4 and create a database named: "dfrm_be"
15. migrate django ORM to database...
	a. python manage.py migrate
	b. migrations are built from dev environment so we don't need to run "makemigrations"
16. load data previously entered from dev environment
	a. after migrate command in step 15.
	b. run "python manage.py loaddata ../backup.json"
	c. backup.json was created from development environment using:
			"python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > backup.json"
17. now test the installation:
	a. python manage.py runserver