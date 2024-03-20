import os


class FileFunc:
    def __init__(self):
        pass

    # Display files
    def display_File(self, location : str):
        """display File

        Args:
            location (str): the location of the file to be displayed

        Opens the file in the default program for the file type
        """
        os.startfile(location)