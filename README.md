

### About the Project
**Author**: Alexander Wagner  
**Project Title**: CRUD Operations and Dashboard for Animal Shelter Database  

This project is a full-stack web application that facilitates CRUD (Create, Read, Update, Delete) operations on a MongoDB database managing animal shelter data. It also provides an interactive dashboard for users to interact with the data, visualize information, and filter records based on specific criteria. The dashboard is built using the Dash framework, and the CRUD operations are handled using PyMongo for MongoDB integration.

The application was developed for the CS-340 Client/Server Development course. The primary goal is to manage animal shelter data efficiently while providing meaningful visual insights to the user.

### Reflection

**How do you write programs that are maintainable, readable, and adaptable?**  
I write programs that are maintainable, readable, and adaptable by following best practices such as organizing code into reusable modules, using meaningful variable and function names, and implementing clear documentation and comments. For example, in my CRUD Python module, I separated the database operations from the rest of the application, making it easier to maintain and extend. This modular approach ensures that if any part of the code (e.g., the database connection) needs updating, it won’t affect the rest of the system. Additionally, by using well-documented libraries like Dash and PyMongo, I ensure that others can easily understand and modify my code in the future. The CRUD module could be reused in other projects requiring similar database operations, enhancing its adaptability.

**How do you approach a problem as a computer scientist?**  
When approaching a problem, I first break it down into smaller tasks, which makes it easier to manage. For example, in this project, I divided the task into distinct components such as authentication, CRUD operations, data visualization, and user interaction. This compartmentalization allowed me to tackle one part at a time and build upon each successful milestone. My approach to this project was more structured than previous assignments, as I incorporated more advanced features like interactive filters and data export. Moving forward, I plan to use more design patterns and perhaps even cloud-based database solutions to meet other client requests in a scalable way.

**What do computer scientists do, and why does it matter?**  
Computer scientists create solutions that simplify complex data and enhance decision-making processes. In this project, the dashboard I developed improves data accessibility and usability for teams managing rescue operations. By making shelter data easier to analyze, update, and visualize, the tool supports strategic decisions on animal rescue and training. This work highlights how computational tools can streamline operations, ultimately boosting the impact and effectiveness of rescue initiatives.

---

### Motivation
The aim of the project is to develop a robust and user-friendly interface for managing animal shelter data, providing users with the ability to easily add, retrieve, update, and delete records. Additionally, the interactive dashboard allows users to explore the shelter data visually, making it easier to identify trends and gain insights.

### Getting Started
To begin using this project:
1. Ensure that Python 3.x and MongoDB are installed on your machine.
2. Clone the repository to your local machine. After cloning, confirm that MongoDB is running locally.
3. Create a database named `AAC` and a collection called `animals`. Import animal records into the `animals` collection using the `aac_shelter_outcomes.csv` file.

Import data using:
```bash
mongoimport --host localhost:27017 --username aacuser --password YourPassword123 --authenticationDatabase admin --db AAC --collection animals --type csv --file "C:\Your\Path\aac_shelter_outcomes.csv" --headerline
```

4. Install the required Python dependencies:
```bash
pip install pymongo dash dash-leaflet plotly pandas notebook
```

5. Run Jupyter Notebook to test CRUD operations:
   ```bash
   jupyter notebook
   ```
6. Open the notebook and import `animal_shelter.py`.

### Usage
Once your environment is set up and MongoDB is running, you can interact with the animal shelter database using the CRUD operations in `animal_shelter.py`. Examples:

```python
from animal_shelter import AnimalShelter
shelter = AnimalShelter(username="aacuser", password="SNHU1234")

# Create a new record
new_animal = {
    "animal_id": "A123457",
    "animal_type": "Dog",
    "breed": "Beagle",
    "color": "Brown",
    "outcome_type": "Adoption",
    "sex_upon_outcome": "Neutered Male"
}
create_result = shelter.create(new_animal)
print("Create operation successful:", create_result)
```

### Running the Dashboard
1. Open `ProjectTwoDashboard.ipynb` in Jupyter Notebook.
2. Ensure MongoDB is running and dependencies are installed.
3. Run the cell with the code to launch the Dash app within the notebook.

### Functionality
The CRUD operations are implemented in the `AnimalShelter` class, and the dashboard provides functionalities including:
- Login authentication.
- Filtering animal records by type, breed, outcome type, and rescue type.
- Viewing an interactive data table with search filters, sorting, and pagination.
- An interactive map showing animal locations based on selected records.
- A pie chart displaying breed distributions.
- Export functionality for filtered data as CSV.

### Tests
CRUD module testing was done by verifying create, read, update, and delete operations in Jupyter Notebook. The environment allows interactive testing, confirming the success of each CRUD function.

### Why MongoDB Was Used
MongoDB was chosen for its flexibility in handling unstructured data. Its schema-less structure fits well with varied animal records, and its integration with PyMongo allows for efficient, real-time data handling within the dashboard.

### Dash Framework and Application Structure
Dash integrates the backend CRUD functionality with an intuitive interface, using components like input fields, data tables, charts, and maps for a seamless user experience.

### Links to Resources
- [MongoDB](https://www.mongodb.com/): NoSQL database for animal shelter records.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/): MongoDB driver for Python.
- [Dash](https://dash.plotly.com/): Framework for the dashboard.
- [Dash Leaflet](https://dash-leaflet.herokuapp.com/): Map extension for Dash.
- [Plotly](https://plotly.com/python/): Graphing library.
- [Pandas](https://pandas.pydata.org/): Data manipulation library.
- [Jupyter Notebook](https://jupyter.org/): For testing and developing the code interactively.


### Contact
For questions or feedback, please contact:  
**Alexander Wagner**  
Email: alexander.wagner@snhu.edu  
GitHub: [github.com/AlexSWagner](https://github.com/AlexSWagner)
