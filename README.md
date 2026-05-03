# CRM
Building a CRM and then updating it to include better documentation. testing, learning more about database and making it into a better app.

# github(important commands)
Always commit changes before switching branches, (git commit or stash)
to switch branch: git switch branch-name
to create and switch branch: git checkout -b "new-branch-name"
if forgot to commit changes and you want your x branch to look exactly like the updated y branch : 
switch to branch x and git rebase y (slightly risky)

# imp terminal commands
python manage.py migrate (migrate db changes)
python manage.py runserver (runserver duh)
django-admin startproject dcrm
python manage.py startapp "appname"
New-Item "filename.extension"
python manage.py createsuperuser (to create an admin)

# WORKFLOW after creating app
-->work on views and urls
