# SnapStats
CS348 Project

SnapStats is a simple Django application where you can view NFL stats for your favorite teams and players.

### How to run

1. A project directory is required. Create a folder to store the app. 
2. CD into the newly created folder.
3. Setup pyenv virtual environment:
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
4. Clone git repository:
```bash
git clone "https://github.com/Not-Aru/SnapStats"
```
5. Edit `settings.py` with your MySQL (or preferred DB) database information (make sure the DB name matches if using MySQL, as well as creating a user with the correct credentials to grant Django the privileges to pull and edit tables).
6. MySQL creates tables with different column ordering than `models.py`. Run the following within MySQL to ensure proper column ordering for data sourcing: 
```bash
alter table app_teams modify column team_name longtext after stadium_id_id;
alter table app_teams modify column division longtext after team_name;
alter table app_players modify column college longtext after team_id_id;
alter table app_players modify column years_on_team int after team_id_id;
alter table app_players modify column games_started int after years_on_team;
alter table app_players modify column player_age int after team_id_id;
alter table app_games modify column home_team_points int after home_team_id_id;
alter table app_games modify column away_team_points int after home_team_points;
alter table app_games modify column away_team_id_id int after home_team_id_id;
```
7. The data is available in `data/data.sql`. Run `source <path-to-data-file>` within MySQL to populate the MySQL tables. 
8. Save all files and run:
```bash
python manage.py makemigrations app
python manage.py migrate
```
9. The previous step will propogate tables into your DB and apply settings. Ensure that this has been done (in MySQL, run `show tables;` or some other command to verify that the Django models were translated to DB tables). Now, run `python manage.py collectstatic`. This will let Django find the bootstrapped frontend files. 
10. Run the server: `python manage.py runserver`. 
111. The project will be up and running. Visit the link in the terminal output in your browser. 