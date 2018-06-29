
# Ride-My-Way
Repository for Andela Kenya Cohort 29 Bootcamp Developer Challenge.

The Ride My Way application uses the power of the web to improve the car-pooling experience. 
The app makes it possible for drivers to create ride offers for passengers to join available ride offers.

# Author:
    Brian Wandera (@wandesky)

# What to expect
    On successful completion of this branch (UI), the app should have the following front end features;
    - Registration page
    - Login page
    - A page that displays all available rides
    - A page to interact with a ride offer (see details of ride and respond)
    - A page to post a ride offer
    - A page that drivers can use to view and accept/reject rides they have created
    - A feature for users to view number of rides taken/given and list all rides 

## Want to have a look at the work done so far
You can have a preview of the work done using the link below;
    https://wandesky.github.io/Ride-My-Way/UI

#The API (rmw-v1)
The API is python based developed using Flask. It is used to keep track the rides created and taken.
The API makes it possible for services to connect to the required endpoints when listing all available rides,
getting a specific ride, creating a ride offer and requesting to join a ride.

# Specifications

| EndPoint | Functionality |
| ------------- | ------------- |
| GET /rides | Fetch all ride offers  |
| GET /rides/<rideId> | Fetch a single ride offer  |
| POST /rides | Create a ride offer |
| POST /rides/< rideId >/requests | Make a request to join a ride |
|  |  |


# Installation


   i. Clone or download the repository
      `git clone https://github.com/wandesky/Ride-My-Way.git`
      `git checkout api-v1`

   ii. Create a virtual environment
      `virtualenv rmw-v1`
      In windows `mkvirtualenv rmw-v1`

   iii. Activate the environment 
      `source rmw-v1\bin\activate`
      in windows use `rmw-v1/Scripts/activate`

   iv. Install the environmmental requirements from the file within the virtual venv
       `pip install -r requirements.txt`

# ride-my-way-2