from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        # Initialize the MongoDB client with credentials
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create(self, data):
        """Insert a new document into the animals collection."""
        if data:
            try:
                self.collection.insert_one(data)
                return True  # Success
            except Exception as e:
                print(f"An error occurred: {e}")
                return False  # Failure
        else:
            raise ValueError("Data parameter is empty.")

    def read(self, search_criteria):
        """Retrieve documents from the animals collection matching the search criteria."""
        try:
            results = list(self.collection.find(search_criteria))
            return results  # Return matching documents as a list
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list on failure

    def update(self, search_criteria, new_data):
        """Update documents in the animals collection."""
        if search_criteria and new_data:
            try:
                result = self.collection.update_many(search_criteria, {"$set": new_data})
                return result.modified_count  # Return the number of modified documents
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0  # Return 0 if no documents were modified
        else:
            raise ValueError("Search criteria or new data missing.")

    def delete(self, search_criteria):
        """Delete documents from the animals collection matching the search criteria."""
        if search_criteria:
            try:
                result = self.collection.delete_many(search_criteria)
                return result.deleted_count  # Return the number of deleted documents
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0  # Return 0 if no documents were deleted
        else:
            raise ValueError("Search criteria missing.")
