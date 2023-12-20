DATABASE_URL = "postgres://yoeytmrg:QhvrZX5YMw2KrAxpmelba38RcY_yPmYF@rain.db.elephantsql.com/yoeytmrg"


create_users_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                user_id          SERIAL PRIMARY KEY,
                first_name       VARCHAR(100) NOT NULL,
                last_name        VARCHAR(100) NOT NULL,
                email            VARCHAR(100) UNIQUE NOT NULL,
                password         VARCHAR(100) NOT NULL,
                address          VARCHAR(255) NOT NULL,
                phone_number     VARCHAR(15) NOT NULL,
                registration_date DATE NOT NULL,
                is_admin         BOOLEAN DEFAULT FALSE
);
'''
insert_users = '''
INSERT INTO users (first_name, last_name, email, password, address, phone_number, registration_date, is_admin)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
RETURNING *
;
'''





create_species_table_query = '''
            CREATE TABLE IF NOT EXISTS species (
                species_id       SERIAL PRIMARY KEY,
                common_name      VARCHAR(100) NOT NULL,
                scientific_name  VARCHAR(100) UNIQUE NOT NULL,
                description      TEXT NOT NULL
            );
'''
insert_species = '''
INSERT INTO species (common_name, scientific_name, description)
VALUES (%s, %s, %s)
RETURNING *
; '''





create_trees_table_query = '''
            CREATE TABLE IF NOT EXISTS trees (
                tree_id          SERIAL PRIMARY KEY,
                species_id       INT NOT NULL,
                location         VARCHAR(100) NOT NULL,
                latitude         NUMERIC(9,6) NOT NULL,
                longitude        NUMERIC(9,6) NOT NULL,
                planted_date     DATE NOT NULL,
                height           NUMERIC(5,2) NOT NULL,
                diameter         NUMERIC(5,2) NOT NULL,
                health_status    VARCHAR(50) NOT NULL,
                
                FOREIGN KEY (species_id) REFERENCES species(species_id)
            );
'''
insert_trees = '''   
INSERT INTO trees (species_id, location, latitude, longitude, planted_date, height, diameter, health_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
RETURNING *
;
'''





create_adoptions_table_query = '''
            CREATE TABLE IF NOT EXISTS adoption (
                user_id          INT NOT NULL,
                tree_id          INT NOT NULL,
                adoption_date    DATE NOT NULL,
                donation_amount  NUMERIC(7,2) NOT NULL,
                
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (tree_id) REFERENCES trees(tree_id),
                PRIMARY KEY (user_id, tree_id)
            );
'''
insert_adoptions = '''  
INSERT INTO adoption (user_id, tree_id, adoption_date, donation_amount)
VALUES (%s, %s, %s, %s)
RETURNING *
;
'''


# Can two Persons Can adopt same tree ??
# No person can adopt same tree twice\
