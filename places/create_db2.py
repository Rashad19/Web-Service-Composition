# Script to create and build database
# It allows for easy changes by deleting db file,
# changing data here and then creating an updated db by running webSer2.py
def create2():
    import sqlite3
    
    # Catch exception if db connection fails
    try:
        # Connect to database and insert data into table using cursor execute
        # Commit changes to database and then closing cursor
        sqlconn = sqlite3.connect('db2.db')
        my_cursor = sqlconn.cursor()
        print("conn success")
        my_cursor.execute("""INSERT INTO places
                            (id, name, city, country)
                            VALUES 
                            (0, 'Tower of London', 'London', 'UK'),
                            (1, 'Buckingham Palace', 'London', 'UK'),
                            (2, 'British Museum', 'London', 'UK'),
                            (3, 'Eiffel Tower', 'Paris', 'France'),
                            (4, 'Louvre', 'Paris', 'France'),
                            (5, 'Sainte-Chapelle', 'Paris', 'France'),
                            (6, 'Colosseum', 'Rome', 'Italy'),
                            (7, 'Grand Canal', 'Venice', 'Italy'),
                            (8, 'Leaning Tower of Pisa', 'Pisa', 'Italy'),
                            (9, 'Acropolis Museum', 'Athens', 'Greece'),
                            (10, 'Erechtheion', 'Athens', 'Greece'),
                            (11, 'Acropolis of Athens', 'Athens', 'Greece'),
                            (12, 'Alhambra', 'Granada', 'Spain'),
                            (14, 'Park Güell', 'Barcelona', 'Spain'),
                            (15, 'Sagrada Família', 'Barcelona', 'Spain'),
                            (16, 'Brandenburg Gate', 'Berlin', 'Germany'),
                            (17, 'Reichstag building', 'Berlin', 'Germany'),
                            (18, 'Neuschwanstein Castle', 'Schwangau', 'Germany'),
                            (19, 'Rijksmuseum', 'Amsterdam', 'Netherlands'),
                            (20, 'Van Gogh Museum', 'Amsterdam', 'Netherlands'),
                            (21, 'Anne Frank House', 'Amsterdam', 'Netherlands'),
                            (22, 'Hagia Sophia', 'Istanbul', 'Turkey'),
                            (23, 'Sultan Ahmed Mosque', 'Istanbul', 'Turkey'),
                            (24, 'Topkapı Palace', 'Istanbul', 'Turkey'),
                            (25, 'Kapellbrücke', 'Luzern', 'Switzerland'),
                            (26, 'Olympic Museum', 'Lausanne', 'Switzerland'),
                            (27, 'Kunsthaus Zürich', 'Zurich', 'Switzerland'),
                            (28, 'Lofoten', 'Nordland', 'Norway'),
                            (29, 'Trolltunga', 'Vestland', 'Norway'),
                            (30, 'Preikestolen', 'Rogaland', 'Norway')
                            """)
        sqlconn.commit()
        print("All good")
        my_cursor.close()
    except:                                                            
        print("Error database") 
    finally:
        if sqlconn:
            sqlconn.close()       
    
# Function to be passed to webSer2.py
if __name__ == '__main__':
    create2()
