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

    A intuitive website thats easy to navigate around and to minimise the required steps to complete tasks. The main page can have a list of the 4 most searched recipes, another page with all the recipes on the website, and another to add your own recipe. In this page, will be a form to fill which will be self explanatory.

  - What they don't know they need?

    For it not to be complex in design. A good website is a simple functional website thats intuitive. A mixture of appealing images and short but descriptive content. I will also need to consider for the future to what constraints does the app have to perform within (scalability) i.e as your user base grows can your app handle the growth in traffic.

    ---

    | Potential Scenarios: | Requirement for Scenario to be fulfilled: |
    |------| :--------:|
    | A user wants to find the ingredients to a particular recipe   | Provide a search bar. This will work if only that particular recipe has been uploaded onto the website        |
    | A user wants to add a recipe of there own      |  Add a navigation link for the user to go to and upload there recipe           |
    | Maybe the user doesn't have a particular recipe they want to look up but see's an image and then wants to look up its method      |  Have a link below the descriptive content of the recipe with the relevant information           |

### Stucture Plane:

The website will present you the user with a intuitive and structured format starting with the navigation. It will be clear and simple, displayed in a horizontal fashion on desktop, thus, it being a predictable structure. More a linear narrative for the audience intended. I will also display a hamburger navigation for mobile use. Color theme on all pages will be the same to make it consistent. 

I will structure the home page so that images will use up the most real estate, as i find an appealing image more satisfying to the eye than a lot of content, however i will leave some space to describe the origins of the recipe.   

The recipe page will have a similar structure to that of the home page giving all the recipes that have been uploaded. And finally the add recipe page will be a designed as a form so the user can fill in the required fields so that it can be uploaded on the website. 

My intention is to allow users to:

  - Efficiently move through content
  - Be easily educated and informed

Allow owners (me the developer) to:

  - Accomodate growth and change in the application

### Skeleton Plane

This particular plane focuses on:

  - Navigation design
  - Interface design

Its important as its convention that when its available/accessible you the developer provide iconography and navigation thats both simple to learn and something the user is used to seeing from other websites. 

In this projects directory is a folder **wireframe**. In that folder i have designed a mockup of my inital plan for the project. I have designed it so that i have the flexibility if needed to alter something, whether it be the functionality, the color scheme, fonts etc as i progress through the project. Its not good practice to set anything in stone from the start but important to have an idea of the structure of the application.

Here is a list of my wireframes with ideas to building this project
  + [index page](https://raw.githubusercontent.com/aledgriffiths79/cookbook/master/wireframe/home-page.png)
  + [recipes page](https://raw.githubusercontent.com/aledgriffiths79/cookbook/master/wireframe/Recipes.png)
  + [add/edit recipe page](https://raw.githubusercontent.com/aledgriffiths79/cookbook/master/wireframe/form-recipes.png)

## Features

The project has multiple pages that provide different features and options.
  + **index.html** is the base of the project and provides a navigation bar, a recipe search bar, and the 4 most looked at recipes in the application with a feature that allows you to go in more specific about the recipe, i.e. ingredients, method etc
  + **recipes.html** provides a base to all the recipes that have been uploaded in the application. Here also you can look at any recipe that you like and look more into detail about that recipe
  + **addrecipe.html** is where you upload a recipe. It allows users to add there recipe by filling out a form
  + **recipe.html** when you look more in detail on a recipe you will arrive at this page. In this page aswell as the recipe method, ingredients, and recipe introduction it provides you a choice to edit that recipe or delete the recipe. 

### Features Left to Implement

  + In the future i may add a login and password so that they the user has more control who can edit there own recipes that they have uploaded, because the application at present has no constraints to who can delete or ammend a recipe.

## Technologies Used

  + Python
    + Python is used for the back-end functionality of this project
  + HTML5
    + Used to construct the structure of the front-end of the project
  + CSS/Materialize
    + Provides styling for the pages and all content
    + Materialize is a modern responsive CSS framework based on Material Design by Google.
  + Mongo
    + Used for storing data and is easy to add or change fields 
  + Flask
    + Flask provides libraries, modules and tools to help build my webb application. It doesnt depend on other libraries, hence why it is referred to a microframework

## Testing

I have tested the application manually on the basis of going over my UX section and ensure they all work as intended with the project providing an easy and straightforward way for the users to achieve their goals.
The index/recipes/add_recipe page is tested by going from one page to the other and seeing if it loads correctly. The **add recipe** page is tested by checking the recipe is entered, the page re-directs and the new recipe is present on the **recipes page**

The recipe page is tested by searching any of the recipes displayed and picking a recipe and then going to that recipe details page and checking that the contents are there.

The update recipe page is tested by going to the **edit recipe page** and changing some data and committing it. This then redirects the user to the index page. I then test that the information has changed on that recipe.

The delete recipe page is tested by going to it's recipe details page and deleting it, then checking the redirect has happened and that the recipe does not appear on the recipes page.

I concentrated on producing a intuitative project where logic and functionality is at its core. I kept my design to be usable and simple to navigate with readable font faces and breathable spacing (i.e. negative space).

As the site is built with a responsive design it works for mobiles, ipad and desktop. I used the development tools on google to make sure the different size devices scalability worked. 

## Deployment

My application was coded in the IDE: **Virtual Studio Code**, a local GIT directory was used for version control and then uploaded to GITHUB.
This site is hosted using Heroku and is deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. 

In order for the success of the deployment version, i would create an environment variable file in my applications repository named env.py. In this file i will store the MongoDB configuration key and values in order to keep the production database connection string private. A MongoDB database was used as the place to store data for this application. I also need to store these configuration variables in my **config vars** in my heroku settings which acts like a security confirmation in accordance with the values i have set in my env.py file. As these variables and its values are confidential they must not be seen by the public, therefore, i have created a file called .gitignore. In this file will be a list of files that i have within the applications repository that i dont want to share to github/public. And one of those files and its data is the environment variable file, **env.py**. 

In the development phase of my application it was important to keep the security of my configuration variables private, because even though my application wasnt in deployment at that stage, in order to work on the development stage i still had to upload my code to github for the changes in my application to take place. 

Hosting the development version was used using the url local host **127.0.0.1:5000/**. This is issued in your local command terminal after inputting **python3 app.py** in the command terminal. The *app.py* file is the base where your backend functionality is interpreted to your frontend templates. When you make new features/functions in your IDE you refresh your development version browser and the changes will be seen live. However to make a permanent change to an updated file you then will have to use git in your command terminal to make those changes which then will be stored in your GITHUB repository.

With Heroku an updated application will be uploaded automatically once you update your github repository as Heroku uses your chosen **deployment method** i.e. Github and *master branch* as every push to master will deploy a new version of the app. 

## Credits

### Content
  + I used code from the documentation in mongo DB for my app.py file for a lot of the methods and the general syntax in development of the application. I also used stackoverflow, w3 school and Mdn Web Docs for pagination, search queries and other app functionalties. As well as the assistance of the sites mentioned i also had advice by some of the tutors for how to look up for solutions to problems.

### Media

  + I added a background image to the index page from [pxhere](https://pxhere.com/)

  + To have the application up and running i added recipes and recipe images myself as part of testing. I attained this from [BBC GoodFood](https://www.bbcgoodfood.com/)


### Acknowledgements

  + I received some structure ideas from the bbc goodfood website for my application.

  + My **Mentor** for his guidance at the beginning, middle and end of the project

  + And to the **Tutors** at [Code Institute](https://codeinstitute.net/)  

