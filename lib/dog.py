from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_table(base, engine):
    base.metadata.create_all(engine)

'''
In summary, this function create_table is used to create database tables in the 
connected database using the provided SQLAlchemy Base object and Engine. This is
useful when you have defined your database schema using SQLAlchemy models and want
to create the corresponding tables in the actual database before starting to work 
with the database.

'''

# This function is used to save a Dog object to the database using the provided session.
def save(session, dog):
    session.add(dog)  # Adds the dog object to the session, preparing it to be saved in the database.

# This function is used to retrieve all the Dog objects from the database using the provided session.
def get_all(session):
    return session.query(Dog).all()  # Queries the Dog table and returns a list of all Dog objects.

# This function is used to find a Dog by its name in the database using the provided session.
def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    # Queries the Dog table with a filter condition for the 'name' attribute, 
    # and returns the first Dog object that matches the condition.

# This function is used to find a Dog by its ID in the database using the provided session.
def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).one()
    # Queries the Dog table with a filter condition for the 'id' attribute, 
    # and returns the Dog object that matches the condition. 
    # Raises an exception if more than one or no Dog objects are found.

# This function is used to find a Dog by its name and breed in the database using the provided session.
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
    # Queries the Dog table with filter conditions for both 'name' and 'breed' attributes, 
    # and returns the first Dog object that matches both conditions.

# This function is used to update the breed of a Dog in the database using the provided session.
def update_breed(session, dog, breed):
    dog.breed = breed  # Updates the 'breed' attribute of the Dog object with the new value.
    session.add(dog)  # Adds the updated Dog object to the session.
    session.commit()  # Commits the changes, saving the updated Dog object to the database.






if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()