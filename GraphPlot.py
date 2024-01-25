import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Data import Data
import seaborn as sns
"""This is a class GraphPlot."""
class GraphPlot:
    """
    This is a class to create widget of graph.

    Attributes:
        parent (str): root of graph.
        data (Data): Data to store information of real estate.
        dataframe (dataframe) : Dataframe of data.
    """
    def __init__(self, parent):
        """
        The constructor for GraphPlot class.
        """
        self.parent = parent
        self.data = Data()
        self.dataframe = self.data.get_data()

    def plot_histogram(self, selected_var):
        """The function for create histogram widget."""
        plt.close('all')
        fig_hist, ax_hist = plt.subplots()
        sns.histplot(self.dataframe[selected_var], ax=ax_hist)
        ax_hist.set_xlabel(selected_var)
        ax_hist.set_ylabel("Frequency")
        ax_hist.set_title("Histogram of " + selected_var)
        histogram_widget = FigureCanvasTkAgg(fig_hist, master=self.parent)
        return histogram_widget

    def plot_compare_all(self):
        """The function for create compare all city widget."""
        plt.close('all')
        fig_compare, ax_compare = plt.subplots()
        data_city = self.dataframe.sort_values(['city', 'price'],
                                               ascending=[True, False])
        data_pivot = data_city.pivot_table(index='city',
                                           columns='property_type',
                                           values='price')
        sns.barplot(data=data_pivot, ax=ax_compare)
        ax_compare.set_title('Comparison of Prices between Cities')
        ax_compare.set_xlabel('City')
        ax_compare.set_ylabel('Price')
        compare_widget = FigureCanvasTkAgg(fig_compare, master=self.parent)
        return compare_widget

    def plot_compare_city(self, city1, city2):
        """The function for create compare 2 city widget."""
        plt.close('all')
        fig_compare2, ax_compare2 = plt.subplots(figsize=(4, 4))
        data_city = self.dataframe[(self.dataframe['city'] == city1)
                                   | (self.dataframe['city'] == city2)]
        sns.barplot(x='property_type', y='price', hue='city', data=data_city,
                    ax=ax_compare2)
        compare_widget2 = FigureCanvasTkAgg(fig_compare2, master=self.parent)
        return compare_widget2
