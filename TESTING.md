<h1 id="top">Cocktail Nerd Testing</h1>

Back to the [README](README.md)

<h1 id="contents">Contents</h1>

- [Automated Unit Testing Results](#automated-testing-results)
- [Automated Functional Testing Results](#automated-testing-results)
- [Manual Testing Results](#manual-testing-results)
- [Frontend](#frontend)
- [Backend/Admin Panel](#backend)
- [Python Validation - PEP8](#python-validation)
- [Lighthouse](#lighthouse)
- [Console Results](#console-results)
- [Bugs / Issues](#bugs)

Testing has taken place continuously throughout the development of the project. The app was tested regularly and deployed early to Heroku to confirm local and remote functioned the same. 


<h2 id="automated-testing-results">Automated Unit Testing Results</h2>


### Before Automated Unit testing coverage was at 79%


![admin.py](documentation/readme_images/testing/before-automated-tests.webp)

### After Automated Unit testing coverage is at 93%

* Increased the models coverage testing from 83% to 100%

* Increased the signals coverage testing from 73% to 100%

* Increased the views coverage testing from 55% to 80%


This could be improved on of course to get to 100% coverage and is something I could look at completing over time. All test files are located in the Cocktailapp/tests folder in the project.


![admin.py](documentation/readme_images/testing/after-automated-tests.webp)


<h2 id="automated-testing-results">Automated Behaviour Driven Development Testing Results</h2>

<a href="#top">Back to the top</a>


The automated Behaviour Driven Development tests were performed with Selenium & Pytest but as this had to be run on a local development enviroment as the Chromedriver would not run on Gitpod, I have included the test file below.

The Username & Passwords were loaded from the seperate env.py file so as not to expose the username & password in the test file on Gitpod.

I ran 4 automated functional tests:

* Test homepage renders for logged out user

* Test a logged in user can like a post

* Test a logged in admin user can delete a post

* Test a logged in admin user can create a post

Behaviour Driven Development Testing Variables '.env' File

```
USER_NAME = <your_username_here>
USER_PASSWORD = <your_password_here>
```
Behaviour Driven Development PyTest Code

```
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import os

USER_NAME = os.environ['USER_NAME']
USER_PASSWORD = os.environ['USER_PASSWORD']

class Hosttest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def site_admin_login(self):
        self.driver.get('http://127.0.0.1:8000/account/login/')
        self.driver.find_element(By.ID, 'id_login').send_keys(USER_NAME)
        self.driver.find_element(By.ID, 'id_password').send_keys(USER_PASSWORD)

        self.driver.find_element(By.ID, 'nerd-login').click()

    # Test home page renders for a logged out user
    def test_loggedout_homepage(self):
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(2)
        expected = "Cocktail Nerd"
        assert self.driver.title == expected

    # Test logged in user can like a  post
    def test_userlikedpost(self):
        self.site_admin_login()
        self.driver.get('http://127.0.0.1:8000/test-post-2/')
        self.driver.set_window_size(1578, 1297)

        time.sleep(2)

        assert "Cocktail Nerd | Test Post 2" in self.driver.title

        self.driver.find_element(By.ID, 'like-button').click()

    # Test a logged in admin user can delete a post
    def test_user_deletes_post(self):
        self.site_admin_login()
        self.driver.get('http://127.0.0.1:8000/test-post-3/')
        self.driver.set_window_size(1578, 1297)

        time.sleep(2)

        m = self.driver.find_element(By.ID, 'nerd-delete-post')

        time.sleep(2)

        m.click()
        
        d= self.driver.find_element(By.CLASS_NAME, "btn-outline-danger")
        d.click()
        
        expected = "Cocktail Nerd | Manage Posts"
        assert self.driver.title == expected

    # Test a logged in admin user can create a post
    def test_user_create_post(self):
        self.site_admin_login()
        self.driver.get('http://127.0.0.1:8000/add_post/')
        self.driver.set_window_size(1578, 1297)

        time.sleep(2)

        self.driver.find_element(By.ID, 'id_title').send_keys('Test Post 5')
        self.driver.find_element(By.XPATH, "//select[@name='status']/option[text()='Published']").click()

        
        time.sleep(2)

        summernote_frame = self.driver.find_element(By.ID, 'id_content_iframe')
        self.driver.switch_to.frame(summernote_frame)
        self.driver.find_element(By.CLASS_NAME, 'note-editable').send_keys('Test Post 5 Content')

        self.driver.switch_to.default_content()
        
        p = self.driver.find_element(By.ID, 'nerd-add-post-button')

        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", p)

        expected = "New Post"
        assert self.driver.title == expected

```

Behaviour Driven Development Testing Results - PASS

```
Test results to go here

```


<h2 id="manual-testing-results">Manual Behaviour Driven Development Testing Results</h2>

<a href="#top">Back to the top</a>


![Manual Test Case](documentation/readme_images/testing/cocktail-nerd-manual-testing.webp)


The online version of the Manual Behaviour Driven Development Test Case can be found here <a href="https://docs.google.com/spreadsheets/d/1pHhJgjFstH7W10ThXaSShCkr6ejq12iErlGVMZsmJKk/edit?usp=sharing" target="_blank">**HERE**</a><br>


<h2 id="frontend">Frontend</h2>

<a href="#top">Back to the top</a>


* The Signup, Login and Logout system is working as it should. It shows the right interactive message to the users on Signup, Login and Logout.


## Sign-up

![Sign-up form](documentation/readme_images/testing/auth/sign-up.webp)


## Login

![Login form](documentation/readme_images/testing/auth/login.webp)

![Login Success](documentation/readme_images/testing/auth/success-login.webp)


## Logout

![Logout Confirmation](documentation/readme_images/testing/auth/logout-confirmation.webp)

![Logout Success](documentation/readme_images/testing/auth/success-logout.webp)


* The Profile Page is working properly. It updates the user information and uploads/updates the 
  user profile image. It shows the interactive message to the user once the update is complete.


![Profile Updated Success](documentation/readme_images/testing/auth/success-profile-updated.webp)


* The user profile image in the comments section of the Post Details page has no issues and shows the user image 
  when it is uploaded by the user on the Profile Page. Otherwise the default avatar will be shown.


![Comments Usr Avatar](documentation/readme_images/testing/auth/comments-user-avatar.webp)


* All the internal links are working and bring the user to the right page on the website.
* All the external links are working and bring the user to the right social media page by 
  opening a new browser tab.


![Social Links](documentation/readme_images/testing/auth/social-links-footer.webp)


* The All Cocktails Page shows all the cocktail recipes. The pagination system is working, it adds another page when more than 6 cocktails on the page.


![All Cocktails](documentation/readme_images/screenshots/all-cocktails.webp)


* The drop-down menu in the navbar shows a list of spirit categories on every page of the website.


![All Spirits Dropdown](documentation/readme_images/screenshots/navbar/dropdown-nav-menu.webp)


* If a category is created and has no cocktails in it if you click on this category link an error will be shown that no posts from that category could be found.


![No cocktails found](documentation/readme_images/testing/no-cocktails-found-error.webp)


* On the Post Details Page, the Like/unlike functionality is working without issues and shows 
  the right interactive message to the user when the heart icon is clicked.


![Liked Cocktail](documentation/readme_images/testing/auth/success-cocktail-liked.webp)

![Unliked Cocktail](documentation/readme_images/testing/auth/success-cocktail-unliked.webp)


* The comment form has no issues and it submits a new comment once the form is completed by a registered user. The comment is submitted for approval and the interactive message for this action is working. 


![Comment Submitted](documentation/readme_images/testing/auth/success-comment-sent-for-approval.webp)


* The functionality to delete a comment, previously sent by the user is 
  working without issues. The Bootstrap model will open asking the user if they want to delete 
  the comment. Once the action is complete, the interactive message is displayed at the top of the page.


![Delete Comment Confirmation](documentation/readme_images/testing/auth/delete-comment-confirmation.webp)

![Comment Deleted Success](documentation/readme_images/testing/auth/success-comment-deleted.webp)


* The functionality to update comments, previously sent by the user is 
  working without issues. A new page is opened, to update the comment then when the update button is clicked. Once the action is complete, the interactive message is displayed at the top of the page.


![Comment Edited Success](documentation/readme_images/testing/auth/success-comment-edited.webp)


* On the Posts MGT Page, the CRUD functionality is working without issues. Logged in staffusers or superuser can create, edit or delete posts. The interactive message is displayed at the top of the page.


![Post Managment](documentation/readme_images/screenshots/manage-posts.webp)

![Delete Post](documentation/readme_images/testing/auth/delete-post-confirmation.webp)


* On the Category MGT Page, the CRUD functionality is working without issues. Logged in staffusers or superuser can create, edit or delete categories. The interactive message is displayed at the top of the page.


![Category Managment](documentation/readme_images/screenshots/manage-categories.webp)

![Delete Category](documentation/readme_images/testing/auth/delete-category-confirmation.webp)


* Staffusers or Superuser can add a new post on the frontend from the drop down Admin menu or by clicking the Add New Post button the Post Mgt page.


![Add New Post](documentation/readme_images/screenshots/add-new-post.webp)


* Staffusers or Superuser can add a new category on the frontend from the drop down Admin menu or by clicking the Add New Category button the Category Mgt page.


![Add New Category](documentation/readme_images/screenshots/add-new-category.webp)


<h2 id="backend">Backend/Admin Panel</h2>


<a href="#top">Back to the top</a>

* I have tested the Admin Panel repeatedly since the start of the project. All the models are working without issues.  
* Posts can be filtered by status, date, category or if featured or not
* Whenever a user comments on a cocktail the Superuser has to approve it before it will be displayed on the website. This functionality is 
  working without issues.
* When the staffuser/superuser is publishing a new cocktail recipe all the required fields have to be filled otherwise the author can't submit the post to the database.


![Django Admin Dashboard](documentation/readme_images/testing/django-admin-dashboard.webp)


<h2 id="python-validation">Python Validation - PEP8</h2>

<a href="#top">Back to the top</a>

* Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files
were entered into the online checker and no errors were found in any of the Cocktail Nerd custom code.


# Cocktail Nerd - cocktailapp
* admin.py
![admin.py](documentation/readme_images/testing/pep8/pep8-check-admin.webp)
* apps.py
![apps.py](documentation/readme_images/testing/pep8/pep8-check-apps.webp)
* models.py
![models.py](documentation/readme_images/testing/pep8/pep8-check-models.webp)
* forms.py
![forms.py](documentation/readme_images/testing/pep8/pep8-check-forms.webp)
* signals.py
![signals.py](documentation/readme_images/testing/pep8/pep8-check-signals.webp)
* urls.py
![urls.py](documentation/readme_images/testing/pep8/pep8-check-urls.webp)
* views.py
![views.py](documentation/readme_images/testing/pep8/pep8-check-views.webp)
* processors.py
![processors.py](documentation/readme_images/testing/pep8/pep8-check-processors.webp)


# Cocktail Nerd - cocktailnerd
* admin.py
* There are 5 lines to long in the settings.py file but these are AUTH_PASSWORD_VALIDATORS and cannot be shortend
* The error about the env imported but not used is because it's in the development mode but will not be present on the production version
![Settings lines to long](documentation/readme_images/testing/settings-line-too-long.webp)


<h2 id="lighthouse">Lighthouse</h2>

<a href="#top">Back to the top</a>


Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop and Mobile.


### Desktop Results:
![Lighthouse Mobile Result](documentation/readme_images/testing/lighthouse-desktop.webp)

### Mobile Results:
![Lighthouse Desktop Result](documentation/readme_images/testing/lighthouse-score.webp)

# HTML Validation
![HTML Validation Result](documentation/readme_images/testing/html-validator-results.webp)

### CSS Validation

![W3C CSS Validation Result](documentation/readme_images/testing/css-validator-results.webp)

* Custom CSS was validated using W3C Jigsaw validation service. One warning was displayed, however, 
  this is related to Bootstrap 5 which will not affect the CSS performance.

<h2 id="console-results">Console Results</h2>

<a href="#top">Back to the top</a>


### Desktop
![Desktop Dev Console Result](documentation/readme_images/testing/desktop-dev-console.webp)
* The browser console is clean, no errors are  showing.

### Mobile
![Mobile Dev Console Result](documentation/readme_images/testing/mobile-dev-console.webp)
* The browser console is clean, no errors are  showing.


<h2 id="bugs">Bugs / Issues</h2>

<a href="#top">Back to the top</a>

Due to the nature of the Postgres database being offered by Heroku and the way tests are run in Django, I encounterd an error while trying to run tests on my Django application with Heroku Postgres Add-on connected to the application.


Attempting to run the testing command results in this error


* Got an error creating the test database: permission denied to create database


* To get this to work I created an additional Postgres database as an add-on and used this as my testing database.


* Also added an if 'test' in sys.argv: to the database settings in my project to connect to the test database when testing and an else statement to connect to the production databse when not testing. The below code is not the real production enviroment and has been changed for security reasons and is only to show what I did to solve the issue.

```
# Updates Database Configuration
if 'test' in sys.argv:
    # Configuration for test database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'd7osdssadag0ugv5',
            'USER': 'lhwwasadqlgjra',
            'PASSWORD': '1524f48a2ce41177c4ssdadasd3a11680b735302d14979d312ff36',
            'HOST': 'ec2-54-75-2326-118.eu-west-1.compute.amazonaws.com',
            'PORT': 5432,
            'TEST': {
                'NAME': 'd7osdssadag0ugv5', #This is an important entry
            }
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```

All bugs found during the development process have been fixed and as such I have not encountered any new ones since submission.... fingers crossed!