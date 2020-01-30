# CookBook
-----------

### Milestone Project 3: Practical Python and Data Centric Development

In this project, I will build a full-stack site that allows users to create, read, update, and delete (CRUD) food recipes. Its value or purpose is to allow users to share there own recipes with the community, and benefit from having convenient access to the recipes provided by all other users.

I will build the application with the idea of allowing easy access to cooking recipes to all users in a manner that is visually appealing and user friendly. It will be simple to navigate and understand with features for users to locate specific recipes based on recipe fields.  

This project can be viewed [here](https://cookbook2020.herokuapp.com/)


## User Experience Design
--------------------------

### Scope Plane:

  - What they say they need?

    The client wants to share and encourage other users to share cooking methods so that anyone and everyone can have a place to come too and find new recipes. The website is to feature images of the recipes and the methods and ingredients to making that recipe.

  - What they actually need?

    A intuitive website thats easy to navigate around and to minimise the required steps to complete tasks. The main page can have a list of the 5 most searched recipes, another page with all the recipes on the website, and another to add your own recipe. In this page, can be a form which will be self explanatory.

  - What they don't know they need?

    For it not to be complex in design. A good website is a simple functional website thats intuitive. A mixture of appealing images and short but descriptive content. I will also need to consider for the future to what constraints does the app have to perform within (scalability) i.e as your user base grows can your app handle the growth in traffic.

    ---

    | Potential Scenarios: | Requirement for Scenario to be fulfilled: |
    |------| :--------:|
    | A user wants to find the ingredients to a particular recipe   | Provide a search bar. This will work if only that particular recipe has been uploaded onto the website        |
    | A user wants to add a recipe of there own      |  Add a navigation link for the user to go to and upload there recipe           |
    | May'be the user does'nt have a particular recipe they want to look up but see's an image and then wants to look up its method      |  Have a link below the descriptive content of the recipe with the relevant informtion           |
    
## Stucture Plane:

The website will present you the user with a intuitive and structured format starting with the navigation. It will be clear and simple, displayed in a horizontal fashion on desktop, thus, it being a pridictable structure. More a linear narrative for the audience intended. On each page the title will be highlighted so that you the user knows what page you are on. I will also display a hamburger navigation for mobile use. That, and the footer which will display my name (copyright) will have the same colored theme on all pages. Make it consistent. 

I will structure the home page so that images will use up the most real estate, as i find an appealing image more satisfying to the eye than a lot of content, however i will leave some space to describe the origins of the recipe.   

The recipe page will have a similar structure to that of the home page giving all the recipes that have been uploaded. And finally the "add recipe" page will be a designed as a form to fill in the required fields so that it can be uploaded on the website. 

My intention is to allow users to:

  - Efficiently move through content
  - Be easily educated and informed

Allow owners (me the developer) to:

  - Accomodate growth and change in the application

## Skeleton Plane

This particular plane focuses on:

  - Navigation design
  - Interface design

Its important as its convention that when its available/accessible you the developer provide iconography and navigation thats both simple to learn and something the user is used to seeing from other websites. 

In this projects directory is a folder **wireframe**. In that folder i have designed a mockup of my inital plan for the project. I have designed it so that i have the flexibility if needed to alter something, whether it be the functionality, the color scheme, fonts etc as i progress through the project. Its not good practice to set anything in stone from the start but important to have an idea of the structure of the application. 

## Deployment

My application was coded in the IDE: **Virtual Studio Code**, a local GIT directory was used for version control and then uploaded to GITHUB.
This site is hosted using Heroku and is deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. 

In order for the success of the deployment version i would create an environment variable file named env.py. In this file i will store the MongoDB configuration key and values in order to keep the production database connection string private. A MongoDB database was used as the place to store data for this application. I also need to store these configuration variables in my **config vars** in my heroku settings which acts like a security confirmation in accordance with the values i have set in my env.py file. As these variables and its values are confidential they must not be seen by the public, therefore, i have created a file called .gitignore. In this file will be a list of files that i have within the applications repository that i dont want to share to github/public. And one of those files and its data is the environment variable file, **env.py**. 

In the development phase of my application i still needed to keep the security of my configuration variables private, because even though my application wasnt in deployment at that stage, in order to work on the development stage i still had to upload my code to github for the changes in my application to take place.  

## Credits

### Content
  + I used code from the documentation in mongo DB for my app.py file for a lot of the methods and the general syntax in development of the application. I also used stackoverflow for pagination and for search queries. As well as the assistance of the sites mentioned i also had advice by some of the tutors for how to look up for solutions to problems.

### Media

  + I added a background image to the index page from [pxhere](https://pxhere.com/)

  + To have the application up and running i added recipes and recipe images myself as part of testing. I attained this from [bbcgoodfood](https://www.bbcgoodfood.com/)


### Acknowledgements

  + I received some ideas from the bbc goodfood website for my application with its structure

  + My **Mentor** for his guidance at the beginning, middle and end of the project

  + And to the **Tutors** at [Code Institute](https://codeinstitute.net/)  















