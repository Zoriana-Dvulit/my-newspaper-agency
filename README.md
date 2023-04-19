# my-newspaper-agency

## Setup

#### Getting Started

First clone the repository from Github and switch to the new directory:

`git clone https://github.com/Zoriana-Dvulit/my-newspaper-agency.git`

cd my-newspaper-agency

#### Activate the virtualenv for your project.

Run the following command to install project dependencies:

`pip install -r requirements.txt`

These instructions assume you have Python 3 and pip (>= v20.3) installed.

#### Run locally

1. Create a virtual environment:

`python3 -m venv venv`

2. Activate the virtual environment:

`source venv/bin/activate`

3. Install the necessary packages:

`pip install -r requirements.txt`

#### Environment Variables

This project uses environment variables to store sensitive information. To set up the environment variables:

1. Copy the `.env_sample` file and rename it to `.env`.

2. Replace the sample values in the `.env` file with your actual values.

3. Add `.env` to the `.gitignore` file to prevent sensitive information from being committed to the Git repository.

**Note:** You can find samples of the required environment variables in the `.env_sample` file.

4. Migrate the database:

`python manage.py migrate`

5. Run the development server:

`python manage.py runserver`

_The API will now be available at_ http://localhost:8000/.

#### Registering and Logging In

To use our API, you'll need to create an account and log in to authenticate your requests.

Here's how you can do that:

##### 1. Register

To register for an account, send a POST request to /api/auth/register/ with your email, username and password
You should receive a response with a token field that you'll need to use to authenticate future requests.

##### 3. Login

To log in to your account, send a POST request to /api/auth/login/ with your email and password
You should receive a response with a token field that you'll need to use to authenticate future requests.

##### 4. Authenticating Requests

To authenticate your requests, you'll need to include an Authorization header in your request with the value
Token <your-token> where <your-token> is the token you received when you registered or logged in.

#### Test user credentials

To test the app, you can use the following test user account:

- Username: `testuser`
- Email: `testuser@example.com`
- Password: `password`

#### API Endpoints Descriptions

###### Topics

[GET] /api/newspaper/topics/ - Receive a list of topics

[GET] /api/newspaper/topics/int:pk/ - Receive details of a specific topic

[POST] /api/newspaper/topics/create/ - Create a new topic

[PUT] /api/newspaper/topics/int:pk/update/ - Update details of a specific topic

[DELETE] /api/newspaper/topics/int:pk/delete/ - Delete a specific topic

###### Newspapers

[GET] /api/newspaper/newspapers/ - Receive a list of newspapers

[GET] /api/newspaper/newspapers/int:pk/ - Receive details of a specific newspaper

[POST] /api/newspaper/newspapers/create/ - Create a new newspaper

[PUT] /api/newspaper/newspapers/int:pk/update/ - Update details of a specific newspaper

[DELETE] /api/newspaper/newspapers/int:pk/delete/ - Delete a specific newspaper

[POST] /api/newspaper/newspapers/int:pk/toggle-assign/ - Toggle assign a specific topic to a specific newspaper

###### Redactors

[GET] /api/newspaper/redactors/ - Receive a list of redactors

[GET] /api/newspaper/redactors/int:pk/ - Receive details of a specific redactor

[POST] /api/newspaper/redactors/create/ - Create a new redactor

[PUT] /api/newspaper/redactors/int:pk/update/ - Update details of a specific redactor's experience

[DELETE] /api/newspaper/redactors/int:pk/delete/ - Delete a specific redactor

**Note:** int:pk refers to the primary key (ID) of the object in the database.

#### Uploading fixtures

This project uses fixtures to store initial data.

To load initial data fixtures, make sure the fixture file is named "initial_data".
Run the following command to apply the fixture data to the database:

`python manage.py migrate`
