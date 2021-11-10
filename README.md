# Fitness Master

![GitHub contributors](https://img.shields.io/github/contributors/alexandergrib/studious-guacamole)
![GitHub last commit](https://img.shields.io/github/last-commit/alexandergrib/studious-guacamole)
![GitHub language count](https://img.shields.io/github/languages/count/alexandergrib/studious-guacamole)
![GitHub top language](https://img.shields.io/github/languages/top/alexandergrib/studious-guacamole)
![Font Awesome version](https://img.shields.io/badge/Font%20Awesome-v5.15.1-blue)
![Total lines](https://img.shields.io/tokei/lines/github/alexandergrib/studious-guacamole)

# Positively Pink

<brief about the project>

## Contents
<p align="center">
  <img width="40%" src= "screenshots/screen_shot.png">
</p>
 
<p align="center"><a href= 'https://positively-pink.herokuapp.com/' target = "_blank">
Positively Pink</a></p>
 
## Table of Contents
 
- [About](#About)
- [User Experience (UX)](#User-Experience-(ux))
  - [User Stories](#User-Stories)
  - [UI](#ui)
  - [Design](#Design)
  - [Database Schema](#database-schema)
  - [Database Model](#database-model)
  - [Wireframes](#Wireframes)
- [Features](#Features)
    - [Future features](#Future-updates)
- [Technologies used](#Technologies-used)
- [Testing](#Testing)
    - [Manual testing](#Testing)
- [Errors](#Errors)
- [Code Notes](#Code-Notes)
- [Deployment](#Deployment)
- [Credits](#Deployment)
    - [Code](#Code)
     - [Images](#Images)
- [Acknowledgements](#Acknowledgements)

---
## About

Bla bla bla bla

---

## User Experience (UX)

### User Stories

#### As a first time user I want to:

*
*
*


#### As a returning user I want to:

*
*



#### As an owner of the website I want to:

*
*

### UI
*
*
*



### Design
*
*

### Wireframes
WWireframes are my initial design, so you may notice that the final website design does not contain everything that was planned at the start of the project. Some missing features are possible future improvements for the project. They may be implemented at a later stage.
  * [wireframes.pdf]

### Database Schema

I started planning the database after I have done my wireframes to justify which fields I would require and what collections I would have to use. After the initial discussion with my mentor, I have settled with the current database schema.
 * [Database schema] screenshot

### Database Model

  * screenshots


#### CRUD

HTTP Verb | URL PATH | PURPOSE
| --- | --- | --- |
GET | /<url> | <description>
POST | /<url>/create | <description>
POST | /<url>/edit/<:id> | <description>
DELETE | /<url>/delete/<:id> | <description>



---

## Features

1.
2.
3.
4.



###  Future updates
1.
2.


---
 
## Technologies used

Below I have listed the programming languages, technologies, frameworks and resources used for this project.
 
* **HTML5**
* **CSS3**
* **Vanilla JS**
* **J Query**
* **Markdown**
* **Git** for version control.
* **Github** to hold my project.
* **Heroku** to deploy my project to the web.
* **Flask**
* **MongoDB**
* **Google Chrome/FireFox/Edge/Safari** 
* **Developer tools for chrome/FireFox/Edge**
* **[Amiresponsive](http://ami.responsivedesign.is/)**
* **[Balsamiq](https://balsamiq.com/)** to create wireframes.
* **[W3Schools](https://www.w3schools.com/)** for help with some issues I ran into
* **[StackOverFlow](https://stackoverflow.com/)** for help with some issues I ran into
* **Mentor** my code institute mentor for advice
* **[Slack](https://slack.com/)** specifically the code institute room in slack.
* **[Grammarly](https://www.grammarly.com/)** to correct grammar and spelling mistakes.
* **[Charts CSS](https://chartscss.org/)** to display charts for each workout completed
* **[animate.style](https://animate.style/)** to display animations

---

## Testing

* [HTML validator](https://validator.w3.org/#validate_by_input)
  * [No issues](readme_screenshots/html_validator.png)
* [CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
 
* [JsHint](https://jshint.com)

* Testing [checklist](https://geteasyqa.com/qa/test-website/)
* [pep8](http://pep8online.com/)

I personally tested the website on some of my own personal systems of which include:
1. Windows10 Google Chrome, Mozilla, Edge browsers
2. [https://www.webpagetest.org/](https://www.webpagetest.org/) To test for errors and performance 

      


### Manual testing

---
<details>
<summary>
Detail testing
</summary>
1
2
3
No automated testing was conducted.
</details>

---

<details>
<summary>
User stories testing
</summary>
1.
2.
3.
</details>

---

### Errors
<details>
<summary>
Current errors:
</summary>
1.
2.
3.

</details>

---

## Code Notes

---

## Deployment

<details>
<summary>
Deployment
</summary>

To deploy this project I used [Heroku](https://dashboard.heroku.com/)

**The final version of the application was deployed using Heroku:**   
**[here](https://fitness-master.herokuapp.com/)**

The deployed version is the same version as in the repository.

The following steps were used for deployment on Heroku:

1. In Gitpod CLI, in the root directory of the project, run 

   `pip3 freeze --local > requirements txt`

   to create a `requirements.txt` file containing project dependencies.

2. In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'.  
   Open the Procfile. Inside the file, enter:  

   `web: python3 app.py`

    Save the file.

3. **Make sure you do a Git commit after creating the requirements.txt and the Procfile.**

4. On [Heroku](https://www.heroku.com/), sign in using your username and password.

5. On Heroku Dashboard, press the "New" button, then select "Create new app".

6. Enter the name of your app and select your region.   
   Press "Create app".

7. On Heroku App Dashboard, select the Settings tab.

    Under "App information", copy the Heroku git URL.

8. In Gitpod workspace CLI, in the project's root directory, enter  

    `heroku login`   

    Follow the instructions to login.

    Enter 

    `git remote add heroku <Heroku Git URL>`

    where `<Heroku Git URL>` is the Heroku git URL copied from the Heroku App Dashboard in Settings (step 7 above).

    Finally, enter

    `git push heroku master`

    to push the contents of your local Git repository to the newly created Heroku remote repository.

9. Still in the Gitpod workspace CLI, enter 

     `heroku ps:scale web=1`
        
     to start the Heroku web process.

10. Log into your [MongoDB Atlas](https://account.mongodb.com/account/login) account.   

    In the dashboard, select your database Cluster, then click the Connect button.

    In the pop-up, select the option "Connect your application". 

    Under the tab "Connection string only", copy the connection string.

11. Login into [Cloudinary](https://cloudinary.com/) account.
    
    In the dashboard copy your cloud name, API key and API Secret

12. On Heroku App Dashboard, in the Settings tab, click the button "Reveal Config vars".

    Using the Add button, add the following keys and their corresponding values:

    key: `IP`  
    value: `0.0.0.0`

    key: `PORT`   
    value: `5000`   
    
    key: `MONGO_URI`   
    value:   
    - paste the string copied from MongoDB,
    - inside the pasted string, replace `<password>` with your database access password (**NOT** your MongoDB login password),
      ensure you remove the `<>`.
    - replace `test` with the name (case-sensitive!) of the database used for your project.

    key: `SECRET_KEY`   
    value: value of SECRET_KEY as entered into the project's env.py file, **without quotes** . 

13. Whilst in the "Config vars" section add the rest of the required [Cloudinary](https://cloudinary.com/) requirements.
    
    key:cloud_name
    value: <your cloud name>

    key: api_key
    value:  "<api value>"

    key: api_secret
    value:  "<secret value>"

14. In the top right corner of the Heroku App Dashboard, click on the More button.

    From the dropdown menu, select "Restart all dynos". Confirm Restart when prompted. 

15. Click on Open app. The App is now deployed.
</details>

### Local Deployment
<details>
<summary>
If you want to run this project locally, you will need to follow these steps.
</summary>

1. Clone or download this repository.

2. Upload the repository into your IDE of choice.  

I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE.

3. In your workspace CLI, run

   `pip3 install -r requirements.txt`

   to install the project-required dependencies.

4. In the root directory of your project, create an env.py file. 

   Don't forget to add the env.py file to your .gitignore file.

5. In MongoDB Atlas, create a new database for the project.

6. Once you have created the database, go back to the Cluster View and click "Connect".
    In the resulting pop-up, click on "Connect your application".
    Under the tab "Connection String Only", copy the connection string.

7. Back in your IDE, open the env.py file.

   At the top of the file, add 

   `import os`

   Then, add 

   `os.environ["MONGO_URI"] = "<mongo_uri>"`
    
    where `<mongo_uri>` is the pasted MongoDB connection string copied in step 6 above.

   In the pasted `<mongo_uri>` string:
   - replace < password > with your database access password (**NOT** your MongoDB login password), and
   - replace "test" with the name (case-sensitive!) of your project database. 

   Finally, add

   `os.environ["SECRET_KEY"] = "<your_secret_key>"`

    where `<your_secret_key>` is a combination of letters, numbers and characters of your choice. This is used to enable the Flask flash messaging feature.

    

8. Login into [Cloudinary](https://cloudinary.com/) account.
    
    In the dashboard copy your cloud name, API key and API Secret
    
    Add them to your env.py
   1. `os.environ["cloud_name"] = "<your_cloud_name>"`
   2. `os.environ["api_key"] = "<your_api_key>"`
   3. `os.environ["api_secret"] = "<your_api_secret>"`
   
    Save the file.

9. Run the app.py file and open it in your browser.   
    The application is now running locally.
</details>


---

## Credits
### Code

   * Animations are done with help of [animate.style](https://animate.style/)
   * Website built based on 


### Images

* [Google-Images](https://www.google.com/imghp?hl=en)
* [https://unsplash.com/](https://unsplash.com/)
* [image placeholders](https://placehold.it/250x250)

---


## Acknowledgements
*
*
*

[Back to top ↑](#fitness-master)

