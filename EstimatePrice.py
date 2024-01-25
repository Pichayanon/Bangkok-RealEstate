from Data import Data
"""This is a class Estimate."""
class Estimate:
    """
    This is a class for estimate price of real estate.

    Attributes:
        data (Data): Data to store information of real estate.
        dataframe (dataframe) : Dataframe of data.
    """
    def __init__(self):
        """
        The constructor for Estimate class.
        """
        self.data = Data()
        self.dataframe = self.data.get_data()

    def estimate_price(self, city, property_type):
        """ The function for estimate price of real estate """
        city_df = self.dataframe[self.dataframe["city"] == city]
        type_df = city_df[city_df["property_type"] == property_type]
        return type_df["price"].mean()
