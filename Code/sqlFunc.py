from doctest import Example
import sqlite3

# Connection to DB
conn = sqlite3.Connection('Database/documents.db')

cursor = conn.cursor()


def insert_file_Data(dName : str, storLoc : str , dateAdded : str, theme : str, dateWritten : str = 'Not Provided', authName : str = 'Not Provided') -> str:
    """ Insert the data into the sql file

    Args:
        dName (str): document name
        storLoc (str): Storage location. It needs to have a double backslash.
        dateAdded (str): D.M.T format. Stored as string. Example: 18.01.2024
        theme (str): eg: Fantiction, Non-Fiction, etc.
        dateWritten (str, optional): The data the auther wrote it Defaults to 'Not Provided'.
        authName (str, optional): The authers name. Defaults to 'Not Provided'.

    Returns:
        str: Returns a string if the data was inserted or not.
    """
    try:
        cursor.execute('INSERT INTO docData(docName, storageLoc, dateAdded, dateWritten, autherName, theme) VALUES(?,?,?,?,?,?)', (dName, fr"{storLoc}", dateAdded, dateWritten, authName, theme))
        conn.commit()
        return "Inserted"
    
    except Exception as err:
        raise Exception(str(err))

def search_for_file(dName: str = None, dateWritten: str = None, theme: str = None, dateAdded: str = None):
    """
    Search through the SQL file for the file needed. Can sort through by: Name, written, theme and date added.
    """
    
    try:
        cursor.execute('SELECT * FROM docData WHERE docName = ? OR dateWritten = ? OR theme = ? OR dateAdded = ?', (dName, dateWritten, theme, dateAdded))
        return cursor.fetchall()
    except Exception as err:
        raise Exception(str(err))



