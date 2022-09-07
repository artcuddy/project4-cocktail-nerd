<a href="https://enigma-code-breaker.herokuapp.com/" target="_blank"><img src="documentation/readme_images/logo/cocktail-nerd-logo-white.webp"></a><br />
<h2>Your expert cocktail guide, featuring hand-selected cocktail recipes.<br />
Find great new drinks to try plus helpful tips and advice.</h2>
<br />

## Contents
<ul>
    <li>
        <a href="#introduction"><strong>Introduction</strong></a>
    </li>
    <li>
        <a href="#ux"><strong>UX</strong></a>               
    </li>
     <li>
        <a href="#features"><strong>Features</strong></a>
    </li>
    <li>
        <a href="#technologies"><strong>Technologies</strong></a>
    </li>
     <li>
        <a href="#testing"><strong>Development & Testing</strong></a>   
    </li>
    <li>
        <a href="#deployment"><strong>Deployment</strong></a>
    </li>
    <li>
       <a href="#credits"><strong>Credits</strong></a> 
    </li>
</ul>
<hr>
<h2 id="introduction">Introduction</h2>

Cocktail Nerd - is full stack Django project that runs on Heroku.

The site allows staff users to edit posts, categories and comments from the frone=tend once logged in & registered users can login to comment and like posts.

## Demo
A live version of the site can be found <a href="https://enigma-code-breaker.herokuapp.com/" target="_blank">**HERE**</a><br><br>
<img src="documentation/readme_images/screenshots/cocktail-nerd-responsive-screenshot.webp"><br><br>
<a href="#top">Back to the top.</a>


<h2 id="future-features">Possible Future Features</h2>

* Features go here  


<h2 id="technologies">Technologies</h2>

<a href="#top">Back to the top.</a>

Throughout the planning, design, testing and deployment of the Cocktail Nerd Website , I have used a number of technologies:

### Languages
<ol>
    <li><a href="https://en.wikipedia.org/wiki/HTML5" target="_blank">HTML</a>
        <ul><li>The main structure of the game container</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a>
        <ul><li>Within the base template by code institute</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">Python</a>
        <ul><li>For the gameplay logic</li></ul>
    </li>
    <li><a href="https://www.markdownguide.org/" target="_blank">Markdown</a>
        <ul><li>For the content and structure of the README.md</li></ul>
    </li>
</ol>   

### Version Control
<ol>
    <li><a href="https://github.com/" target="_blank">Git & Github</a>
        <ul><li>For the hosting and version control of the ENIGMA game</li></ul>
    </li>
    <li><a href="https://www.gitpod.io/" target="_blank">Gitpod</a>
        <ul><li>The development environment used for writing the code for the ENIGMA game</li></ul>
    </li>
</ol>


### Applications    
<ol>
   <li><a href="https://lucid.app/" target="_blank">Lucid Chart</a>
        <ul><li>For the creation of the flowchart</li></ul>
    </li>
    <li><a href="https://visualstudio.microsoft.com/" target="_blank">Visual Studio (Desktop)</a>
        <ul><li>For testing out different code strategies without interfering with code for the ENIGMA Game</li></ul>
    </li>
    <li><a href="https://slack.com/intl/en-gb/" target="_blank">Slack (Desktop)</a>
        <ul><li>For communicating with fellow students and troubleshooting problems with the different environments used during the course and solving coding issues.</li></ul>
    </li>
</ol>
    
## Frameworks, Libraries and Programs


<ol> 
    <li><a href="https://docs.python.org/3/library/time.html" target="_blank">Python time library</a>
        <ul>Used to delay the next line of text in the python terminal</ul>
    </li>
    <li><a href="https://pypi.org/project/termcolor/" target="_blank">Python termcolor library</a>
        <ul>Used to add colour to the text in the python terminal</ul>
    </li>
    <li><a href="http://pep8online.com/checkresult" target="_blank">PEP8 ONLINE</a>
        <ul><li>To test and search for errors in the Python code</li></ul>
    </li>
    <li><a href="https://developers.google.com/web/tools/lighthouse" target="_blank">Lighthouse</a> Performance Tool
        <ul><li>To ensure high performance and quick loading times of the ENIGMA game</li></ul>
    </li>
</ol><br> 

<h2 id="testing">Development & Testing</h2>

<a href="#top">Back to the top.</a>


### Flow Chart



## Validator Testing


* <a href="https://developers.google.com/web/tools/lighthouse" target="_blank">Lighthouse</a> Performance Tool

