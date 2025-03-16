# AEP_Chinook_Reference_Project

#### Roles
Developer - Phillip Gachnang
<br>Documentation - Charuta Pande
<br>Tutorials - Sandro Schwander, Kyrylo Buga
<br>Coaches - Christian Schmid, Faruk Doganci, Kyrylo Buga, Phillip Gachnang, Sandro Schwander, Charuta Pande

# Project Structure
The project has a modular structure is divided into logical layers. Each layer performs a single responsibility. The project uses Object-oriented concepts and Python's import system for communication between layers. Let's understand the layers from right to left:

[![](/images/Project_Structure.png)]

1. The **database** layer has the actual database (sqlite file(s) that represent(s) the data storage).

2. The **model** layer is responsible for transporting data between other layers as data objects. Every class in this layer corresponds to an entity in the database and defines functions to get and set properties that correspond to the attributes of that entity. The classes in this layer follow the naming convention ```<entity_name>.py```, where entity_name corresponds to the names of the entities in the database.
<br>*Note that every new class added to this layer should be included in the ```__init.py__``` file so that it can be imported from other layers.* 

3. The **data_access** layer is responsible for interacting with the database, i.e., performing CRUD operations. All SQL queries/DML statements are written in this layer. The classes in this layer follow the naming convention ```<entity_name>_dal.py```, where entity_name corresponds to the database entity on which CRUD operations will be performed.
<br>*Note that every new class added to this layer should be included in the ```__init.py__``` file so that it can be imported from other layers.*

4. The **business_logic** layer is responsible for applying any business logic. The classes in this layer follow the naming convention ```<entity_name>_manager.py```, where entity_name corresponds to the entity on which business logic will be applied before either a. saving information in the database or b. presenting the information to the user.
<br>*Note that every new class added to this layer should be included in the ```__init.py__``` file so that it can be imported from other layers.*

5. Lastly, the **ui** layer is responsible for handling input from the user. It includes a helper class to validate user input and inform the user if the input needs to be corrected. The final output presented to the user is handled in Deepnote notebooks - see section [Working with Notebooks](#working-with-notebooks) for more details.


# How to Start
1. Create a new (empty) repository on GitHub
2. Create a new project on Deepnote
3. Create an integration with the repository created in 1. above (see video tutorials on Moodle)
4. Create the project structure inside the root repository:
    - Create a new folder model - Create all model classes here
    - Create a new folder database - Add your .db sqlite file in this folder
    - Create a new folder business_logic - Add all manager classes here
    - Create a new folder data_access - Add all dal classes here
    - Create a new ui folder - You may reuse the input_helper.py provided in the reference project
5. Share the Deepnote project with collaborators - assign execute access to each member. Provide access to <u>all coaches</u> in the final deliverable.

We suggest that <u>one member</u> from every team follows the above steps. The current repository and the corresponding Deepnote project are for reference only. Please avoid cloning/duplicating them to start on your project - you may run into issues.

# Working with Notebooks
Notebooks are a way to showcase your user stories. You may create multiple notebooks, import required modules/classes and demonstrate how your user stories work. 
- Add a new notebook and give it an appropriate name
- Click on the 3 dots next to the notebook and set the working directory to the folder corresponding to your GitHub repository. For e.g., if your repository is called Hotel_Reservation, set the working directory to ```/Hotel_Reservation```. You will be prompted to restart the machine after changing the working directory. Ensure that you have created a GitHub integration before this step.
- Add notebooks to GitHub on a regular basis - refer to the section [Commit to GitHub](#commit-to-github).

*Alternatively, you may work with an IDE like PyCharm. This requires a slightly different setup than working with Notebooks. Please contact your coach if you prefer this approach. However, in this module, notebooks is the recommended way to showcase your user stories*. 

Refer to MediaShop and DateExample notebooks in the reference project. View the reference project in [Deepnote](https://deepnote.com/workspace/charutapande-cdd21ef1-81ef-478b-bad4-3126daa688f2/project/AEP-Reference-Project-4e94a061-aa40-40c5-852c-78ff3f280c82/notebook/Notebook-1-fd5bf4d4c1cb447797824210a20c4d24?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=4e94a061-aa40-40c5-852c-78ff3f280c82).


# Documentation
Describe the overall documentation for your project in the GitHub ReadMe.md file. This may include the contributors, their roles, your methodology/project management and overall reflection. Include links to the Deepnote project, Project Board etc. directly in the ReadMe.md file.

Include any documentation specific to the user stories like instructions to run the notebook, explanation of output etc. directly in the notebook. You need not duplicate this information in the GitHub ReadMe.md file.

## Commit to GitHub
Define milestones in your project to commit your changes to GitHub on a regular basis. Do ensure that your code including the notebooks is error-free! Refer to the videos on Moodle to understand how to work with GitHub from Deepnote.