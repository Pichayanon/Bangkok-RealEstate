import pandas as pd

"""This is a class Data."""
class Data:
    """
     This is a class to read data file.

     Attributes:
         path (str): Path of data file.
         dataframe (dataframe): Dataframe of data.
     """
    def __init__(self):
        """
        The constructor for Data class.
        """
        self.path = "complete_df.csv"
        self.dataframe = pd.read_csv(self.path)

    def get_data(self):
        """ The function for get dataframe """
        return self.dataframe
