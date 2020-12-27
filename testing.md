# TESTING 
## Table of contents

- [**Automated testing**](#Automated-testing)
    - [Validating](#Validating)
- [**Testing user stories**](#Testing-user-stories)
- [**Manual testing**](#Manual-testing)
    - [Sign Up](#Sign-up)
    - [Log In](#Log-in)
    - [Log Out](#Log-out)
    - [Change Password](#Change-password)
    - [Delete Account](#Delete-account)
    - [Gallery](#Gallery)
    - [Profile](#Profile)
    - [Add Image](#Add-image)
    - [Edit Image](#Edit-image)
    - [Delete Image](#Delete-image)
    - [Search Image](#Search-image)
    - [Flash Messages](#Flash-messages)
    - [Buttons](#Buttons)
    - [Footer](#Footer)
- [**Resolved issues**](#Resolved-issues)
- [**Unresolved issues**](#Unresolved-issues)
- [**Browsers**](#Browsers)
- [**Responsiveness**](#Responsiveness)

To return to the README file, click [here]( https://github.com/SuzanneNL/star-trail-photography/blob/master/README.md).

## Automated testing
### Validating
- HTML code was validated by the [W3C Markup Validation Service](https://validator.w3.org/) and beautified using [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html). 
- CSS code was validated by the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/), and beautified using [Freeformatter CSS Beautifier](https://www.freeformatter.com/css-beautifier.html). No errors came up.
- Javascript code was validated by [JSHint](https://jshint.com/), and beautified using [BeautifyTools Javascript Beautifier](http://beautifytools.com/javascript-beautifier.php). 
- Python code was validated by [pep8]( http://pep8online.com/). 

## Testing user stories
### As the creator of this website...
1. **I want my website to be attractive so that a user is enticed to navigate it and discover all there is to see.**
    - The star trail images against the black background attract the attention of any user. Buttons are a bit dull, as to highlight the star trail images even more. The Sign Up button stands out more, due to its white color, to attract new members. The use of several Materialize features, allows for a positive user experience. 
2. **I want my website to have a clear structure, so that it is easy to navigate.**
    - The navigation bar allows a user to browse to the different pages of this website. A user will only be able to see and visit pages that are relevant to him, as explained in the paragraph 'Structure' of the README file. 
    - Buttons are in place to delete an image or the user's account, or redirect a user to pages for adding/editing images and updating the password. 
    - A 'go to the top' button in the gallery and on the profile page allows users to go to the top of the page. 
    - A scrollspy on the homepage makes it easy for a user to skip to interesting parts of the article.
    - Links in content on pages also redirect users to other pages, such as 'New here? Join Now!' on the Sign Up page, or the article on the homepage inviting a user to visit the gallery. 
    - Functions in the app.py file ensure that a user, after an action, is redirected to a relevant page. For example: after a user logs in, he is redirected to his profile page. After logging out, he is redirected to the log in page. After adding or editing an image, he can see the result immediately as he is redirected to the gallery.
3. **I want my website to give feedback to users so that it is easy to navigate.**
    - The Materialize forms for signing up, logging in, adding images, editing images and updating a password give feedback in the form of colors (red for error and green for success) and text when fields are filled in correctly and incorrectly, or left blank. 
    - Flash messages give feedback after user actions with color and text (again red for error and green for success). For example, when logging in with an incorrect username or password, the flash messages points out that an incorrect username or password was given. Or when a user tries to sign up and the username is already taken, he will receive a flash message pointing this out. Another example is when a user logs in or signs up, he is welcomed by a flash message. 
    - Hover effects such as a pointer and changing colors of/in a button also give feedback to the user, about whether or not something can be clicked. 
    - Since the edit and delete buttons are icons, these buttons have a mouseover effect on desktops, showing text: 'Edit image' for the edit buttons and 'Delete image' for the delete buttons.
4. **I want my website to inform users about how to take star trail photographs.**
    - On the homepage one finds an article with advice on how to take star trail photographs. The gallery shows images that registered users have taken and serve as an example for e.g. camera settings and locations one can choose.
5. **I want my website to have users sign up, and share and manage their photography.**
    - The Sign Up button in the navigation bar stands out from the other buttons because of its white color. Signing up is easy and simple, and with only two required fields, little private information is needed to register.        
    - Adding an image is simple as well, through a Materialize form. Taking your first star trail image feels like quite an achievement. I like to believe that new photographers are inspired by the images in the gallery and will feel a wish to share their own work as well, if they're proud of it (they will be!). 
6. **I want to let my registered users manage their own work and their account.**
    - Users can upload their images and as long as they are logged in, they can edit their work by clicking on the edit button. They will be redirected to a page with the same form as the one for adding an image, except all the fields will be filled in with the current information of the image. He can change whatever he wants and by clicking on submit. The information is changed and saved in the database and therefore in the gallery and on the profile page. 
    - He can also delete his image by clicking on the bin icon and confirming his decision.
    - The downside of signing up with nothing more than a username and a password is that without an e-mail address the username and password cannot be retrieved when the user loses his information. A user does have power of his account in the sense that he can change his password through a simple form, , or even delete his account. 
7. **I want to protect the work of users by not giving rights to edit and delete images to others than themselves. They should also be the only ones to be able to change their password or delete their accounts.** 
    - Users can only see the edit and delete buttons under their own images. When a user chooses to edit an image he is redirected to a page with the following URL:
http://star-trail-photography.herokuapp.com/edit_image/<image_id>.
Unfortunately, if a malevolent user was to discover the id of someone else's image (they cannot be retrieved from the website itself, but could be found for example by checking the browser history), he could copy this id into the URL and will then have the possibility to change the image. 
    - When a user goes to the form for changing their password, the URL is as follows:
http://star-trail-photography.herokuapp.com/change_password/<username>
A malevolent user would perhaps try to type someone else's username, but will not succeed because the session cookie and the username will not correspond. 
    - On the profile page, a user sees a button that says 'Delete Account'. When he clicks on this, a modal pops up to make a user confirm his choice so that the account gets deleted (or he can go back to his profile by clicking on Cancel). 
8. **I want to prevent random guest users from uploading random images and information, so as not to pollute the gallery.**
    - Adding an image to the gallery can only be done after someone registers with a username and password. 
9. **I want users that upload their work to fill out the form with details.** 
    - All fields on the forms for adding and editing an image, except for the description field, are required. If a user leaves one field empty, the Materialize form will give an error message. The point is namely not only to show images but also to show settings, so that other photographers can learn from them. That is also why fields have minimum and maximum lengths. All values are stored as strings in the database, even though ISO for example is always a number. This is because I do want to allow a user to type e.g. '?' if he doesn't know his settings. 
10. **I want to warn users when they try to delete their work, as a form of defensive programming.** 
    - When a user clicks on the bin icon, the image is not immediately deleted, but a modal pops up. The user is asked if he is sure he wants to delete this image. He can then cancel and go back to the gallery or profile page, or confirm. 
11. **I want to have rights over all content on my website, by giving myself the role of administrator, in case users behave in an unwanted fashion (e.g. uploading irrelevant content).** 
    - As an administrator (username 'Admin'), I manage all content on my website. I can edit and delete all images that have been uploaded by all users. I, however, do not have access to a username's password other than my own. This is not something I would want, for privacy reasons. Of course, if I user misbehaves, I could delete the account from the database, if necessary.

### As a user in general...
1. **I am interested in star trail photography.**
    - The website is intended for people who have an interest in night photography, specifically star trail photography. They can be more advanced photographers that want to share their work, or beginners that have not learned yet and are looking for information, or people that have learned through this website and now want to share their first images. Advertizing this website would be helpful to attract these kinds of people. 
2. **I enjoy looking at beautiful images of star trails.**
    - I haven't met anyone yet that doesn't like star trail images. People who are new to star trail photography, are usually curious and try to understand what they see. Some will look at them longer than others of course. In any case, the website has a beautiful banner image and a gallery with beautiful pictures. 
3. **I want to learn about how to create star trail images myself.**
    - Users can learn how to take these pictures through reading the article on the homepage, and looking at other people's images and the settings they chose. 
4. **I want to search through the gallery.**
    - At the top of the gallery is a search bar. It can search the fields title, user and description. 
5. **I want to sort images in the gallery.**
    - Users have the option to sort the images in the gallery by selecting one of the options in the 'sort by' menu. There are four options: date uploaded ascending, date uploaded descending, date taken ascending and date taken descending. 
6. **I want to be able to easily navigate the website.**
    - Navigation is easy, as already explained above. This is made possible with a navigation bar, buttons, the scrollspy and links in the content. Also, users are redirected to logical pages after actions such as logging in and out. 
7. **I want to be able to contact the creator of the website.**
    - Users can click on the icons at the bottom of the page to be referred to the creators' personal pages.

### As a guest user...
1. **I want to be able to sign up, so that I can share my own work.**
    - A white button in the navigation bar stands out from the other buttons, to attract attention. When users want to sign up, they only have to provide a username and password. After registering, they will see an 'add your image' button at the top of the gallery, which is not visible for unregistered users. 

### As a logged in user...
1. **I want to upload my work to the gallery, providing details about my images.**
    - After clicking on the 'add your image' button, a user is redirected to a form with different fields, such as a title, the camera that was used, settings such as ISO and focal length, location, date and a description. The description field is the only one that isn't required. All answers will be stored as strings in the database, even if some values are integers. This is because I want to allow users to write '?' for example, when they don't know their settings. 
2. **I want to manage the work that I have uploaded.**
    - Underneath each of their own images, users will see an edit and delete button. They are the only ones to see these (except for the administrator). These buttons allow users to edit and delete their images. 
3. **I want to have a profile page where I can see only my work.**
    - After logging in, a user is redirected to his personal profile page. 'Profile' also appears in the navigation bar. On this profile page, a users sees all his own images. 
4. **I want to be able to update my password.**
    - On the profile page, a user will see a button 'Change Password'. When a user clicks on this, he will be redirected to a small form. The form contains two fields: username and password. The value for username is already filled in. A new password can be typed and a user can submit to save the new password. 
5. **I want to be able to delete my profile.**
    - On the profile page, a user will see a button 'Delete Account'. When a user clicks on this, a modal pops up asking the user if he is sure he wants to delete his account. A user can then cancel and go back to the profile page, or confirm his choice. He is then logged out, his account is deleted from the database, and he is redirected to the sign up page. His images will stay in the gallery under his former account name. 
6. **I want to be able to log out.**
    - A user logs out by clicking on Log Out in the navigation bar. He will see a green flash message that informs him logging out was successful. His session cookie has been deleted. The website is now shown as it's supposed to, for users who haven't registered or aren't logged in. 

## Manual testing
Manual testing was done on different devices (see Responsiveness).
### Sign Up
- Before signing up, users see the options Home, Gallery, Log In and Sign Up in the navigation bar. 
- In the Sign Up form: provide username of less than 4 characters. The form tells a user that the username doesn't meet the criteria (red color, text).
- Provide password of less than 4 characters. The form tells a user that the password doesn't meet the criteria (red color, text).
- Leave one of two fields empty. The form tells a user that the empty field needs to be filled in (red color, text).
- Provide username or password containing forbidden characters. The form tells a user that the username or password don't meet the criteria (red color, text).
- Provide username and password that meet requirements. The form will give the fields a green color. 
- Provide a username that already exists and submit the form. The user is redirected back to the sign up page. A red flash message is visible: 'That username is taken. Please try another.'
- Provide a username that doesn't already exist and submit the form. The user is redirected to the home page. A green flash message is visible: 'Thank you for signing up! Welcome!' In the database, a new user is added with an id, username and hashed password. The user sees the options Home, Gallery, Profile and Log Out in the navigation bar. 

### Log In
- Before logging in, users see the options Home, Gallery, Log In and Sign Up in the navigation bar.
- In the Log In form: leave one of two fields empty, or both, and try to log in. The form tells a user that the empty fields need to be filled in (red color, text).
- Provide both username and password. The form will give the fields a green color. 
- Provide a false username with a false or correct password and submit the form. The user is redirected back to the log in page. A red flash message is visible: 'Incorrect username and/or password. Please try again.'
- Provide a correct username with a false password and submit the form. The user is redirected back to the log in page. A red flash message is visible: 'Incorrect username and/or password. Please try again.'
- Provide a correct username with a correct password and submit the form. The user is redirected to the home page. A green flash message is visible: 'Welcome, <username>!' A session cookie is added, as can be seen in the Chrome DevTool (go to Application, Cookies, click on the URL, you will see the session cookie). The user sees the options Home, Gallery, Profile and Log Out in the navigation bar. In the gallery, a user will see an 'add your image' button. And underneath previously added image, he will see edit and delete buttons.

### Log Out
- Click on 'Log Out' in the navigation bar. The user is redirected to the Log In page. A green flash message is visible: 'You have been logged out'. The session cookie is deleted, as can be seen in the Chrome DevTool (go to Application, Cookies, click on the URL, you will no longer see the session cookie). The website is displayed as it was before logging in. 

### Change Password
- Click on 'Change Password' on the profile page. The user is redirected to the change password form. His username is filled in, the password field is empty.
- In the form, leave the password field empty and try to submit. The form tells a user that the empty field needs to be filled in (red color, text).
- Provide a password that doesn't meet requirements. The form will give the field a red color and warn the user that it doesn't meet the requirements. 
- Provide a password that meets the requirements. The form will give the fields a green color. After submitting, the user is redirected to the profile page. A green flash message is visible: 'Your password has been updated!' The new password has been hashed and stored in the database.
- Try again. Now change the username and provide a password that meets the requirements. After submitting, the user is redirected to the profile page. A green flash message is visible: 'Your password has been updated!'. The username has not been changed, as this form only serves to change the password. The new password has been hashed and stored in the database.

### Delete Account
- Click on 'Delete Account' on the profile page. A modal pops up asking the user if he is sure he wants to delete his account. 
- A user can click on 'Cancel'. The modal closes and he is back on the profile page.
- A user can click on 'I'm Sure' to confirm his choice to delete his account. The user is then logged out, his account is deleted from the database, and he is redirected to the sign up page. A green flash message is visible: 'Your account has been removed'. The session cookie is deleted, as can be seen in the Chrome DevTool (go to Application, Cookies, click on the URL, you will no longer see the session cookie). The website is displayed as it was before logging in. 
- After deleting his account, his images will stay in the gallery under his former account name. 

### Gallery
- The gallery renders all images that have been added (and not deleted) by users and exist in the database. 
- Images that have been deleted by users, are not shown in the gallery.
- Logged in users see an 'add your image' button at the top of the gallery.
- Logged in users see edit and delete buttons under their own images.

### Profile
- The profile page renders all images that have been added (and not deleted) by the currently logged in user and exist in the database. 
- Images that have been deleted by the user, are not shown on the profile page.
- Users see edit and delete buttons under all their images.

### Add Image
- After logging in or signing up, go to the gallery. An 'add your image' button is visible. Click on the button.
- A user is redirected to the add image page. 
- All fields need to meet requirements, or the form will give a warning as in the log in and sign up forms. 
- All fields except the descriptions need to be filled in. Otherwise the form cannot be submitted. 
- After submitting a correctly filled out form, the user is redirected to the gallery. A green flash message is visible: 'Thank you. Your image has been added to the gallery!'. In the database, a new image has been added. 
The displayed number of images in the gallery is updated with one extra. The image has been added to the gallery, at the bottom. It will also have been added to the profile page.

### Edit Image
- A user can see an edit button under his own images. After clicking on this, a user is redirected to the edit image page. 
- All fields are filled in with the current value. When updating fields, they need to meet requirements, or the form will give a warning as in the log in and sign up forms. 
- All fields except the descriptions need to be filled in. Otherwise the form cannot be submitted. 
- After submitting a correctly filled out form, he is redirected back to the gallery or the profile page, depending on where he clicked on the edit button. A green flash message is visible: 'Your image has successfully been updated!'. In the database, the information has been updated. When looking in the gallery and profile page, one sees that the image has been updated. 

### Delete Image
- A user can see a delete button under his own image. After clicking on this, a modal pops up: 'Are you sure you want to delete this image?'
- After clicking on cancel, the modal closes. 
- After confirming his decision to delete the image, he is redirected to the gallery or the profile page, depending on where he clicked on the delete button. A green flash message is visible: 'Your image has been removed'. In the database, the image has been deleted. Therefore, the image has been deleted from the gallery and from the profile page.

### Search Image
- At the top of the gallery is a search bar. It can search the fields title, user and description.
- If a user searches a word that exists in the fields title, user or description, the images containing this word will be shown. Also the user sees the number of images containing this word. 
- If a user searches a word that doesn't exist in the fields title, user or description, a message is shown: 'Sorry, your search returned no results'. The total number of images is 0.
- If a user searches a word that exists in the image information but outside of the fields title, user or description, a message is shown: 'Sorry, your search returned no results'. The total number of images is 0.
- Clicking on the cancel button will reset the page to show all images and empty the search field. The total number of images on the page is shown.

### Flash Messages
- Successful actions give dark green flash messages in a light green field.
- Successful actions have a dark green checkbox icon at the left of the text.
- Unsuccessful actions give dark red flash messages in a light red field.
- Unsuccessful actions have a dark red exclamation mark icon at the left of the text.

### Buttons
- All buttons have a hover effect: the mouse turns into a pointer and the color of the button and/or the text/icons inside change. 
- Since the edit and delete buttons are icons, these buttons have a mouseover effect on desktops, showing text: 'Edit image' for the edit buttons and 'Delete image' for the delete buttons.
 
### Footer
- The icons in the footer have a hover effect: the mouse turns into a pointer and the color of the icons change.
- When a user clicks on one of these icons, he is redirected to the corresponding website in a new tab.

## Resolved issues
**1: A line on the right side of the body**<br>
When I changed the background color of the body, a 10px line appeared on the right, from the top to the bottom of the page. The Chrome DevTool showed that this was because a div called **drag-target** appeared. This is a Materialize class, probably originating from the navigation bar. The following CSS code fixed this bug:
```
.drag-target {
    width: 0 !important;
}
```

**2: Double for loop**<br>
This website has a gallery with images accompanied by photography details. I wanted the structure of the gallery on a small screen to be different from the structure on a desktop. First I wrote a section for the desktop gallery structure and underneath, I added a section for the mobile gallery structure. I explained in the Materialize paragraph in the README file, that this is because Materialize doesn't have order classes. I had to create two structures in my html file. I hid the mobile gallery with **display: none**. Then in the media queries, I set the desktop gallery to **display: none** and the mobile gallery to **display: block**. In desktop view, the gallery appeared. In mobile view however, the gallery was not visible. This is because Jinja already unpacked my list of images for the desktop gallery, even though I had set that to **display: none**. I therefore had to make a change in my get_images function.
My original code for the gallery was:
```
@app.route("/get_images")
def get_images():
    images = mongo.db.images.find()
    return render_template("gallery.html", images=images)
``` 
However, what you see is not technically a list: it's a Mongo Cursor Object. Wrapping the find method inside a Python list converts the Cursor Object into a proper list:
``` 
@app.route("/get_images")
def get_images():
    images = list(mongo.db.images.find())
    return render_template("gallery.html", images=images)
```
This resolved the issue: the mobile gallery appears on smaller screens.  

**3: Misplaced button**<br>
I had accidentally placed the submit button for signing up outside of the form code. Therefore, a new user could not actually sign up. This was fixed of course by placing the button inside the form.

**4: Defensive programming for registering**<br>
Users were allowed to create an account without filling in both the username and password fields. Also, spaces could be used to create a username or password. The first issue was resolved by adding the required attribute. The second was resolved by specifying that users could use the letters A-Z both in lower and uppercase, the numbers 0-9, an underscore and a period.

**5: Mobile gallery disappeared**<br> 
I had built two galleries, one for the desktop, and one for mobile screens that I made visible on different screen sizes using media queries, **display: none** and **display: block**, as I already explained above. 
However, one day, I discovered that the mobile gallery had disappeared: it was no longer visible. It seemed like I had changed something in my code. I retraced my commit messages, but I couldn't find anything that would have made this change. I used !important to see if this could override, but nothing happened. I deleted all my new code from after creating my two gallery structures, but it didn't help. I used online validators to check if something was wrong with my code, but there were no errors. 
Then I realized I had recently added an extra image to my database. There were three images now, instead of two. So I deleted the third image from the DB, and my mobile gallery reappeared, with two images! My hypothesis then was that the gallery would only appear if it had to display an even number of images. I therefore added two extra images to the database, and indeed, all images (a total of 4 now) appeared. My hypothesis was correct: the mobile gallery was visible only when it had to display an even number of images, but disappeared when there it had to display an uneven number of images. This was strange, because the desktop gallery worked with both uneven and even numbers. 
I thought this might be resolved by adding an extra if statement (like the one I use for the desktop gallery), but this didn't resolve the issue. As I was talking to tutor support, who weren't able to help me, I suddenly came up with the idea that probably, the if statement in my desktop gallery was having some sort of power over my mobile gallery and that the order 'desktop gallery - mobile gallery' had something to do with this. So I decided to put the mobile gallery section at the top of my html file, above the desktop gallery section. This resolved the issue! The mobile gallery now is visible, both with an even and uneven number of images.  

**6: Datepicker shows future dates**<br> 
Users need to fill in when they took a picture when they want to add an image to the gallery. I used the datepicker from Materialize. As a user cannot take pictures in the future, I wanted the datepicker to only display dates in the past, and today. I did this by adding the following jQuery code:
```
maxDate: new Date()
```
This prevented a user from selecting a date in the future. However, a user could still browse to a year in the future. Granted, there were no dates to actually select, but it didn't make sense for the year dropdown menu to display future years. I wanted the last year in the yearrange to be the current year. 
This was resolved by creating a variable:
```
var currentYear = (new Date).getFullYear();
```
And adding this variable to the datepicker's code:
```
maxYear: currentYear
```
Now, users cannot select a future date or browse beyond the current year.

**7: Wrong images were deleted**<br> 
Users have the power to edit or delete their own images. As an administrator, I can delete every image. When testing the delete image function, I found out that the wrong images were getting deleted.
I had used loop.index to retrieve all images from the database and an if statement to make images switch sides in the desktop gallery. 
Numbers 1, 3, 5, 7 etc. are positioned on the right side of the page. Numbers 2, 4, 6, 8 etc. are positioned on the left side. 
In desktop view, when I tried to delete number 3, 5, 7 or another uneven number, image 1 was getting deleted. When I tried to delete number 2, 4, 6 or another even number, image 2 was deleted. In mobile view (no if statement was used for the mobile gallery), it was always number 1 that was getting deleted.
Actually, the delete function was working fine when there was a button under the image that was linked directly to the delete function. But as a form of defensive programming, the delete button first triggers a modal asking the user if he's sure he wants to delete this image. I linked the confirmation button in this modal to the delete function and that is when the problem arose. 
I tried several things and tested in the desktop view. First, I placed the code for the modal outside of the loop, but this produced a Jinja error: 'image not defined'. That made sense. 
When I placed the modal inside the loop but outside of the if statement, the first image got deleted, no matter which image I tried to delete. In hindsight, that makes a lot of sense too. 
When I placed the modals inside the if statement, numbers 1 and 2 were getting deleted, depending on whether I tried to delete an even or uneven image - which was how it was when I first discovered the bug. 
Tutor support thought at first that it had something to do with **loop.index** at the top of the gallery, so they asked me to change it to **loop.index0**, but this didn't resolve the issue. 
They then suggested to change it to **loop.index -1**. This only made the first image appear on the left side and all other images on the right side. It didn't fix the bug. 
Then they suggested I write **( loop.index - 1)**. But this also did not resolve the issue. 
Then another tutor came online and figured out that at that moment, one generic modal seemed to pop up (or actually two, one for even and one for uneven images), but of course we wanted each image to open its own relevant modal. Looking at the page source in the DevTool, we could see that a modal was in fact created for every single image, but that every modal took the id of numbers one and two. 
It became clear that when a modal (and a delete button inside that) is placed inside a for loop, it does generate a modal for every item in the loop, but that I needed to give each modal and button inside a unique id. The solution was to add **{{loop.index}}** to the modal ID and the data-target of the confirmation button, for each modal (also inside the mobile gallery). This resolved the issue. 

**8: Text input without spaces**<br>
When adding an image to the gallery, a user can fill in the description field with text that doesn't contain any spaces. This turned the input into one long line that runs behind the image and outside of the card-panel, all the way to the end of the screen. One way to prevent this from happening is having a moderator check added images before they are added to the gallery. I thought I would have to traverse the input string to check the length of every word and compare those lengths to a max length of a word, in order to allow or disallow it. But an easy way to resolve the issue was hiding the overflow of the card-panel. 

**9: Being redirected to the wrong page after deleting an image**<br>
A user sees buttons for deleting images on both his profile page and in the gallery under his own images. When a user is in the gallery and deletes an image from there, he is redirected back to the gallery (that has been refreshed, and now no longer has this specific image). However, when the user was on his profile and he deleted an image, he was then redirected to the gallery instead of his profile page. Of course, it makes more sense if the user is redirected to the profile page if that is where he was before. I tried to resolve this using 'request.path' but with a bit of help, I was able to resolve the issue with the following code:
```
url = request.referrer
    url_split = url.split('/')
    current_page = url_split[-1]
```
This checks the page where the user is coming from. I then split the URL at the slash, and have the function check if the part behind the slash corresponds with the profile page. If so, the user is redirected to the profile page. If not, this means that he was coming from the gallery, and is redirected to the gallery:
```
if current_page == "profile_page":
    return redirect(url_for("profile_page"))
return redirect(url_for("get_images"))
```
This resolved the issue. 

**10: Being redirected to the wrong page after editing an image**<br>
There is not only a delete button under each image, there is also an edit button. The same issue presented itself:
When a user is in the gallery and edits an image from there, he is redirected back to the gallery (that has been refreshed, and now shows the updated image). However, when the user was on his profile and he edited an image, he was then redirected to the gallery instead of his profile page.
I thought that the redirecting issue could be solved in the exact same way as I had for the delete function. The code worked just fine with a simple route, in the Delete Image function. So I wrote the following code:
```python
@app.route("/edit_image/<image_id>", methods=["GET", "POST"])
def edit_image(image_id):
    url = request.referrer
    url_split = url.split('/')
    current_page = url_split[-1]
    is_from_profile = False
    if current_page == "profile_page":
        is_from_profile = True
    if request.method == "POST":
        submit = {
            "url": request.form.get("url"),
            "image_title": request.form.get("image_title"),
            "camera": request.form.get("camera"),
            "focal_length": request.form.get("focal_length"),
            "iso": request.form.get("iso"),
            "aperture": request.form.get("aperture"),
            "exposure": request.form.get("exposure"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        mongo.db.images.update({"_id": ObjectId(image_id)}, submit)
        flash("Your image has successfully been updated!", "success")
        if is_from_profile:
            return redirect(url_for("profile_page"))
        return redirect(url_for("get_images"))

    image = mongo.db.images.find_one({"_id": ObjectId(image_id)})
    return render_template("edit_image.html", image=image)
```
(Remark: I chose a bad variable name, 'current_page', I should have chosen 'previous_page'). But as you can see, in the Edit Image function, the route is called twice: first on GET and then on POST. This means that the URL changes between the first and the second call, so my original method (like the one for the Delete function) didn't work. I got the advice to use a hidden input field in my Edit Image Form to save the previous URL.
So what I had to do is:
- On the first call, get the previous URL.
- Pass that URL into the hidden input field in the form. This way, it is intact by the second route call.
- Retrieve the URL from the form on the POST request. 
- Then redirect to it. <br>
This way, the user gets redirected back to the page where he was coming from. 

**11: The scrollspy didn't entirely display on all screen sizes**<br>
I created the website on a large screen. But when I tested the website on other devices, I noticed that on certain medium sized screens, such as my laptop, the scrollspy didn't fit completely. The last two list items fell off the screen. I had several options: either make the height of the banner image smaller, remove certain list items, or stick the scrollspy to the bottom of the page, as low as possible. I chose a combination of the last two. I don't really like how it looks on my larger screen, but at least it now fits on the screens I tested. 

## Unresolved issues
**1: Mobile menu stays open in desktop view**<br>
When a user opens the Chrome DevTool and switches from desktop view to mobile view, he can click on the mobile menu. When switching to desktop view with an open mobile menu, the menu stays visible on the screen.
For now, it doesn't seem to impact user experience, but this might be something to address in the future. 

**2: Other users can edit your image**<br> 
Users can only see the edit and delete buttons under their own images. When a user chooses to edit an image he is redirected to a page with the following url:
http://star-trail-photography.herokuapp.com/edit_image/<image_id>.
Unfortunately, if a malevolent user was to discover the id of someone else's image (for example by checking the browser history), he could copy this id into the URL and will then have the possibility to change this image. 

**3: Page not loading correctly**<br>
Sometimes, a page will load slowly or even incompletely. I have seen this have an effect on the buttons. When this happens the hover effect that I have written usually doesn't override the Materialize CSS, making buttons green (instead of black, grey and white). 

**4: Regain control of a deleted account**<br>
After a user deletes his account, the user is deleted from the database. This means that someone new can then sign up with the previously used username. There will be no error message, because the username is no longer in use. If this former user had uploaded images to the gallery, and hadn't deleted them before deleting his profile (which is what I want: to keep as much images as possible), a new user gains access to these images. He can then edit and/or delete them. 

## Browsers
The final version of the website was tested in different browsers. The website works correctly in Chrome, Opera, Mozilla, Safari, Microsoft Edge and Internet Explorer. 

## Responsiveness
- Whilst building this website, testing to see if the website adjusts itself to the size of the device was mostly done with the Chrome DevTool. Media queries are in place to adapt elements to different screen sizes. 
- At the final stage, the website was tested on my personal devices (Lenovo Ideapad 110, HP Pavilion P6330NL with Lenco Monitor (1920px x 1080px), Huawei P30, Samsung Galaxy S4 mini), and my family's and friends' devices. The website was displayed as intended. 


