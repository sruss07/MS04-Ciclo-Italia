<h1 align=center id=top> Ciclo Italia </h1>

# Project Overview

Ciclo Italia is an online bike store offering a selection of the finest Italian designed road racing bikes!
Offering the best quality bikes from iconic Italian brands, Bianchi, Cinelli, Colnago, De Rosa , Pinarello and Wilier

<h2 align=center id="top"><img src="docs/Ciclo_Italia_responsive_screen_views.png"></h2>

View live project [here](https://ciclo-italia.herokuapp.com/) 

# Table of Contents

**<details><summary>[User Experience (UX)](#user-experience-ux)</summary>**

- [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
  - [Existing Features](#existing-features)
  - [Future Features to Implement](#future-features-to-implement)
- [Structure](#structure)
- [Database](#database)
- [Data Schema](#data-schema)
- [Skeleton](#skeleton)
- [Wireframes](#wireframes)
- [Surface](#surface)
  - [Colours](#colours)
  - [Typography](#typography)
  - [Animations](#animations)

  </details>

**<details><summary>[Technologies Used](#technologies-used)</summary>**

- [Languages](#languages)
- [Integration](#integration)
- [Dependencies](#dependencies)
- [Tools](#tools)
- [IDE Extensions](#ide-extensions)
- [Code Validity](#code-validity)

</details>

**<details><summary>[Bugs/Issues](#bugs)</summary>**

- [Project barriers and solutions](#project-barriers-and-solutions)
- [Known Issues](#known-issues)

</details>

**<details><summary>[Workflow](#workflow)</summary>**

- [Version Control](#version-control)
- [Development Environment](#development-environment)

</details>

**<details><summary>[Deployment](#deployment)</summary>**
</details>

**<details><summary>[Testing](#testing)</summary>**
</details>

**<details><summary>[Credits](#credits)</summary>**

- [Resources](#resources)
- [Media](#media)
- [Content](#content)
- [Code Snippets](#code-snippets)
- [Acknowledgments](#acknowledgments)

</details>

---

## User Experience (UX)

### User Stories

|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| Anonymous user       | easily navigate the site;                                                | find what I am looking for quickly                            |
| Anonymous user       | view the site on all screen sizes;                                       | visit the site using my mobile and/or tablet device           |
| Anonymous user       | search for and view bikes;                                               | quickly browse for different models of bikes                  |
| Anonymous user       | filter my search results;                                                | search by brand and/or bike model                             |
| Anonymous user       | read details about each bike;                                            | can read technical details to inform my choice of bike        |
| Anonymous user       | access Ciclo Italia social media links;                                  | join Ciclo Italia social media sites                          |
| Anonymous user       | register for a user profile account with a username and password;        | register for an account to allow easy access to site          |
| Anonymous user       | verify that my registration was successful;                              | receive a confirmation email after registering                |
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and log out of my profile account;                                | easily enter and leave the site                               |
| Registered user      | update my shipping, billing and payment details;                         | update address and other details when required                |
| Registered user      | store my address for later use;                                          | avoid having to retype it every time I make a purchase        |
| Registered user      | store my purchase history;                                               | access my previous purchases and payments                     |
| Registered user      | review my purchase choices at checkout;                                  | decide whether to edit purchases before confirming payment    |
| Registered user      | easily make secure payments;                                             | ensure my payments are securely handled                       |
| Registered user      | receive email confirmation of my purchase payment;                       | confirm that my payment was processed successfully            |
| Registered user      | create personal bike reviews;                                            | add a personal review of a purchased bike                     |
| Registered user      | update their personal bike reviews entries;                              | update personal bike reviews if details change                |
| Registered user      | delete their personal bike reviews entries;                              | remove personal bike review details if they become irrelevant |
|          ---         |                                    ---                                   |                              ---                              |
| Site admin/superuser | add new bike listings;                                                   | continuously make new bikes available for purchase            |
| Site admin/superuser | update existing bike listings;                                           | revise existing bike listings with new information            |
| Site admin/superuser | delete existing bike listings;                                           | delete bikes that may no longer be available                  |
| Site admin/superuser | create cycling blogs;                                                    | inform users of news in the cycling world                     |
| Site admin/superuser | update cycling blog entries;                                             | update users on new developments on previous blogs            |
| Site admin/superuser | delete cycling blog entries;                                             | remove blog details if they become irrelevant                 |
| Site admin/superuser | create bike reviews;                                                     | add a review of a purchased bike                              |
| Site admin/superuser | update bike reviews entries;                                             | update bike reviews if details change                         |
| Site admin/superuser | delete bike reviews entries;                                             | remove bike review details if they become irrelevant          |
|                      |                                                                          |                                                               |

### Strategy

The target demographic encompasses riders from 18 upwards who have the desire and finanacil freedom to own a beautiful and finely crafted Italian road bike 

This demographic will include riders of all abilities, from weekend leisure riders, to daily commuters, to serious amateur road racers, semi-professional riders and fully professional team riders

Riders purchasing from the site for competitive reasons will most likely be competing in road racing, time trialling, triathlon and cyclocross events

The site attempts to provide to its users an attractive, user friendly experience and functionality, which allows customers to easily find the bike of their dreams at an affordable price

Ciclo Italia provides a high quality selection of Italian designed road bikes providing customers with high quality imagery, detailed descriptions, customer reviews and competitive pricing, to allow informed decisions before purchases are completed

The main strategy of this site to provide accurate information about the products offered, make it easy and intuitive to navigate and transparent with information to maintain trust and integrity with users

#### Project Goals

To provide customers with a comprehensive, attractive and user friendly site that showcases a selection of the best Italian designed road racing bikes

#### User Goals

Users can easily find their desired bike, see transparent pricing, read reviews on each bike, and choose whether to complete a purchase

### Scope

Project reflects my current skill-set of HTML, CSS, JavaScript, Python and Django

To provide an app with relevant categories, product listings and detail pages, with scope for future expansion

#### Existing Feature

- Fully responsive website for all common mobile, tablet and desktop devices, using Bootstrap responsive grid and custom media queries
- Striking home page jumbotron image to convey a positive initial response from visitors
- Intuitive and responsive Navigation menu with links and search facility
- Links to all available bikes, each available brand and each available model containing a description and image
- A filtering function to sort available bikes
- Registration page with form
- Login page with form
- Profile page containing personal details, payment details and order history
- Cart page with form displaying chosen bike/s
- Checkout page with payment functionality
- Reviews page containing customer reviews of bikes
- Blog page containing cycling themed blog posts
- Project management page for adding, updating and deleting bikes
- Blog and review add/edit page for adding, updating and deleting blog and review entries
- Footer element with social media icon links

#### Future Features to Implement

- Membership scheme app to save on future purchases 
- Members forum app for sharing cycling information such as routes, holidays, maintenance tips, bike recommendations etc
- Contact app to enable users to contact the site owners to ask questions, give feedback etc
- Create the appropriate Ciclo Italia social media sites

### Structure

The overall structure is aimed at ease of navigation to each section and an intuitive path from initial arrival on the home page through finding the desired bike through to a smooth and secure final payment checkout experience

#### Interaction Design

The content has been laid out in an intuiitive way, providing a good flow of information. The home page clearly leads to the bikes page where customers can easily browse through all available bikes. Purchases can be easily made from the bikes page through an easy to use cart and checkout payment pages 

Clear feedback is provided to the user after each interaction, using the messages function in Django and with the use of javascript pop-up toast messages

#### Information Architecture  

The main organising principle for the user is the brand. The app contains a total of 6 brands. Each brand contains 4 bike models. This gives the current app a total of 24 bikes available to view

Available bikes can be found by searching by the following methods:

- Search by brand
- Search by bike model name
- Search by keyword

[Back to Top](#table-of-contents)

#### Database

Development - SQLite3
Production - Heroku Postgres

#### Apps and Models used

- Bikes App

  - The **Bike model** stores information about the all available bikes within each brand

  - The **Brand model** stores information about each brand of bike that is available

- Profiles App

  - The **UserProfile** model stores information about registered users, including shipping and billing address, payment details and purchase history

- Checkout App

  - The **Order** model stores information about each purchase order placed

  - The **OrderLineItem** model stores information from the order, used in calculation in the Order model

- Blog App

  - The **Blog** model stores information about cycling blog posts

- Review App

  - The **Review** model stores information about bike review posts

#### Model Relationship Data Schema

![DB Schema](docs/ms4_database_structure.png)

### Skeleton

#### Page Structure

![page structure diagram](docs/ms4_site_structure.png)

#### Wireframes

My app design has evolved since I first created my wireframes. The overall structural idea I originally had is still, to some extent, visible in my final app

- [MOBILE WIREFRAMES](docs/wireframes/ms4_mobile_wireframes.png)
- [TABLET WIREFRAMES](docs/wireframes/ms4_tablet_wireframes.png)
- [DESKTOP WIREFRAMES](docs/wireframes/ms4_desktop_wireframes.png)

The layout has been kept consistent throughout the site with the navigation bar and footer consistemt to all pages

- Top Navigation bar containing the following before a user is logged in:
  - Ciclo Italia brand logo, providing a site wide link back to the home page
  - A search bar providing users with a way to search by keyword
  - My Account link icon with dropdown menu providing links to the register page and login page
  - Shopping Bag link icon providing access to users shopping cart
- Top Navigation bar containing the following when a user is logged in:
  - Ciclo Italia brand logo, providing a site wide link back to the home page
  - A search bar providing users with a way to search by keyword
  - My Account link icon with dropdown menu providing links to Product Management for superusers, Add/Edit Bike Reviews, Add/Edit Cycling Blog Post, My Profile and Logout for all users
  - Shopping Bag link icon providing access for all users to their shopping cart

- Bikes navigation links situated below the search bar:
  - All Bikes 
    - link that displays all available bikes
  - Bianchi   
    - link to all available Bianchi bikes, including dropdown menu with links to each individual Bianchi model
  - Cinellii  
    - link to all available Cinelli bikes, including dropdown menu with links to each individual Cinelli model
  - Colnago   
    - link to all available Colnago bikes, including dropdown menu with links to each individual Colnago model
  - De Rosa   
    - link to all available De Rosa bikes, including dropdown menu with links to each individual De Rosa model
  - Pinarello   
    - link to all available Pinarello bikes, including dropdown menu with links to each individual Pinarello model
  - Wilier   
    - link to all available Wilier bikes, including dropdown menu with links to each individual Wilier model
  - Reviews 
    - link that displays all existing bike review posts
  - Blog 
    - link that displays all existing cycling blog posts
  
- Footer with social media links to Facebook, Twitter, Instagram, YouTube and Pinterest

### Surface

The overall UX aligns with the design priciples of a modern online bike store type site. The overall feel needs to give confidence to customers that they are purchasing from a professional organisation 

#### Colours
  
Colour palette has been chosen to reflect the Italian origins of the bikes that are available for customers to purchase

Colour Palette generated on [Coolors.co](https://coolors.co/)

![Colour palette](docs/ms4_color_palette.png)

#### Typography

"Barlow" font (with fall-back font of Serif). This font was chosen as it has a modern, technical feel that reflects the high level of technical expertise that goes into designing and manufacturing the best Italian bikes

#### Images

High quality imagery is vital to convey the beauty of the products to potential customers. High quality images of each bike allow customers to fully appreciate what they will be buying and allows them to make an informed decision before completing a purchase

[Back to Top](#table-of-contents)  

## Technologies Used

Designed with HTML5, CSS3, JavaScript, Python3 with the Django Framework

### Languages

[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Integration

[Bootstrap](https://getbootstrap.com/) - by linking via [Bootstrap CDN](https://www.bootstrapcdn.com/) to HTML Doc

[FontAwesome](https://fontawesome.com/) Icons for Social Media links

[Google Fonts](https://fonts.google.com/) - Overall Typography import

[jQuery](https://jquery.com/) - JavaScript library

[Django](https://www.djangoproject.com/) Micro web framework written in Python

### Tools

[VSCode](https://code.visualstudio.com/) - Main workspace IDE (Integrated Development Environment)

[Git](https://git-scm.com/) - Distributed Version Control tool to store versions of files and track changes

[GitHub](https://github.com/) - A cloud-based hosting service to manage Git repositories

[Heroku](https://heroku.com) - Container-based cloud platform for deployment and running of apps

[AWS S3](https://aws.amazon.com/s3/) - Cloud storage for static and media files

### IDE Extensions

- Auto Close Tag
- Beautify - Code Formatter
- Indent-Rainbow
- Bootstrap 4 CDN Snippet
- Markdown Lint
- Python
- JSHint

### Code Validity

- HTML - [W3C](https://validator.w3.org/) - Markup Validation
- CSS - [W3C](https://jigsaw.w3.org/css-validator/) - Jigsaw CSS Validation
- JavaScript - [JSHINT](https://jshint.com/) - JavaScript code warning & error check
- Python - [Pyton Tester](https://extendsclass.com/python-tester.html) Python code syntax checker
- [Autoprefixer](https://autoprefixer.github.io/) Parses CSS and adds vendor prefixes
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) Mobile-friendly check on site
- [Website Page Test](https://www.webpagetest.org/) Runs a website speed test from multiple locations around the globe using real browsers (IE and Chrome) and at real consumer connection speeds.
- [Online-Spellcheck](https://www.online-spellcheck.com/) Online spelling and grammar checks for site and README content

### Other

- [Favicon](https://favicon.io/favicon-converter/) - Favicon Generator
- [Affinity Photo](https://affinity.serif.com/en-gb/photo/) - Image manipulation and colour corrections

[Back to Top](#table-of-contents) 

## Bugs

### Known Issues

  - When creating new bike reviews and cycling blogs from within the app admin all details render correctly. However, when creating from within the app itself, titles, text, added by and published time details all render correctly but images do not render correctly. I will endevour to solve this issue in the near future
  - In Chrome Dev Tools the console returned 3 errors. Errors 1 and 3 relate to the loading of a site.webmanifest file for the site favicon. I have chosen to ignore these errors as they do not affect the performance of the app. Error 2 is a syntax error relating to my doctype. On checking my app the document type is declared correctly and I have run my code through html validation with no errors, so I have chosen to ignore this error as well

![Colour palette](docs/ms4_console_errors.png)

### Project Barriers and Solutions

  - I encountered problems in enabling webhooks to perform as required. I found that purchase confirmation emails were not being sent due to webhook errors. I discovered that the path within Stripe fior my webhooks was missing a / behind the wh at the end of the path. Once this / was added the webhook test returned a 200 code, indicating all was working as expected

[Back to Top](#table-of-contents) 

## Workflow

### Version Control

- Used Git for version control

### Development Environment

- All code was written on [Visual Studio Code](https://code.visualstudio.com/), within the Github environment
- The code was then pushed to GitHub where it is stored in my [Repository](https://github.com/sruss07/MS04-Ciclo-Italia)

### Local Installation

#### 1. Cloning the project

- The code can be run locally through clone or download from the repository on [GitHub](https://github.com/sruss07/MS04-Ciclo-Italia)
- You can do this by opening the repository, clicking on the Code' button and selecting either 'clone or download'

    ![Image](docs/ms4_clone.png)
- The Clone option provides a URL, which you can use on your CLI with `git clone <paste url>`.
- The Download ZIP option provides a link to download a ZIP file which can be unzipped on your local machine. The files can then be uploaded to your IDE

#### 2. Create a Virtual Environment

In the Terminal window:

- Navigate to the folder of the installed files with `cd <path>`
- Create the virtual environment folder with `python -m venv venv`
- Activate the virtual environment with `venv\Scripts\activate.bat

#### 3. Create Environmental Variables

- For sensitive information/passwords, create an `env.py` file to store these as environmental variables

```python
import os

os.environ['DEVELOPMENT'] = 'True'

# Django Secret key - ensure you remove from 
# main>settings.py before pushing to your repository
os.environ['SECRET_KEY'] = '<your value>'

# stripe
os.environ['STRIPE_PUBLIC_KEY'] ='<your value>'
os.environ['STRIPE_SECRET_KEY'] ='<your value>'
os.environ['STRIPE_WH_SECRET'] = '<your value>'

# DB
os.environ['DATABASE_URL'] ='<your value>'

# AWS S3
os.environ['AWS_ACCESS_KEY_ID'] = '<your value>'
os.environ['AWS_SECRET_ACCESS_KEY'] = '<your value>'

# Email
os.environ['DEFAULT_FROM_EMAIL'] = '<your value>'
os.environ['EMAIL_HOST_USER'] = '<your value>'
os.environ['EMAIL_HOST_PASSWORD'] = '<your value>'

```

#### 4. Create a .gitignore file

- Create a file called **.gitignore** in the root directory and ensure it contains the following git exclusions:

```text
    core.Microsoft*
    core.mongo*
    core.python*
    __pycache__/
    *.py[cod]
    node_modules/
    *.sqlite3
    *.__pyc
    env.py
```

#### 5. Install project dependencies

- Install project requirements by typing `pip install -r requirements.txt`

#### 6. Migrate

- Apply model migrations useing `python manage.py migrate`

#### 7. Create a SuperUser account

- Type `python manage.py createsuperuser` and follow the username and passwords prompts from the terminal

#### 8. Deploy locally

- To run the project locally, in the terminal type `python manage.py runserver`
- This will open a localhost address, which is provided in the CLI.
- Either copy and paste the url shown below into a new browser tab, or hover over it and click *follow link*

## Deployment

This project has been deployed to [HEROKU](https://www.heroku.com/)

Media files are hosted on AWS S3 Bucket, and instructions can be found [HERE](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

### Deployment Instructions

1. [Sign up](https://signup.heroku.com/login) for an account on Heroku or [Log in](https://id.heroku.com/login) with your existing account

2. Click on the 'New' dropdown box and 'Create new app'
![Create app on Heroku screenshot](docs/heroku_create_app_01.png)

3. Name your app, choose the appropriate region and submit
![Naming app screenshot](docs/heroku_name_app_02.png)

4. On the Resources tab , search for Heroku Postgres Database and add (*a free Hoby Dev account can be used*)

5. Postgres requires dj_database_url, and psycopg2, which will be installed when the requirements.txt dependencies are installed as explained earlier

6. Click on the Deploy tab and select the GitHub option, then choose you GitHub account and search for the repository to connect to (*You can enter a keyword in the input to search for*). Once confirmed, press 'Connect'
![Connect GitHub sceenshot](docs/heroku_connect_github_03.png)

7. Under Manual deploy, choose your main (or sometime called master) branch to deploy to and press 'Deploy Branch'
![Manual deploy screenshot](docs/heroku_manual_deploy_04.png)

8. Once the build has completed, under Automatic deploys, choose your main (or sometime called master) branch and press 'Enable Automatic Deploys'
![Automatic deploy screenshot](docs/heroku_auto_deploy_05.png)

9. Click on the Settings tab and then the 'Reveal Config Vars' button to reveal the Environmental Variables
![Config Vars reveal button screenshot](docs/heroku_reveal_config_vars_06.png)

10. Enter your Environmental variables and values with the following fields:
![Config Vars screenshot](docs/heroku_config_vars_07.png)


#### 7. Remote Deployment on Heroku

[Back to Top](#table-of-contents) 

 ## Testing

Testing documentation can be found on a separate document [HERE](docs/TESTING.md)

## Credits

### Resources

- [Code Institute Course Content](https://courses.codeinstitute.net/) - Main source of knowledge
- Code Institute **SLACK Community** - Main source of assistance
- [Stack Overflow](https://stackoverflow.com/) - General resource
- [Youtube](https://www.youtube.com/) - General resource
- [CSS-Tricks](https://css-tricks.com/) - General resource
- [W3.CSS](https://www.w3schools.com/w3css/4/w3.css) - General resource
- [CommonMark](https://commonmark.org/help/) - Markdown language reference
- [Colour Palette - Coolors.co](https://coolors.co)
- [TinyPNG](https://tinypng.com/) - Compression of images for site
- [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator
- [Balsamiq](https://balsamiq.com/wireframes/) - Wireframing design tool

### Media

- Site images used are from the respective bike manufacturers websites:
  - [Bianchi](https://www.bianchi.com/)
  - [Cinelli](https://cinelli.it/en/)
  - [Colnago](https://www.colnago.com/en/)
  - [De Rosa](https://derosa.it/)
  - [Pinarello](https://pinarello.com/uk/en)
  - [Wilier](https://wilier.com/en)

## Acknowledgments

I would like to thank:

- **Gerard McBride**, my mentor, for his guidance and advice throughout this project
- **Thomas Muat** for all his help on Slack with my many cries for help!!
- **Chris Zielinski** who's vast knowledge helped me out of a situation where my app wasn't working at all
- Everyone on Tutor Support for giving invaluable help, advice and assistance with my many questions
- **CI staff** and **Slack Community** for always being on-hand to answer my questions

[Back to Top](#table-of-contents) 

