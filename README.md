# pymongo-dashboard
This is a Jupyter Dash application with python CRUD functionality.
Programs that are written with consistency and reusable code ensure maintainability, readability, and adaptability. Developing the CRUD python module first helped to ensure the database could be easily manipulated once it was integrated with the dashboard interface. The purpose of this project was to improve the current system for user experience.

### About the Project/Project Title
 This software application works with existing data to help locate available dogs by providing a dashboard and the database interface logic using Python, MongoDB, and Jupyter Dash. 
This fully functional MongoDB dashboard allows the mock client, Grazioso Salvare, to interact with and visualize the database.The user-friendly dashboard is an intuitive interface that reduces user errors and training time while ensuring access restrictions through the use of Authentication.

### Motivation
This is a project for an innovative(and mock) international rescue-animal training company, Grazioso Salvare. Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs are able to find and help to rescue humans or other animals, often in life-threatening conditions. To help identify dogs for training,  data from a mock non-profit was provided. The purpose of this project is to demonstrate the CRUD functionality in Python using MongoDB.

### Getting Started
To get a local copy up and running:  
 Run ‘mongod_ctl start’   
Find your Port number:
![image](https://user-images.githubusercontent.com/56535394/197425273-446f59ec-0234-4524-bcd5-13e2ba135b4d.png)

Use ‘localhost’ + your Port number in the AnimalSheter class init  function
![image](https://user-images.githubusercontent.com/56535394/197425358-87f1cf92-b50f-4e51-8347-d538c92d2511.png)

Enter the username followed by the password for the database being used. 
The database here is titled ‘AAC.’  
![image](https://user-images.githubusercontent.com/56535394/197425378-6ae344b3-76ef-405a-ad1f-6264f6be0bc6.png)

Open the ‘Project Two’ folder in Jupiter notebook: 
![image](https://user-images.githubusercontent.com/56535394/197425405-c8d71957-ef26-4d5e-b2da-d87fa783b23d.png)

Then, Open and Run the ‘Project2__JoannCarter.ipynb’.


 After running the IPYNB file, you will see an interactive data table that responds to input from the four radio buttons that filter the results by types of Rescue Dogs. Interactive radio buttons are used to filter the Austin Animal Center Outcomes data set. The initial state is set to reset which shows all the unfiltered data.  
 
Reset Search Results(shows all the Dog data):
![image](https://user-images.githubusercontent.com/56535394/197425444-7f03e579-00a0-4ae1-803b-b354f7d63ee5.png)

Water Rescue Filter:
![image](https://user-images.githubusercontent.com/56535394/197425473-399b2bce-016a-47a2-8d79-f32c7cdc7147.png)

Mountain  Rescue Filter:
![image](https://user-images.githubusercontent.com/56535394/197425486-578e732f-8d0f-429b-84bc-c027f318e3e9.png)

Disaster Filter:
![image](https://user-images.githubusercontent.com/56535394/197425501-3f25b266-18e5-45c2-81ca-f058f390b7c0.png)

The number of rows displayed has been limited to three to ensure the user sees the graphs located below the chart( and radio button filtering options). Pagination is incorporated and located at the bottom of the chart to provide access to more data not yet shown on the screen. The two graphs below the chart are a map and a pie chart. The pie chart dynamically responds to the radio button filtering options. Examples of this are demonstrated above.

The geolocation chart/map also dynamically responds to the radio button filtering options. Examples of this can be seen in the examples above. Furthermore, a pin is shown on the map to represent the location of the first Rescue Dog shown in the data table. The first picture below demonstrates how the map looks without any interaction by the user. When the user hovers over the pin, a tooltip shows the breed of the dog at this location. An example can be seen in the second image below. When the user clicks on the pin, more information about the Rescue Dog at that location is shown. An example can be seen in the third image below. 

![image](https://user-images.githubusercontent.com/56535394/197425580-b752c9ed-eccd-411f-b19f-4bd544b67603.png) ![image](https://user-images.githubusercontent.com/56535394/197425543-3cd674ee-d622-4be6-9e2f-31f2117e7e2d.png) ![image](https://user-images.githubusercontent.com/56535394/197425591-998eb743-7864-4c1f-888e-1040960d7095.png)

## Installation

### TOOLS:
Jupyter Notebook- https://jupyter.org/install  
MongoDB- https://www.mongodb.com/docs/manual/  
Jupyter Dash- https://dash.plotly.com/installation  

### LIBRARIES:
PyMongo is used as the Python driver for Mongo because of the bson package 		that is implemented to convert the dictionary cursor into json format.
```
from pymongo import MongoClient
from bson.objectid import ObjectId
```

Jupyter Dash is used as the framework for the dashboard.
![image](https://user-images.githubusercontent.com/56535394/197426180-f7d32dc5-6a84-4500-bef5-d122d1fd4fc4.png)

Base64 is used to encode the mock companies logo.
![image](https://user-images.githubusercontent.com/56535394/197426197-7ad715f4-61bb-4de0-86e2-c2984c358dd7.png)

This line imports the CRUD functionality from the animal_shelter.py file located in the ‘Project Two’ folder:
![image](https://user-images.githubusercontent.com/56535394/197426217-0549e2a8-87cb-4a93-a830-2fdcd63bf515.png)


## Usage
### Code Example
Create and Read functions for dictionary data. The next example uses the database ‘AAC’ with the collection ‘animals.’
![image](https://user-images.githubusercontent.com/56535394/197426245-38c6ccb0-b4e2-49da-a0d5-13c12e077b0c.png)

Update and Delete functions for dictionary data. This example uses the database ‘AAC’ with the collection ‘animals.’ To update the data with the new information is validated first. Then, the cursor is found from calling the read method. Then the cursor is looped through to find the associated animal ID. This is in case the user doesn't know the animal idea off the top of their head. Then the updated info is stored in a separate cursor. Finally, the cursor is returned in JSON format with the dumps method from bson.
To delete the data the animal ID is first I looked for in a list of the dictionary documents. Then, the document is deleted.
![image](https://user-images.githubusercontent.com/56535394/197426275-598d2725-9f4e-42d9-a893-407bdb4ff672.png)

### Tests
The steps of this test are as follows:  
Create an instance of the class and assign it data.  
Then, print ‘animal added’ if the create method works.  
Then, print the animal data and “animal read” if the read method works.  
* Note: this test is not included in this version.  
![image](https://user-images.githubusercontent.com/56535394/197428265-f45ccc75-991d-48dc-89b9-da4bd90c438d.png)
Below is an example of the test script running correctly for the data seen above.  
![image](https://user-images.githubusercontent.com/56535394/197428271-78261e31-fd8d-4e9f-9f09-a834652009d1.png)

Below is a screenshot of the test animal shelter file. There is data created for a mock document and new data instantiated for later use. The variable shelter instantiates the object animal shelter using the username and password. This is example uses the command shelter.create(data) and the boolean value True.
Next the shelter is updated with the new data variable. This returns the JSON format that includes the new data. 
![image](https://user-images.githubusercontent.com/56535394/197428333-2817e0bc-5d11-44ea-819f-0bedcad34294.png)

The delete results:
![image](https://user-images.githubusercontent.com/56535394/197428356-c9eb32d9-124c-4391-ac5b-58d92af93e94.png)
Screenshots:  Photo credit: screenshots from my laptop September, October 2022

### Roadmap/Features/Roadblocks
#### Roadmap:
As of now, there are no future plans for this project as it is completed and the first 	version has been released.
#### Roadblocks:
Rendering the filtered data with the radio buttons was trivial. The issue was solved by 	removing the component ‘id’ from the return statements in the update_graph and 	update_map functions located in ‘Project2__JoannCarter.ipynb.’
#### Contact
Joann Carter





