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



<summary>models.py</summary>
<br>
<img src="">
<br>
<summary>views.py</summary>
<br>
<img src="">
<br>
<summary>urls.py</summary>
<br>
<img src="">
<br>
<summary>form.py</summary>
<br>
<img src="">
<br><br>

