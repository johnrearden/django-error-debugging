# django-debugging
Django project with multiple branches, each with a single bug

# Instructions

Click the gitpod button and open your own workspace from this git repository. You can checkout each
branch in turn (there are 7 in all) e.g. 

`git checkout branch1`

Then run the server with 

`python manage.py runserver`

And try to fix the bug! There's a link to a video of each fix below, but give it a go on your own first! 

# Switching to the next branch

You won't be able to switch to another branch if you have made changes to the branch you're currently in! You can save your work and run `git add .` and `git commit -m '{MEANINGFUL_MESSAGE}'` in the local git repo.

If you'd just like to switch back to the main branch without committing any changes you've made, you can run `git reset --hard`, which will return the filesystem to the state it was in just after the last commit.

![instruction_diagram](static/doc_images/django-debugging-diagram.png)

# Branches, Errors and Solutions
Branch 1 - 400 Bad Request [video solution](https://youtu.be/zEXMulgZrnE)

Branch 2 - TemplateDoesNotExist [video solution](https://youtu.be/9QDwl-FkQws)

Branch 3 - NoReverseMatch [video solution](https://youtu.be/sVr9JBglrH8)

Branch 4 - Where's my form gone! [video solution](https://youtu.be/_I4wsFe_oLM)

Branch 5 - Where's my home page gone! [video solution](https://youtu.be/qPKhm4DcH3I)

Branch 6 - OperationalError - no such table [video solution](https://youtu.be/y6znhjy7Gfk)

Branch 7 - Where have my styles and background image gone? [video solution](https://youtu.be/gpn_uplePvE) - for bonus points solve without changing settings.py!


