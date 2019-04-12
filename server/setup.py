import mysql.connector
from sqlalchemy import *

DB_INFO = "DBInfo"      #name of the file that stores db credentials

def connectToDatabase(file_name):
    '''
    Connects to a database given the file with the credentials for the server
    and returns the connection to the server
    '''

    DBinfo = []
    file = open(file_name, 'r')

    for line in file:
        DBinfo.append(line.rstrip("\n"))

    file.close()

    #made to query list of databases
    mysql_engine = create_engine("mysql+mysqlconnector://{0}:{1}@{2}".format(
        DBinfo[0], DBinfo[1], DBinfo[2]))

    #If database does not exist create it
    mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format(DBinfo[3]))

    db_url = "mysql+mysqlconnector://%s:%s@%s/%s?charset=utf8mb4" \
            % (DBinfo[0], DBinfo[1], DBinfo[2], DBinfo[3])

    mydb = create_engine(db_url)    #, echo=true) #include for debugging
    return mydb

def initializeDatabase(db_connection):
    metadata = MetaData(db_connection)
    courses = Table("CS_courses_fall19", metadata,
            Column("course_number", String(20)),
            Column("alt_course_number", String(20)),
            Column("course_section", Integer),
            Column("course_id", Integer),
            Column("course_name", String(20)),
            Column("professor", String(20)),
            Column("location", String(20)),
            Column("room_number", String(20)),
            Column("days", String(20)),
            Column("start_time", String(20)),
            Column("end_time", String(20)),
            Column("node_id", Integer))

    edges = Table("CS_courses_fall19_edges", metadata,
            Column("from_node", Integer),
            Column("to_node", Integer))

    metadata.create_all()

def main():
    db = connectToDatabase(DB_INFO)
    
    if not db.has_table("CS_courses_fall19") and not db.has_table("CS_courses_fall19_edges"):
        initializeDatabase(db)
        print("Initialized database")

    else:
        print("Database already exists")

if __name__ == '__main__':
    main()
