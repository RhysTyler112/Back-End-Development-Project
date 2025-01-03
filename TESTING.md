<img src="">
<br><br>

# Testing documentation for Onyx | Gym Web application.
<br><br>

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
    * [WAVE Accessibility](#wave-accessibility-checker)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [Member User](#member-user)
    * [Employee/PT User](#employeept-user)
    * [Managment User](#management-user)
* [Manual Testing](#manual-testing)
* [Responsiveness](#responsiveness)

<br><br>

# Validation

## HTML Validation

All pages pass HTML Validation at [W3C markup validation service](https://validator.w3.org/) with no site breaking errors or warnings. 


<summary>Homepage</summary>
<br>
<img src="static/README/validation/homepage-checker.png">

<summary>Create a Booking</summary>
<br>
<img src="static/README/validation/create-booking-checker.png">

<summary>My Bookings</summary>
<br>
<img src="static/README/validation/my-bookings-checker.png">

<summary>Log In</summary>
<br>
<img src="static/README/validation/login-checker.png">

<summary>Log Out</summary>
<br>
<img src="static/README/validation/logout-checker.png">

<summary>Register</summary>
<br>
There was 4 errors on the registar html do to the html format used by allauth that I can not chanage, this is something I look to update myself in the future.
<br>
<img src="static/README/validation/registar-checker.png">

<summary>Edit Booking</summary>
<br>
<img src="static/README/validation/edit-booking-checker.png">

<summary>404 Error</summary>
<br>
Had to check the code manually for this one as checking via url would bring up IO Error: HTTP resource not retrievable. There are 2 errors showing due to it not liking the Django syntax for links. Otherwise all working correctly with no working issues.
<br>
<img src="static/README/validation/404-checker.png">

<summary>500 Error</summary>
<br>
<img src="#">
<br><br>

## CSS Validation

All pages pass CSS Validation at [W3C CSS validation service](https://jigsaw.w3.org/css-validator/) with no errors or warnings.


<summary>CSS Validation</summary>
<br>
<img src="static/README/validation/css-checker.png">
<br><br>

## JS Validation

Custom JS script file run through [JShint](https://jshint.com/) for validation. Shows one undefined but as this is part of the script get bootstap modal to work and one warning I have chosen to ignore these as the components work as expected.

<summary>JS Validation</summary>
<br>
<img src="static/README/validation/js-checker.png">
<br><br>

## CI Python Linter
All python files run through CI PEP8 Linter and passed with no warnings, with the exception of the E501 line too long (84 > 79 characters). I beleive this has no impact on the function of the b page so I have left it as it is.


<summary>models.py</summary>
<br>
<img src="static/README/validation/models.py-checker.png">
<br>
<summary>views.py</summary>
<br>
<img src="static/README/validation/view.py-checker.png">
<br>
<summary>urls.py</summary>
<br>
<img src="static/README/validation/urls.py-checker.png">
<br>
<summary>form.py</summary>
<br>
<img src="static/README/validation/form.py-checker.png">
<br><br>

## Lighthouse


<summary>Homepage - Best practices has a lower score as report states "Does not use HTTPS" this is something I am unware how to fix as we are host the project on a 3rd aprty site Heroku.
</summary>
<br>
<img src="static/README/lighthouse/homepage-lighthouse.png">
<br>
<summary>Register - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/signup-lighthouse.png">
<br>
<summary>Log In - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/login-lighthouse.png">
<br>
<summary>Sign Out - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/signout-lighthouse.png">
<br>
<summary>My Bookings - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/my-bookings-lighthouse.png">
<br>
<summary>New Booking - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/new-booking-lighthouse.png">
<br>
<summary>Edit Booking - Good Scores.</summary>
<br>
<img src="static/README/lighthouse/edit-booking-lighthouse.png">
<br>
<summary>404</summary>
<br>
<img src="">
<br>
<summary>500</summary>
<br>
<img src="">
<br>

## WAVE Accessibility Checker

<summary>Homepage - No errors or contrast errors, two alerts for redundant links as Home link is present in both Nav logo and Nav link, one with 2 classes with the same name, this is needed as they are on differnt days.
</summary>
<br>
<img src="static/README/wave/homepage-wave.png">
<br>
<summary>Register - No errors, 1 contrast error, seems to be the colour of the text for the sign up link, I beleive this is easy to see but will look to darken in future updates. Same alerts as Homepage.</summary>
<br>
<img src="static/README/wave/signup-wave.png">
<br>
<summary>Log In - No errors, same contrast and alertes as register.</summary>
<br>
<img src="static/README/wave/signin-wave.png">
<br>
<summary>My Bookings - </summary>
<br>
<img src="">
<br>
<summary>New Booking - No errors or contrast errors.</summary>
<br>
<img src="static/README/wave/new-booking-wave.png">
<br>
<summary>Edit Booking - </summary>
<br>
<img src="">
<br>
<summary>404 - No errors, 1 contrast error, seems to be the colour of the button that links them back to the homepage
</summary>
<br>
<img src="static/README/wave/404-wave.png">
<br>
<summary>500 No errors, 1 contrast error, seems to be the colour of the button that links them back to the homepage
</summary>
<br>
<img src="static/README/wave/500-wave.png">
<br>
