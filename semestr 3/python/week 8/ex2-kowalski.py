'''
COMMANDS CHEATSHEET

Arguments need to be provided in the given format: <Table> <operation> <optional_data>
Available tables: Movies, Directors, Producers
Available operations: --add, --show, --simple_show (Only --add takes additional data)
Required arguments for adding to Directors / Producers: name, surname
Required arguments for adding to Movies: title, year, directors_id, producers_id

Example: ex2-kowalski.py Movies --add "Cool Movie" 2021 1 1
More examples provided in the test script (It's written for Windows, I hope it's not a problem)
'''



import sqlalchemy as db
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
import sys



#Declarative_base() constructs a base class for classes representing database entries and tables
Base = declarative_base()


class Movie(Base):
    #The table name isn't used/shown anywhere in this program, but it would be visible if one opened the database in an external program
    __tablename__ = 'Movies'

    #Turns out that sqlalchemy sets autoincrement=True automatically for the an Integer primary_key column 
    #https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column.params.autoincrement
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    year = db.Column('year', db.Integer)
    #There's a ne to many relationship between Movies table and Directors/Producers table
    #It's a bidirectional relatiomship, so the other tables have a many to one relationship with Movies
    #https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many
    director_id = db.Column('director_id', db.ForeignKey('Directors.id'))
    producer_id = db.Column('producer_id', db.ForeignKey('Producers.id'))
    director = relationship('Director', back_populates = 'movies')
    producer = relationship('Producer', back_populates = 'movies')

    def __init__(self, title, year, director_id, producer_id):
        self.title = title
        self.year = year
        #get returns an instance based on the given primary key identifier, or None if not found.
        self.director = session.query(Director).get(director_id)
        self.producer = session.query(Producer).get(producer_id)

    #(self.director != None) and self.director.simple_str() makes sure that we don't call a simple_str() method on a nonexistent object
    #'False' will be printed out in such a case
    def __str__(self): return f'Movie(id = {self.id}; title = {self.title}; year = {self.year}; director = {(self.director != None) and self.director.simple_str()}; producer = {(self.producer != None) and self.producer.simple_str()})'
    #simple_str prints out an element without printing out the related elements
    def simple_str(self): return f'Movie(id = {self.id}; title = {self.title}; year = {self.year})'


class Director(Base):
    __tablename__ = 'Directors'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    movies = relationship('Movie', back_populates = 'director')

    def __init__(self, name, surname): 
        self.name = name
        self.surname = surname
        self.movies = []

    def __str__(self): return f'Director(id = {self.id}; name = {self.name}; surname = {self.surname}; movies = {(self.movies != []) and list(map(lambda x: x.simple_str(), self.movies))})'
    def simple_str(self): return f'Director(id = {self.id}; name = {self.name}; surname = {self.surname})'


class Producer(Base):
    __tablename__ = 'Producers'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    movies = relationship('Movie', back_populates = 'producer')

    def __init__(self, name, surname): 
        self.name = name
        self.surname = surname
        self.movies = []

    def __str__(self): return f'Producer(id = {self.id}; name = {self.name}; surname = {self.surname}; movies = {(self.movies != []) and list(map(lambda x: x.simple_str(), self.movies))})'
    def simple_str(self): return f'Producer(id = {self.id}; name = {self.name}; surname = {self.surname})'



if len(sys.argv) < 2: exit()

Engine = db.create_engine('sqlite:///bootleg_imdb.db')
#This line creates all tables stored in this declarative base (if they don't exist in the target database)
#https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.MetaData.create_all
Base.metadata.create_all(Engine)

with Session(Engine) as session:
    new_thing = None

    if sys.argv[1] == 'Movies':
        if sys.argv[2] == '--add': new_thing = Movie(*sys.argv[3:])
        elif sys.argv[2] == '--show':
            movies = session.query(Movie).all()
            for m in movies: print(m)
        elif sys.argv[2] == '--simple_show':
            movies = session.query(Movie).all()
            for m in movies: print(m.simple_str())

    elif sys.argv[1] == 'Directors':
        if sys.argv[2] == '--add': new_thing = Director(*sys.argv[3:])
        elif sys.argv[2] == '--show':
            directors = session.query(Director).all()
            for d in directors: print(d)
        elif sys.argv[2] == '--simple_show':
            directors = session.query(Director).all()
            for d in directors: print(d.simple_str())

    elif sys.argv[1] == 'Producers':
        if sys.argv[2] == '--add': new_thing = Producer(*sys.argv[3:])
        elif sys.argv[2] == '--show':
            producers = session.query(Producer).all()
            for p in producers: print(p)
        elif sys.argv[2] == '--simple_show':
            producers = session.query(Producer).all()
            for p in producers: print(p.simple_str())

    if new_thing is not None:
        session.add(new_thing)
        session.commit()