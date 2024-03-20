import sqlite3

# Connection to DB
conn = sqlite3.Connection('Database/documents.db')

cursor = conn.cursor()


class SQLFunc:
    def __init__(self):
        # Connection to DB
        self.conn = sqlite3.Connection('Database/documents.db')
        self.cursor = self.conn.cursor()

    def insert_File_Data(self, dName: str, storLoc: str, dateAdded: str, theme: str, dateWritten: str = 'Not Provided', authName: str = 'Not Provided') -> str:
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
            self.cursor.execute('INSERT INTO docData(docName, storageLoc, dateAdded, dateWritten, autherName, theme) VALUES(?,?,?,?,?,?)', (dName, fr"{storLoc}", dateAdded, dateWritten, authName, theme))
            self.conn.commit()
            return "Inserted"
        
        except Exception as err:
            raise Exception(str(err))

    def search_For_File(self, dName: str = None, dateWritten: str = None, theme: str = None, dateAdded: str = None):
        """
        Search through the SQL file for the file needed. Can sort through by: Name, written, theme and date added.
        """
        self.cursor.execute('SELECT storageLoc FROM docData WHERE docName = ? OR dateWritten = ? OR theme = ? OR dateAdded = ?', (dName, dateWritten, theme, dateAdded))
        return self.cursor.fetchall()

    def return_All_Doc(self,):
        """
        Returns all the documents in the database.
        """
        try:
            self.cursor.execute('SELECT * FROM docData')
            return self.cursor.fetchall()
        except Exception as err:
            raise Exception(str(err))
        
    def docNames(self):
        """
        Returns all the document names in the database.
        """
        self.cursor.execute('SELECT docName FROM docData')
        return self.cursor.fetchall()