# Cocktail Nerd Testing
Back to the [README](README.md)

Testing has taken place continuously throughout the development of the project. The app was tested regularly and deployed early to Heroku to confirm local and remote functioned the same. 


<h2 id="automated-testing-results">Automated Testing Results</h2>

Due to the nature of the Postgres database being offered by Heroku and the way tests are run in Django, I encounterd an error while trying to run tests on my Django application with Heroku Postgres Add-on connected to the application.
<br>
Attempting to run the testing command results in this error
<br>
* Got an error creating the test database: permission denied to create database
<br>
To get this to work I created an additional Postgres database as an add-on and used this as my testing database.
<br>
Also added an if 'test' in sys.argv: to the database settings in my project to connect to the test database when testing and an else statement to conncet to the production databse when not.

### Before Automated testing coverage was at 79%
<br>

![admin.py](documentation/readme_images/testing/before-automated-tests.webp)

### After Automated testing coverage is at 93%

Once the testing had been setup I was able to get the total automated test coverage up to 93%.
<br>
This could be improved on of course to get o 100% coverage and is something I could look at completing over time.

![admin.py](documentation/readme_images/testing/after-automated-tests.webp)

<br>
<h2 id="manual-testing-results">Manual Testing Results</h2>

<details> <summary> Manual Test Case can be found here.</summary>

![Manual Test Case](documentation/readme_images/testing/cocktail-nerd-manual-testing.webp)

</details>

<br>

# Frontend
<br>
* The Signup, Login and Logout system is working as it should. It shows the right interactive message to the users on Signup, Login and Logout.
<br>

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

<br>

# Backend/Admin Panel
* I have tested the Admin Panel repeatedly since the start of the project. All the models are working without issues.  
* Posts can be filtered by status, date, category or if featured or not
* Whenever a user comments on a cocktail the Superuser has to approve it before it will be displayed on the website. This functionality is 
  working without issues.
* When the staffuser/superuser is publishing a new cocktail recipe all the required fields have to be filled otherwise the author can't submit the post to the database.
<br>

![Django Admin Dashboard](documentation/readme_images/testing/django-admin-dashboard.webp)

<br>

# Python Validation - PEP8
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

<br>

# Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop and Mobile.

### Desktop Results:
![Lighthouse Mobile Result](documentation/readme_images/testing/lighthouse-desktop.webp)

### Mobile Results:
![Lighthouse Desktop Result](documentation/readme_images/testing/lighthouse-score.webp)

### HTML Validation
![HTML Validation Result](documentation/readme_images/testing/html-validator-results.webp)

### CSS Validation

![W3C CSS Validation Result](documentation/readme_images/testing/css-validator-results.webp)

* Custom CSS was validated using W3C Jigsaw validation service. One warning was displayed, however, 
  this is related to Bootstrap 5 which will not affect the CSS performance.


# Console Results:

### Desktop
![Desktop Dev Console Result](documentation/readme_images/testing/desktop-dev-console.webp)
* The browser console is clean, no errors are  showing.

### Mobile
![Mobile Dev Console Result](documentation/readme_images/testing/mobile-dev-console.webp)
* The browser console is clean, no errors are  showing.

<br>


# Bugs
* All bugs found during the development process have been fixed and as such I have not encountered any new ones since submission.... fingers crossed!