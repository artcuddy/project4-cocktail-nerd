# Cocktail Nerd Testing
Back to the [README](README.md)

* Testing has taken place continuously throughout the development of the project. Each view was tested regularly adn dployed early to Heroku to confirm local and remote functioned the same.  

### Python Validation - PEP8
* Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files
were entered into the online checker and no errors were found in any of the Cocktail Nerd custom code.

#### Cocktail Nerd - cocktailapp
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


## Lighthouse
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


### Console Results:

### Desktop
![Desktop Dev Console Result](documentation/readme_images/testing/desktop-dev-console.webp)
* The browser console is clean, no errors are  showing.

### Mobile
![Mobile Dev Console Result](documentation/readme_images/testing/mobile-dev-console.webp)
* The browser console is clean, no errors are  showing.

## Manual Testing
### Frontend
* The Signup, Login and Logout system is working as it should. It shows the right interactive message to the users on Signup, Login and Logout.
<br>

![Login Success](documentation/readme_images/testing/auth/success-login.webp)

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

* The All Cocktails Page shows all the cocktail recipes. The pagination system is workin, it adds another page when more than 6 cocktails on the page.

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


* The functionality to update a comments, previously sent by the user is 
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

## Backend/Admin Panel
* I have tested the Admin Panel repeatedly since the start of the project. All the models are working without issues.  
  I have created, deleted, and updated data in all models without errors. The models have the behavior expected for what they were built for.
* Whenever a user comments on a cocktail the Superuser has to approve it before it will be displayed on the website. This functionality is 
  working without issues.
* When the staffuser/superuser is publishing a new cocktail recipe all the required fields have to be filled otherwise the author can't submit the post to the database.


## Bugs
* All bugs found during the development process have been fixed and as such I have not encountered any new ones since deployment.... fingers crossed!