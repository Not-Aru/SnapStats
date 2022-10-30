# SnapStats
CS348 Project

SnapStats is a simple Django application where you can view NFL stats for your favorite teams and players.

### How to run

1. A project directory is required. Create a folder to store the app. 
2. CD into the newly created folder.
3. Setup pyenv virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```
4. Clone git repository
```bash
git clone "https://github.com/Not-Aru/SnapStats"
```
5. Edit `settings.py` with your MySQL (or preferred DB) database information 
6. Save all files and run
```bash
python manage.py makemigrations app
python manage.py migrate
```
7. The previous step will propogate tables into your DB and apply settings. Ensure that this has been done (in MySQL, run `show tables;` or some other command to verify that the Django models were translated to DB tables). Now, run `python manage.py collectstatic`. This will let Django find the bootstrapped frontend files. 
8. Run the server: `python manage.py runserver`. 
9. The project will be up and running. Visit the link in the terminal output in your browser. 