# [RARE Publishing Platform Server in Python]

> Nashville Software School Group Project for Rabid Sharks

## The Concept

This server code pairs with the Rare Publishing Platform React App which can be found here https://github.com/nss-day-cohort-44/rare-rabid-sharks

Rare App allows users to make, view, edit, and comment their own posts, as well as the posts of other users

(insert ERD here)
RareServerERD.png

## Features

* Embedded YouTube player so that users can easily watch videos within the app.
* Transcription Request creation and activation process that is intuitive, easy-to-use, and minimally disruptive to the user's immersion in their video of choice.
* Responsive design so that the site remains not only functional, but also a joy to use regardless of the user's screen size.
* Internationalization! The app is all set up and ready to be translated into any language spoken on this Earth! There is already a full translation set for Chinese set up in the app (albeit surely with wild grammatical and vocabulary inaccuracies since I, a very much non-fluent Chinese speaker, made it).
    * The app makes its choice on what locale the user is in based on the user's primary browser language. To see the Chinese version of the site, you must change your browser's language to Chinese!


### Setting Up Database

# Pulling down the Server-Side Repo. 
 
> Note: This project is meant to run simultaneously with the Client-Side Repo found here: https://github.com/nss-day-cohort-44/rare-rabid-sharks  
 
> Depending on which repo you start with, you may already have the following directories set up.  
> This project requires Python  
 
# To Begin installing the Server-Side Repo, complete the following steps: 
 
1. Create a directory from which to deploy the application. 
	
```mkdir RARE ```
 
1. Within RARE, create two sub-directories, CLIENT and SERVER 

```mkdir CLIENT ```
	
```mkdir SERVER ```
 
1. Navigate into the SERVER sub-directory. 
 
```cd CLIENT ```
 
1. Enter the following commands: 
	
 <git clone git@github.com:nss-day-cohort-44/rare-rabid-sharks.git .> <-- note the single 	
dot preceded by a single space.  
 
Create a virtual environment: 
<pipenv shell>

Once the virtual environment is created, install the 3rd-party software. 

```pipenv install autopep8 watchgod ```

Enter in the following command to start your new data server written in Python: 

```watchgod request_handler.main ```

> If there are no errors in the code, you will see the following, terse output:  
 
<watchgod request_handler.main [09:34:37] watching "/Users/.../workspace/python-server" and reloading "request_handler.main" on changes…> 









## Screenshots

myPosts.png

## A guided workflow, if it so interests you

1. Register a new account. **Do not use any sensitive credentials. This is not a secure application!** 
1. Make a post of your own or view other users posts and comment on them.
1. Edit or delete any of your own posts or comments.
1. Add, edit, or delete Categories for your posts.
1. Add, edit, or delete Tags for your posts.

## Technologies Used

This application was built using [Python] and [SQLite3]  

## Author

NSS Cohort 44 Rabid Sharks Team
