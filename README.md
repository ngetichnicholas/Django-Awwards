# Django-Awwards
## Author
Nicholas Ngetich
*****
### Description
This is a Django web application that allows users to view posted projects and their details. The user can also post a project to be rated or reviewed and a user can as well rate and review other users' projects.

### Prerequisites
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Setup Instruction
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone $ git clone https://github.com/ngetichnicholas/Django-Awwards.git
1. This will clone the repositoty into your local folder
*****
### Home page
A user is required to register and login to the application. Upon successful authentication the user is redirected to home page where all projects posted by different users is displayed.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626781661/screencapture-nick-awwards-herokuapp-2021-07-20-14_26_02_la9krd.png)
*****
### User Profile
Every user registered in the application has profile associated with their account. Profile contains personal details and projects posted by that particular user.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626791781/screencapture-nick-awwards-herokuapp-users-3-2021-07-20-17_31_59_mtj3hu.png)
*****
### View Project details
A user can click on any project image and a page will be displayed containing the project information like ratings, project title, description, live link, repository link and also date posted.  
A user can only see a delete button if they are the owner of the post so they cannot delete a post belonging to another user
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626781789/screencapture-nick-awwards-herokuapp-project-16-2021-07-20-14_37_30_zezmab.png)
*****
### Search Function
A user can search projects and it will return projects matching the search term or display "Found 0 results if no match found by the search function.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626790591/screencapture-127-0-0-1-8000-search-2021-07-20-17_14_13_vzah3v.png)
*****
## API
### Get all Projects [see json list here](https://nick-awwards.herokuapp.com/api/projects/?format=json)
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626789966/Screenshot_from_2021-07-20_17-00-32_ahsrlf.png)
*****
### Get all Profiles [see json list here](https://nick-awwards.herokuapp.com/api/profiles/?format=json)
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1626789966/Screenshot_from_2021-07-20_17-05-34_m1uomy.png)
*****
## Behaviour Driven Development
1. Provides rating form
   - INPUT: User fills rating form
   - INPUT: Rate button clicked
   - OUTPUT: New rating added to the project
1. Provides form to post project 
   - INPUT: Menu link 'Post Site' clicked
   - OUTPUT: Form page displayed
   - INPUT: Form field inputs filled
   - INPUT: Post button clicked
   - OUTPUT: New post added
1. Show user profile 
   - INPUT: User profile icon clicked
   - OUTPUT: Profile page with user information displayed
1. Provides a search form
   - INPUT: Search term entered in the search field
   - OUTPUT: Number of matched project results displayed in the page
1. Show project details
   - INPUT: Project image clicked
   - OUTPUT: A new page loaded with project details
1. Provides a delete function for project
   - INPUT: Delete button clicked
   - OUTPUT: Project deleted
## Dependencies
* django-bootstrap
* Pillow
* cloudinary
* psycopg2
* django-registration
* python-decouple
* Python Venv
* whitenoise
* gunicorn
*****
## Technologies Used
* HTML
* Python 3
* JavaScript
* CSS
******
### Live Link
Or you can access the web application directly via this [LIVE LINK](https://nick-awwards.herokuapp.com/).
*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[nicholas.ngetich@student.moringaschool.com](mailto:nicholas.ngetich@student.moringaschool.com)**
