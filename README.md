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

**<details><summary>[Support](#support)</summary>**
</details>

---

## User Experience (UX)

### User Stories



### Strategy

The target demographic encompasses riders from 18 upwards who have the desire and finanacil freedom to own a beautiful and finely crafted Italian road bike. 

This demographic will include riders of all abilities, from weekend leisure riders, to daily commuters, to serious amateur road racers, semi-professional riders and fully professional team riders.

Riders purchasing from the site for competitive reasons will most likely be competing in road racing, time trialling, triathlon and cyclocross events.

The site attempts to provide to its users an attractive, user friendly experience and functionality, which allows customers to easily find the bike of their dreams at an affordable price.

Ciclo Italia provides a high quality selection of Italian designed road bikes providing customers with high quality imagery, detailed descriptions, various sizes and colours, customers reviews and competitive pricing, to allow informed decisions before purchases are completed.

The main strategy of this site to provide accurate information about the products offered, make it easy and intuitive to navigate and transparent with information to maintain trust and integrity with users.

#### Project Goals

To provide customers with a comprehensive, attractive and user friendly site that showcases all the best Italian designed road racing bikes

#### User Goals

Users can easily find their desired bike in the correct size and colour, read reviews on each bike and choose whether to complete a purchase.

### Scope

Project eflects my current skill-set of HTML, CSS, JavaScript, Python and Django.

Provide a site with relevant categories, product listings and detail pages, with scope for future expansion

#### Existing Feature

- Fully responsive website for all common mobile, tablet and desktop devices, using Bootstrap responsive grid and custom media queries
- Striking home page jumbotron image to convey a positive initial response from to visitors
- Intuitive and responsive Navigation menu with associated links and search facility
- Brands link to Brands page containing images and details of available bikes
- Search function with filtering.
- Login page with form
- Profile/account page containing personal details, payment details and order history
- Checkout page with payment functionality
- Reviews page containing customer reviews of products
- Blog page containing cycling themed blog posts
- Footer element with social media icon links
- Project management page for adding, updating and deleting products
- Blog management page for adding, updating and deleting blog entries.

#### Future Features to Implement

- Membership scheme to save on future purchases and a members forum area for sharing cycling information such as routes, holidays, maintenance tips, equipment recommendations etc

### Structure

The overall structure is aimed at ease of navigation to each section and an intuitive path from initial arrival on the home page through finding the desired product and finally to a smooth and secure final payment checkout experience

#### Interaction Design

The content has been laid out in an intuiitive way, providing a good flow of information. The home page clearly leads to the brands page where customers can easily browse through all available products. Purchases can be easily made from the brands page through an easy to use payments page 

Clear feedback is provided to the user after each interaction, using the messages function in Django

#### Information Architecture

TBA =========> navigational SCHEMA. ![Site Info Schema]()  

The main organising principle for the user is the brand, with each brand section containing a number of available models

- Search by keyword
- Search by brand
- Search by model name
- Search by size
- Search by colour

#### Database

Development - SQLite3
Production - Heroku Postgres

#### Data Schema

TBA =========

### Skeleton

#### Page Structure

![page structure diagram](docs/wireframes/)

#### Wireframes

[MOBILE WIREFRAMES](docs/wireframes/)
[TABLET WIREFRAMES](docs/wireframes/)
[DESKTOP WIREFRAMES](docs/wireframes/)

The layout has been kept consistent throughout the site with the navigation bar and footer consistemt to all pages

- Top Navigation bar - Menu with links pointing to each page, inluding:
  - brands page
  - offers page
  - reviews page
  - blog page
  - login page
  - profile page
  - Footer with social media links
  

