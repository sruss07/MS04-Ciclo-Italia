![Header](ms04_testing_header.png)

**Table of Contents**

1. [Code Testing](#code-testing)
  - [Automated Testing](#automated-testing)
  - [Validator Testing](#validator-testing)
2. [User Story Testing](#user-story-testing)
3. [Manual Testing](#manual-testing)
  - [Lighthouse](#lighthouse)
  - [Responsive Testing](#responsive-testing)
4. [Usability Testing](#usability-testing)
5. [Defensive Design](#defensive-design)
  - [Navbar](#navbar)
  - [Footer](#footer)
  - [Login/Signup](#login/signup)
  - [Products](#products)
  - [Checkout](#checkout)
  - [Blog](#blog)
 
Back to [README.md](https://github.com/sruss07/MS04-Ciclo-Italia/blob/master/README.md)

# Code Testing

## Automated Testing

In addition to the full manual testing, I created a few automated tests. 
The automated testing can be improved as I am not 100% confident with automated testing.

11 automated tests were created and run. These include:
- Checkout>tests.py: Order form testing
- Bikes>tests.py: Bike form testing and Bikes page view test

- In the terminal type the following command:
  `python manage.py test <<app name>>`
- The test results will be shown within the terminal.

## Validator Testing 

[W3C Markup Validation](https://validator.w3.org/nu/#textarea)

### HTML 

### Entire app html

- No errors were returned

![HTML](ms4_html_validation.png)

### CSS

### base.css

- 1 error was returned 
    - This error relates to the underline effect when clicking on navbar links and dropdown menu links. The error states that the 'property text-decoration-thickness doesn't exist'. I have chosen to ignore this errror as the css is causing no problems with running the app and the css provides the desired underline effect that was intended

![Base.css](base_css_validator_results.png)

### checkout.css

- No errors were returned

![Checkout.css](checkout_css_validator_results.png)

### profile.css

- No errors were returned

![Profile.css](profile_css_validator_results.png)

 [JSHINT](https://jshint.com/)

 - When run through the [JSHint validator](https://jshint.com/) these metrics were returned:
 
### main.js

![Main.css](ms4_main_js_results.png)

### countryfield.js

![CountryField.css](ms4_countryField_js_results.png)

### stripe.js

![Stripe.css](ms4_stripe_js_results.png)
 
 # User Story Testing

## As an Anonymous User I want the ability to...

- Easily navigate the site
    - User is able to easily navigate the site dur to the clear layout of links and information, both before logging in and after logging in, allowing users to find what they are looking for quickly
- View the site on all screen sizes
    - User is able to view the site satisfactorily on all available devices from desktops to laptops, from tablets to mobiles with all links and information rendered as needed for a n excellent user experience
- Search for and view bikes
    - User is able to seamlessly search for and view all bikes available on the site, including bike descriptions, images and prices
- Filter my search results
    - User is able to use the search facility to find bike brands and models by entering brand name, bike model name or keyword
- Read details about each bike
    - User is able to read details on each available bike when the appropriate bike image is clicked on the bikes page, helping them make an informed choice
- Access Ciclo Italia social media links
    - User is able to navigate to the site footer where they can access social media links for Facebook, Twitter, Instagram, YouTube and Pinterest
- Register for a user profile account with a username and password
    - User is able to easily register an account, confirm registration via the email sent and view their profile with their details saved 
    - To test this, I used [Temp Mail](https://temp-mail.org/en/) to generate a temporary email address to register with
- Verify that my registration was successful
    - User quickly receives an email to inform them that their registration has been completed successfully

## As a Registered User I want the ability to...

- Log in and log out of my profile account
    - User is able to easily log in and log out of the site with the login and logout links
- Update my shipping, billing and payment details
    - User is able to login to their profile and easily update their shipping, billing and payment details
- Store my address for later use
    - User details are easily stored by clicking save my details when completeing a purchase
- Store my purchase history
    - User is able to easily browse their purchase and payment history within their personal profile
- Review my purchase choices at checkout
    - User can review and edit their intended purchase within their shopping cart before making the final decision to buy and proceed to the payment page
- Easily make secure payments 
    - User is able to use the site checkout to safely and securely complete payments and feel confident that their details are protected
- Receive email confirmation of my purchase payment
    - User receives a confirmation email to their inbox upon completion of the purchase checkout procedure
- Create personal bike reviews
    - User is able to create their own bike reviews by clicking on the Add/Edit Bike Review link within the My Account dropdown menu
- Update their personal bike reviews entries
    - User is able to edit their own bike reviews by clicking on the Add/Edit Bike Review link within the My Account dropdown menu
- Delete their personal bike reviews entries
    - User is able to delete their own bike reviews by clicking on the Add/Edit Bike Review link within the My Account dropdown menu

## As a Site Admin/Superuser I want the ability to...

- Add new bike listings
    - Site admin/superuser is able to easily create new bike listings by using the product management link located within the my account dropdown menu
- Update existing bike listings
    - Site admin/superuser is able to easily update existing bike listings when information changes by using the product management link located within the my account dropdown menu
- Delete existing bike listings
    - Site admin/superuser is able to easily delete existing bike listings when certain bikes are no longer available by using the product management link located within the my account dropdown menu
- Create cycling blogs
    - Site admin/superuser is able to easily create new cycling blogs by using the add/edit cycling blog link located within the my account dropdown menu
- Update cycling blog entries
    - Site admin/superuser is able to easily update existing cycling blogs by using the add/edit cycling blog link located within the my account dropdown menu
- Delete cycling blog entries
    - Site admin/superuser is able to easily delete existing cycling blogs by using the add/edit cycling blog link located within the my account dropdown menu
- Create bike reviews
    - Site admin/superuser is able to easily create new bike reviews by using the add/edit bike review link located within the my account dropdown menu
- Update bike review entries
    - Site admin/superuser is able to easily update existing bike reviews by using the add/edit bike review link located within the my account dropdown menu
- Delete bike review entries
    - Site admin/superuser is able to easily delete existing bike reviews by using the add/edit bike review link located within the my account dropdown menu


:arrow_up: [Back to top](#code-testing)

# Manual Testing

## Lighthouse 

- An audit was completed using Lighthouse on the Rivercity jewellery. 
- Quite a low performance but upon completing audits of several other websites, such as: 
    - [Code Like a Girl](https://code.likeagirl.io/) 
    - [Medium](https://medium.com/) 

I learned that higher markings in Accessibility, Best Practices & SEO were more frequent than having a high-performance rating.

![Lighthouse](lighthouse.JPG)

## Responsive testing

### Desktop Testing

| Page          | Responsive    | Notes |
| :------------- |:-------------:| :---------------:|
| Index     | Y    | Fully Responsive. No horizontal scrollbar.  |
| Products      |    Y   | Fully Responsive. No horizontal scrollbar.   |
| Product Details |    Y   |  Fully Responsive. No horizontal scrollbar. The Image is rather large   |
| Shopping Bag |   Y   | Fully Responsive. No horizontal scrollbar. Easy to read   |
| Checkout |    Y  | Fully Responsive. No horizontal scrollbar.     |
| Checkout Successful |    Y   |   Fully Responsive. No horizontal scrollbar. Checkout success message is helpful |
| Blog |   Y  | Fully Responsive. No horizontal scrollbar. Blog posts are easily distinguisable    |
| Blog Details|   Y   | Fully Responsive. No horizontal scrollbar. Easy to read commet secton    |
| Sign Up |   Y    |   Fully Responsive. No horizontal scrollbar. Footer is not fixed to bottom  |
| Login |    Y   |   Fully Responsive. No horizontal scrollbar. Footer isn't fixed to bottom  |

### Tablet Testing

| Page          | Responsive    | Notes |
| ------------- |:-------------:| :-----:|
| Index      | Y | Fully responsive, no horizontal scrollbar  |
| Products      |   Y    |  Fully responsive, no horizontal scrollbar. 2 products per row work well  |
| Product Details |  Y     |   Fully responsive, no horizontal scrollbar. Product details easy to read  |
| Shopping Bag |   Y   |   Fully responsive, no horizontal scrollbar   |
| Checkout |    Y  |   Fully responsive, no horizontal scrollbar   |
| Checkout Successful |  Y     |  Fully responsive, no horizontal scrollbar   |
| Blog |  Y   |   Fully responsive, no horizontal scrollbar. Blog post easy to read  |
| Blog Details|  Y    |   Fully responsive, no horizontal scrollbar. Comment section easy to read  |
| Sign Up |  Y     |   Fully responsive, no horizontal scrollbar   |
| Login |  Y     |   Fully responsive, no horizontal scrollbar   |

### Mobile testing

| Page          | Responsive    | Notes |
| :-------------: |:-------------:| :-----:|
| Index      | Y| Fully Responsive, footer looks nice |
| Products      |   Y    |  Fully responsive there is noticable whitespace above header. Images better size |
| Product Details |  Y     |   Fully responsive, added product to bad, success message works well  |
| Shopping Bag |    Y  |   Fully responsive with totals at the top of the page for easy reading  |
| Checkout |   Y   |  Fully responsive, order summary and checkout form works well. Country easy to select on iPhone. Card details easy to enter with number pad on iPhone   |
| Checkout Successful |   Y    | Fully responsive,  success message easily read. Buttons to blog responsive |
| Blog |   Y  |   Fully responsive, easy to see which post I would like to read  |
| Blog Details|    Y  |  Fully responsive, article read, image a good size, comment section responsive   |
| Sign Up |   Y    |  Fully responsive , no horizontal scrollbar   |
| Login |    Y   |  Fully responsive, no horizontal scrollbar   |

# Usability Testing
- A site-wide usability test was conducted. I asked my partner to help participate in the testing. The user was presented with the following aims:
    - You are an avid jewellery enthusiast. You are interested in buying yourself a new piece of jewellery at a treat, you deserve it!
    - Navigate to the Home page to see if you would prefer to go stright to the product or check out the blog.
    - You decide that you would like to know more about jewellery, so you head to the blog. You browse through the blog list and pick a post to read in full.
    - You decide you would like to set up your own profile page, enter your details for convenience. You register with your email and confirm your registration by following the link sent to you via email. 
    - You know would like to buy a pair of earrings. You navigate to the 'Earrings' button and decide to check out 'All Earrings'
    - You have great taste so you decide to buy a pair of the Skew Silver Hoops. 
    - Now you add the earrings to your bag and head to checkout 
    - You should now be able to easily enter your shipping details, card details and complete the order. 
    - The payment went through, you can now review your order on the site and in the email that was sent to your email address, your item is on the way! 
    - You can now see a breakdown of your Rivercity jewellery purchases on your profile page! 

- User Testing Feedback
    - I was able to easily checkout a product, received the email and had a read through the blog. 
    - More work on the buttons for each page would be nice, making all product images the same size would be good as well

# Defensive Design

## Navbar
- All links were tested & deemed to be fully functional, directing users to the desired location.
- Logo redirects the user to the index page

## Footer
- Icons navigate to relevant external links when clicked & a new tab is opened for navigating to this page.

## Login/Signup
- Links in these pages functioned correctly
- Buttons performed desired actions.
- Required fields in forms rendered an error when not filled correctly.
- Messages displayed if the information was submitted incorrectly.

## Products
- All links to other pages were checked & deemed rendering correctly.
- Buttons performed the desired actions.
- Any forms that needed to be filled out flashed relevant errors if filled incorrectly.
- Error messages flashed as desired when forms or pages were submitted incorrectly.

## Checkout
- All links to other pages were checked & deemed rendering correctly.
- Any forms that needed to be filled out flashed relevant errors if filled incorrectly.
- Error messages flashed as desired when forms or pages were submitted incorrectly.

## Blog
- All links to other pages were checked & deemed rendering correctly.
- Any forms that needed to be filled out flashed relevant errors if filled incorrectly. 

![testing](https://media.giphy.com/media/3orieKKmYyvUdR3RkY/giphy.gif)

[Back to top](#code-testing)

Back to [README.md](https://github.com/lucyrush/rivercity_jewellery#table-of-contents)