<img src="documentation/readme_images/testing/lighthouse-testing.webp"><br><br>


<h2 id="deployment">Deployment</h2>

<a href="#top">Back to the top.</a>

### This project was created on GitHub and Edited in GitPod by carrying out the following:

<ol>
    <li>A new repository was created using 'Code-Instutute-Org/python-essentials-template'</li>
    <li>A meaningful name was given to my new repository and I selected 'Create Repository'</li>
    <li>I then opened the repository on GitHub and clicked the 'Gitpod' button to build the GitPod workspace which would allow me to build and edit the code used to make the <em>Star Trek Time Loop</em> website/game</li>
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

The project was deployed via <a href="https://id.heroku.com/login" target="_blank">Heroku</a>, and the live link can be found here: <a href="https://enigma-code-breaker.herokuapp.com/" target="_blank">ENIGMA – Code Breaker</a>

This project was developed utilising the <a href="https://github.com/Code-Institute-Org/python-essentials-template" target="_blank">Code Institute Template</a>. Some of the deployment steps below are specifically required for the new CI template and may not be applicable to older versions, or different projects.

Before deploying to Heroku pip3 freeze > requirements.txt was used to add pyfiglet and termcolor imports for deployment.

This project was deployed to Heroku using the Heroku CLI details below

* Login
To use the CLI you must log in to your Heroku account. To do this you will need to
enter the command heroku login -i in the terminal. It requires the email and
password you used to sign up. If you have enabled multi-factor authentication (a
recommended security practice) then instead of your password you need an API key.
To get the API key go to your account settings and scroll down to the section ‘API
Key’. Click reveal and copy that, then paste it into the password prompt.

<img src="assets/screenshots/heroku-login-cli.jpg"><br><br>

* Creating A Heroku App
Now that you are logged in, the first thing is to create a new app. Heroku creates a
URL based on your app name, so it must be unique not only on your account, but
across the whole site. You may need to try a few different names. To create an app
use the following command, where myapp is the name of your app.

<img src="assets/screenshots/creating-heroku-app.jpg"><br><br>

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
    <li>Navigate to the repository <a href="https://github.com/artcuddy/project3-enigma" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Fork' button in the top right corner of the page (under your account image)</li>
    <li>The repo has now been copied into your own repos and you can work on it in your chosen IDE</li>
    <li>If you have any suggestions to make regards to the code to make the site better, you can put in a pull request</li>
</ol>

#### Cloning the repo with GitPod
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project3-enigma" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Ensure HTTPS is selected and click the clipboard on the right of the URL to copy it</li>
    <li>Open a new workspace in GitPod</li>
    <li>In the bash terminal type 'git clone [copy url here from step 4]'</li>
    <li>Press enter - the IDE will clone and download the repo</li>
</ol>

#### Github Desktop
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project3-enigma" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Open with GitHub Desktop'</li>
    <li>If you haven't already installed GitHub desktop application - you will need to follow the relevant steps to do this</li>
    <li>The repo will then be copied locally onto your machine</li>
</ol>

#### Download and extract the zip directly from GitHub
<ol>
    <li>Log in to your GitHub account</li>
    <li>Navigate to the Repository <a href="https://github.com/artcuddy/project3-enigma" target="_blank"><strong>HERE</strong></a></li>
    <li>Select the 'Code' button above the file list on the right had side</li>
    <li>Select 'Download Zip'</li>
    <li>Once you have the Zip downloaded, open it with your prefered file decompression software</li>
    <li>You can then drag and drop the files from the folder into your chosen IDE or view/edit them on your local machine</li>
    <li>If you want to create a web-app from the repo please follow the instructions in "Project Deployment"</li>
</ol>


<h2 id="credits">Credits</h2>

<a href="#top">Back to the top.</a>

I have listed some of the resources I used for inspiration and in researching how to create the Cocktail Nerd Website

* Mastermind Game with Python: Tutorial: <a href="https://www.youtube.com/watch?v=NLfxNo7Q0Pk" target="_blank">Youtube</a>


These resources helped me solve some of the issues encountered when developing the site

* How to use Pyfiglet to display the game Heading & Subheading <a href="https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/" target="_blank">Pyfiglet</a>


<a href="#top">Back to the top.</a>

<h2 id="acknowledgements">Acknowledgements</h2>

This project was made possible due to the help & advice from my Mentor Rohit, Code Institute Slack community, Stack Overflow community and a lot of extensive Googling.
