# Django-GraphQL-API withStrawberry

This repository contains a simple GraphQL API built using Django and the Strawberry library.
It serves as a basic template for building GraphQL APIs in Django.  If you're new to GraphQL or looking to explore
its implementation with Django, this project is an excellent starting point.

## Features

- Built on Django: The popular web framework.
- GraphQL API: Utilizes GraphQL for flexible and efficient data retrieval.
- Strawberry Library: Incorporates the Strawberry librfary to define GraphQL schema.
- SQLite Database: Comes with Django ready to use.
- Scalable and Customizable: Provides a foundation for expanding your GraphQL API.
- Beginner-Friendly: Ideal for those new to GraphQL APIs.

## Getting Started

To run this project loally and explore the GraphQl API:

1.  Clone the Repository:
```
    git clone https://github.com/Jkhall81/Django-GraphQL-API.git
    cd Django-GraphQL-API
```
2. Install Dependencies
```
  pip install -r requirements.txt
```
3. Apply Migrations
```
python manage.py migrate
```
4. Run the Development Server:
```
python manage.py runserver
```
5. Explore the API:

Open your browser and navigate to 'http://localhost:8000/graphql/'.  You can use the GraphiQL interface
to interfact with your GraphQL API.

6. Start Building Your API:

Customize the schema, define your models, and create new queries and mutations according to your proejct's requirements.
