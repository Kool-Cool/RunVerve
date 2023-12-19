DATABASE_URL = "postgres://yoeytmrg:QhvrZX5YMw2KrAxpmelba38RcY_yPmYF@rain.db.elephantsql.com/yoeytmrg"



create_users_table_query = '''
            CREATE TABLE IF NOT EXISTS Users (
                UserID          SERIAL PRIMARY KEY ,
                FirstName       VARCHAR(100) NOT NULL,
                LastName        VARCHAR(100) NOT NULL,
                Email           VARCHAR(100) UNIQUE NOT NULL,
                Password        VARCHAR(100) NOT NULL,
                Address         VARCHAR(255) NOT NULL,
                PhoneNumber     VARCHAR(15) NOT NULL,
                RegistrationDate DATE NOT NULL
);
'''
insert_users = '''
INSERT INTO Users (FirstName, LastName, Email, Password, Address, PhoneNumber, RegistrationDate)
VALUES (%s, %s, %s, %s, %s, %s, %s) 
RETURNING *
;
'''
# Using Return for API Testing





create_species_table_query = '''
            CREATE TABLE IF NOT EXISTS Species (
                SpeciesID       SERIAL PRIMARY KEY ,
                CommonName      VARCHAR(100) NOT NULL,
                ScientificName  VARCHAR(100) UNIQUE NOT NULL,
                Description     TEXT NOT NULL
            );
'''
insert_species = '''
INSERT INTO Species (CommonName, ScientificName, Description)
VALUES (%s, %s, %s)
RETURNING *
; '''





create_trees_table_query = '''
            CREATE TABLE IF NOT EXISTS Trees (
                TreeID          SERIAL PRIMARY KEY,
                SpeciesID       INT NOT NULL,
                Location        VARCHAR(100) NOT NULL,
                Latitude        NUMERIC(9,6) NOT NULL,
                Longitude       NUMERIC(9,6) NOT NULL,
                PlantedDate     DATE NOT NULL,
                Height          NUMERIC(5,2) NOT NULL,
                Diameter        NUMERIC(5,2) NOT NULL,
                HealthStatus    VARCHAR(50) NOT NULL,
                
                FOREIGN KEY (SpeciesID) REFERENCES Species(SpeciesID)
            );
'''
insert_trees = '''   
INSERT INTO Trees (SpeciesID, Location, Latitude, Longitude, PlantedDate, Height, Diameter, HealthStatus)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
RETURNING *
;
'''





create_adoptions_table_query = '''
            CREATE TABLE IF NOT EXISTS Adoption (
                UserID          INT NOT NULL,
                TreeID          INT NOT NULL,
                AdoptionDate    DATE NOT NULL,
                DonationAmount  NUMERIC(7,2) NOT NULL,
                
                FOREIGN KEY (UserID) REFERENCES Users(UserID),
                FOREIGN KEY (TreeID) REFERENCES Trees(TreeID),
                PRIMARY KEY (UserID, TreeID)
            );
'''
# No two Persons Can adopt same tree
# No person can adopt same tree twice\
    
insert_adoptions = '''  
INSERT INTO Adoption (UserID, TreeID, AdoptionDate, DonationAmount)
VALUES (%s, %s, %s, %s)
RETURNING *
;
'''

