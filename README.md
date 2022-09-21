<a id="top" href="https://enigma-code-breaker.herokuapp.com/" target="_blank"><img src="documentation/readme_images/logo/cocktail-nerd-logo-white.webp"></a><br />
<h2>Your expert cocktail guide, featuring hand-selected cocktail recipes.<br />
Find great new drinks to try plus helpful tips and advice.</h2>
<br />

<h1 id="contents">Contents</h1>

- [Introduction](#Introduction)
 - [User Experience - UX](#user-experience)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
- [Design](#design)
    - [Database](#database)
    - [Wireframes](#wiresframes)
- [Features](#features)
    - [Future Features](#future-features)
- [Technologies](#technologies)
    - [Languages](#languages)
    - [Version Control](#version-control)
    - [Applications](#applications)
    - [Frameworks & Libraries](#frameworks)
- [Development & Testing](#testing)
    - [Database](#database)
    - [Testing Results](TESTING.md)
    - [Test Case](TESTCASE.md)
- [Deployment](#deployment)
- [Credits](#credits)

<h1 id="introduction">Introduction</h1>

Cocktail Nerd - is full stack Django project that runs on Heroku.

The site allows staff users to edit posts, categories and comments from the frontend once logged in & registered users can login to comment,like & rate cocktail recipes.

<h1 id="demo">Demo</h1>
A live version of the site can be found <a href="https://project4-cocktail-nerd.herokuapp.com/" target="_blank">**HERE**</a><br><br>
<img src="documentation/readme_images/screenshots/cocktail-nerd-responsive.webp"><br><br>

<h1 id="user-experience">User Experience - UX</h1>

<a href="#top">Back to the top.</a>

<h2 id="user-stories">User Stories</h2>

* As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of cocktail recipes and choose accordingly.
3. Search cocktail recipes to find specific recipes.
4. Click on post to read the cocktail recipe details.
5. Register for an account to like, rate or comment on a cocktail recipe.
6. View the number of likes on a cocktail recipe.
7. View comments on cocktail recipes so that I can read other users opinions.

* As logged in website user, I can:

1. Like/unlike cocktail recipes and view them on a single liked cocktails page.
2. Comment on cocktail recipes and give my opinion about the posts.
3. Delete or edit my previous comments.
4. Manage my profile by updating my details and user image.

* As a website staffuser, I can:

1. Create and publish a new cocktail recipe.
2. Create draft recipe posts that can be reviewed and finalised later.
3. Create a new user, cocktail recipes and cocktail categories.
4. Delete a user, cocktail recipes, cocktail categories and comments.
5. Approve user's comments.
6. Change the website permissions for a user.

<h2 id="agile-methodology">Agile Methodology</h2>

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board which can be seen here -  <a href="https://github.com/users/artcuddy/projects/2" target="_blank"> Cocktail Nerd </a>

Through the use of the Kanban board in the projects view in Github, the project was divived into a few different sections:
* Addons
* Todo
* In Progress
* Done

![Kanban board github](documentation/readme_images/screenshots/git-hub-kanban-board.webp)

Github issues were used to create User Stories and any other fixes or updates for the project. This was where the project user was assigned, labels were added to provide clarity, and the story was added to the appropriate sprint and the project. Each User Story, Fix or Update had a clear title. 

Milestones were used to create sprints. There were 3 sprints each dated appropriately. User Stories were completed based on the current sprint in progress. Each sprint was completed on time.

The Github issues were not just used to record User Stories but also used to record any bug fixes or updates to the codebase as well.

<br>
<h2 id="the-scope">The Scope</h2>

* To provide users with a good clean experience when using the Cocktail Nerd website.
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
* To provide a website with a clear purpose.
* To provide role-based permissions that allows user to interact with the website example: like, comment or rate a cocktail.
* To provide search functionality to find cocktails on the Cocktail Nerd site.

<br>

<h1 id="features">Features</h1>

<a href="#top">Back to the top.</a>

## Homepage

* The Home Page is the landing page of the website and that's visible first when the site loads. It is designed to allow the user to quickly find their way around the site.

<img src="documentation/readme_images/screenshots/homepage.webp">

## Navigation Desktop

* The site navigation is done through the navigation bar at the top of each page & this is consistant throughout the website.

* The navigation bar at the top of each page is sticky to allow access to the navigation at any time.

* Options on the navigation bar change depending on whether the user is logged in or not, or is an admin/staffuser or not.

* Navigation menu when nobody is logged in only options are login or sign-up.
<img src="documentation/readme_images/screenshots/navbar/nav-menu-not-signed-in.webp">

* Navigation menu when regular authenticated user is logged in no access to Admin or Dashboard menu.
<img src="documentation/readme_images/screenshots/navbar/reguser-logged-in.webp">

* Navigation menu when staffuser user is logged in has access to the Admin menu but not the Dashboard menu.
<img src="documentation/readme_images/screenshots/navbar/staffuser-logged-in.webp">

* Navigation menu when admin user is logged in has access to the Admin menu & the Dashboard menu.
<img src="documentation/readme_images/screenshots/navbar/admin-logged-in.webp">

## Navigation Mobile

* Navigation menu when nobody is logged in only options are login or sign-up.
<br>
<img src="documentation/readme_images/screenshots/mobile/mobile-nobody-logged-in.webp">

* Navigation menu when regular authenticated user is logged in no access to Admin or Dashboard menu.
<br>
<img src="documentation/readme_images/screenshots/mobile/mobile-reguser-logged-in.webp">

* Navigation menu when staffuser user is logged in has access to the Admin menu but not the Dashboard menu.
<br>
<img src="documentation/readme_images/screenshots/mobile/mobile-staffuser-logged-in.webp">

* Navigation menu when admin user is logged in has access to the Admin menu & the Dashboard menu.
<br>
<img src="documentation/readme_images/screenshots/mobile/mobile-admin-logged-in.webp">

## Liked Cocktails

* When an authenticated user likes a cocktail this will be added to their liked posts page which can be accessed by clicking on the heart icon on the navbar.
<br>
<img src="documentation/readme_images/screenshots/liked-cocktails.webp">

## All Cocktails

* To see all cocktails on a paginated page click the cocktails menu or button on the homepage
<br>
<img src="documentation/readme_images/screenshots/all-cocktails.webp">

<h2 id="future-features">Possible Future Features</h2>

* Social login to allow the user to signup using Facebook or Google 

* Password reset on the users profile page

* Allowing users to post their own cocktail recipes 

<br>
<h1 id="technologies">Technologies</h1>

<a href="#top">Back to the top.</a>

Throughout the planning, design, testing and deployment of the Cocktail Nerd Website , I have used a number of technologies:

<h2 id="languages">Languages</h2>
<ol>
    <li><a href="https://en.wikipedia.org/wiki/HTML5" target="_blank">HTML</a>
        <ul><li>The main structure of the site</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a>
        <ul><li>Within the base template by code institute</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">Python</a>
        <ul><li>For the site logic</li></ul>
    </li>
     <li><a href="https://www.djangoproject.com/" target="_blank">Django</a>
        <ul><li>For the site templating and structure</li></ul>
    </li>
    <li><a href="https://www.markdownguide.org/" target="_blank">Markdown</a>
        <ul><li>For the content and structure of the README.md</li></ul>
    </li>
</ol>   

<h2 id="version-control">Version Control</h2>
<ol>
    <li><a href="https://github.com/" target="_blank">Git & Github</a>
        <ul><li>For the hosting and version control of the Cocktail Nerd site.</li></ul>
    </li>
    <li><a href="https://www.gitpod.io/" target="_blank">Gitpod</a>
        <ul><li>The development environment used for writing the code for the Cocktail Nerd site.</li></ul>
    </li>
</ol>


<h2 id="applications">Applications</h2>   
<ol>
<li><a href="https://www.heroku.com/" target="_blank">Heroku</a>
        <ul><li>For the application hosting</li></ul>
    </li>
   <li><a href="https://lucid.app/" target="_blank">Lucid Chart</a>
        <ul><li>For the creation of the flowchart</li></ul>
    </li>
    <li><a href="https://visualstudio.microsoft.com/" target="_blank">Visual Studio (Desktop)</a>
        <ul><li>For testing out different code strategies without interfering with the code of the Cocktail Nerd site.</li></ul>
    </li>
    <li><a href="https://slack.com/intl/en-gb/" target="_blank">Slack (Desktop)</a>
        <ul><li>For communicating with fellow students and troubleshooting problems with the different environments used during the course and solving coding issues.</li></ul>
    </li>
</ol>
    
<h2 id="frameworks">Frameworks, Libraries and Programs</h2> 

<ol> 
    <li><a href="https://getbootstrap.com/docs/5.0/getting-started/introduction/" target="_blank">Bootstrap 5</a>
        <ul><li>As the base HTML5 and CSS </li></ul>
    </li>
    <li><a href="http://pep8online.com/" target="_blank">PEP8 ONLINE</a>
        <ul><li>To test and search for errors in the Python code</li></ul>
    </li>
    <li><a href="https://developers.google.com/web/tools/lighthouse" target="_blank">Lighthouse</a> Performance Tool
        <ul><li>To ensure high performance and quick loading times of the Cocktail Nerd site</li></ul>
    </li>
</ol><br> 

<h1 id="testing">Development & Testing</h1>

<a href="#top">Back to the top.</a>

<h2 id="database">Database</h2>

* Flow chart to go here

<br> 

<h2 id="testing-results">Testing Results</h2>

* Testing results [here](TESTING.md)

<h2 id="testing-results">Manual Test Case</h2>

* Test case results [here](TESTCASE.md)


<br>
<h1 id="deployment">Deployment</h1>

<a href="#top">Back to the top.</a>

### This project was created on GitHub and Edited in GitPod by carrying out the following:

<ol>
    <li>A new repository was created using 'Code-Instutute-Org/python-essentials-template'</li>
    <li>A meaningful name was given to my new repository and I selected 'Create Repository'</li>
    <li>I then opened the repository on GitHub and clicked the 'Gitpod' button to build the GitPod workspace which would allow me to build and edit the code used to make the <em>Cocktail Nerd</em> website.</li>
    <li>Version control was used throughout the project using the following commands in the terminal using Bash
        <ul>
            <li>git add . <strong>OR</strong> git add "file name" - to stage the changes and get them ready for being committed to the local repo.</li> 
            <li>git commit -m "Description of the update" - to save the change and commit the change to the local repo</li>
            <li>git push - to push all committed changes to the GitHub</li>
            <li>commit --amend - for changing the wording or spelling of the most recent commit</li>
            <li>git reset "commit hash" </li>
            <li>git push -f - This was used to force changes through to the GitHub repo if either "commit --amend" or "git reset" were used</li>
        </ul>
    </li>


### Heroku

The project was deployed via <a href="https://id.heroku.com/login" target="_blank">Heroku</a>, and the live link can be found here: <a href="https://project4-cocktail-nerd.herokuapp.com/" target="_blank">Cocktail Nerd</a>

This project was developed utilising the <a href="https://github.com/Code-Institute-Org/python-essentials-template" target="_blank">Code Institute Template</a>. Some of the deployment steps below are specifically required for the new CI template and may not be applicable to older versions, or different projects.

Before deploying to Heroku pip3 freeze > requirements.txt was used to add all dependencies for deployment.

This project was deployed to Heroku using the Heroku CLI details below

* Login
To use the CLI you must log in to your Heroku account. To do this you will need to
enter the command heroku login -i in the terminal. It requires the email and
password you used to sign up. If you have enabled multi-factor authentication (a
recommended security practice) then instead of your password you need an API key.
To get the API key go to your account settings and scroll down to the section ‘API
Key’. Click reveal and copy that, then paste it into the password prompt.
<br> 
<img src="documentation/readme_images/screenshots/heroku-login-cli.jpg"><br><br>

* Creating A Heroku App
Now that you are logged in, the first thing is to create a new app. Heroku creates a
URL based on your app name, so it must be unique not only on your account, but
across the whole site. You may need to try a few different names. To create an app
use the following command, where myapp is the name of your app.
<br> 
<img src="documentation/readme_images/screenshots/creating-heroku-app.jpg"><br><br>

* Here the app heroku-cli-example has been created with an output of the website
URL. It also displays and sets the git remote repository which will be used to deploy.
By default the region will be set to the US. If you would prefer a server based in the
EU then you can specify the region with the flag EU

* Packages
* When you push code to Heroku it will look at the repository contents to decide how
to build the project. One of the factors taken into consideration is the package file.
With a Python project the standard file is a requirements.txt file, which will have the
list of packages needed to run the project. If this file is present it will build the project
using the Python buildpack.
<br><br>
* It is also possible to specify the buildpack manually. More information about
buildpacks can be found in the documentation. To check the buildpack for the
project you can enter heroku buildpacks in the terminal.

* Click **Enable Automatic Deploys** for automatic deployment when you push updates to Github.

* Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.


### Github Local Deployment
There are many ways to deploy the project locally on your own device. Forking, Cloning, GitHub Desktop and Zip Exctraction, the steps in these processes are outlined below:

#### Forking the GitHub repo
If you want to make changes to the repo without affecting it, you can make a copy of it by 'Forking' it. This will make sure that the original repo remains unchanged.

<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the repository <a href="https://github.com/artcuddy/project4-cocktail-nerd" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Fork' button in the top right corner of the page (under your account image)</li>
    <li>The repo has now been copied into your own repos and you can work on it in your chosen IDE</li>
    <li>If you have any suggestions to make regards to the code to make the site better, you can put in a pull request</li>
</ol>

#### Cloning the repo with GitPod
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project4-cocktail-nerd" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it</li>
    <li>Open a new workspace in GitPod</li>
    <li>In the bash terminal type 'git clone [copy url here from step 4]'</li>
    <li>Press enter - the IDE will clone and download the repo</li>
</ol>

#### Github Desktop
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project4-cocktail-nerd" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Open with GitHub Desktop'</li>
    <li>If you haven't already installed GitHub desktop application - you will need to follow the relevant steps to do this</li>
    <li>The repo will then be copied locally onto your machine</li>
</ol>

#### Download and extract the zip directly from GitHub
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project4-cocktail-nerd" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Download Zip'</li>
    <li>Once you have the Zip downloaded, open it with your prefered file decompression software</li>
    <li>You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>

<br>
<h1 id="credits">Credits</h1>

<a href="#top">Back to the top.</a>

I have listed some of the resources I used for inspiration and in researching how to create the Cocktail Nerd Website

* Lists to go here


These resources helped me solve some of the issues encountered when developing the site

* Resourses to go here

<h2 id="acknowledgements">Acknowledgements</h2>

This project was made possible due to the help & advice from my Mentor Rohit, Code Institute Slack community, Stack Overflow community and a lot of extensive Googling.
