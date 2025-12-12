# Capstone Project - NoteKnight



Introduction
----
Noteknight is a full Django powered application designed for users to manage their own personal notes with basic read/write functionality using a Python back-end. The app includes user roles, a custom profile model, system security and structured and responsive UI.

The system has been kept simplistic and minimal to help the projects intended purpose in learning full project management and cloud based deployment handling with

Planning
----
The core planning goals of the project where a working authentication system, functional CRUD implementation, clean integration between models and templates, a reliable deployment pipeline and an accessibility focused UX/UI

A structured agile methodology was used throughout the project to keep it on track and help with any timekeeping issues. Admittedly this project had some deployment bumps in its early stages and the entirety of the work was done in the last week, the final project being the third attempt to produce as the first two’s codebases ended up far too needlessly complex for the state of the project/ With that the projects todo board is somewhat lip-service to its required function

UX/UI Design
----
The UI was intentionally kept clean and clear as the focus was on data handling and permissional role management. A minimalist layout using html and css allows for simple navigation through the app allowing the user to login, register, view/create/delete notes, and logout.

Visually clear and consistent styling across templates help to make the app simple to login and use without any hand-holding required for the user. Forms where styled with usability first in mind, this helped to keep the focus of the project on a clean and clear codebase.

The ui is responsive to user actions and across different devices following the mobile first methodology of development. 

The user is able, upon registration, to become an admin with a keyword used in the sign up form. This gives them access to django’s in built dashboard with access to user information and the ability to delete users



Features
----
Existing features include:

User registration
Secure login/logout
Fully functional note creation and manipulation
Per-user data isolation
Auto generated timestamps
Mobile friendly browser layout
User roles via a Profile model
CSRF protection
Form validation
Security features, including Django’s built-in authentication, safe redirect patterns and server-side model validation

Agile
----

Libraries and Frameworks
----
Django 4.2.1 – main web framework
Gunicorn – production WSGI server
Whitenoise – static file management on Heroku
SQLite (dev) → PostgreSQL (Heroku)
Bootstrap / CSS – styling
Heroku CLI – deployment
Django Forms – rendering & validation
Python 3.12 – core language

AI Implementation
----
AI was mainly used as a basic framework builder and aided in syntax correction, it also helped with debugging somewhat during the various Heroku deployments and project deployment during our pipeline setup

Deployment
----
The app is deployed to heroku following the various coding and project setup practices required for deployment on the platform, such as the use of a Procfile, whitenoise static collection, config vars with key-value pairs and Heroku’s PostgreSQL addon


Testing & Validation
----
Testing covered the basic manual testing between the IDE environment through to the deployment platform on a regular basis with each feature completion to enable end of run deployment without any hiccups, this methodology helped with better understanding of the pipelines process and requirements during the project lifetime

Automated testing through python proved somewhat tricky with the Heroku setup projecting failures on manually tested and passed features


Future Features and Changes
----
This app was developed for personal use for my own varied projects, its continuation will include mind maps, image handling and category handling for different projects through data id’s.

I plan to increase protection through the use of rate limiting and Django’s CSP, data encryption and logging system, as this app will be acting as my personal projects board for the future



References
----
Django’s Documentation
Code Institutes LMS
W3C Validators
Heroku Deployment Documentation
Bootstrap Documentation
StackOverflow




