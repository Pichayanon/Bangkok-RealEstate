import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt
from EstimatePrice import Estimate
from GraphPlot import GraphPlot

"""This is a class App."""
class App(tk.Tk):
    def __init__(self):
        """
        This is a class to create main window.

        Attributes:
            estimate (Estimate): Estimate Class.
            graph_plot (GraphPlot): GraphPlot Class.
        """
        super().__init__()
        self.title('Bangkok Real-Estate')
        self.geometry('1000x700')
        self.configure(bg="#2c698d")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.estimate = Estimate()
        self.graph_plot = GraphPlot(self)
        self.main_menu()

    def main_menu(self):
        """ The function for display main menu """

        # Create Label Select Menu
        tk.Label(self, text="Select Menu", font=("Helvetica", 48),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2).\
            grid(row=0, column=0, padx=10, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to function Estimate price
        tk.Button(self, text="Estimate price of Real Estate",
                  relief="flat", width=20, height=2,
                  command=self.swift_estimate_menu).\
            grid(row=1, column=0, padx=10, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to function Compare price
        tk.Button(self, text="Compare price between 2 district",
                  relief="flat", width=20, height=2,
                  command=self.swift_compare_menu). \
            grid(row=2, column=0, padx=10, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to function Show statistic
        tk.Button(self, text="Show Statistic of data",
                  relief="flat", width=20, height=2,
                  command=self.swift_statistic_menu). \
            grid(row=3, column=0, padx=10, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to quit App
        tk.Button(self, text="Quit Application",
                  relief="flat", width=20, height=2,
                  command=self.destroy). \
            grid(row=4, column=0, padx=10, columnspan=4, pady=10, sticky="SEW")

    def estimate_menu(self):
        """ The function for estimate main menu """

        # Create property_type
        property_type = tk.StringVar(value="")

        # Create city
        city = tk.StringVar()

        # Create price
        price = tk.StringVar(value="0 Baht")

        # Create list of all city
        list_city = list(np.unique(self.estimate.dataframe['city']))

        # Create Label to let user select type of real estate
        tk.Label(self, text="Select Type",
                 font=("Helvetica", 20),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create land type button
        tk.Button(self, text='Land', width=20, height=2,
                  command=lambda: property_type.set("Land")).\
            grid(row=1, column=0, padx=10, pady=10)

        # Create condo type button
        tk.Button(self, text='Condo', width=20, height=2,
                  command=lambda: property_type.set("Condo"))\
            .grid(row=1, column=1, padx=10, pady=10)

        # Create house type button
        tk.Button(self, text='House', width=20, height=2,
                  command=lambda: property_type.set("Detached House"))\
            .grid(row=1, column=2, padx=10, pady=10)

        # Create townhouse type button
        tk.Button(self, text='Townhouse', width=20, height=2,
                  command=lambda: property_type.set("Townhouse"))\
            .grid(row=1, column=3, padx=10, pady=10)

        # Create Label to let user city
        tk.Label(self, text="Select District",
                 font=("Helvetica", 20),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Combobox to select city
        ttk.Combobox(self, textvariable=city, values=list_city).\
            grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Label to show what type and city be selected
        tk.Label(self, text="Estimate Price of", font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")
        tk.Label(self, textvariable=property_type, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2).\
            grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="EW")
        tk.Label(self, textvariable=city, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2).\
            grid(row=5, column=2, columnspan=2, padx=10, pady=10, sticky="EW")

        # Create button to show Estimate Price
        tk.Label(self, textvariable=price, font=("Helvetica", 48),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # Create button to compute Estimate Price
        tk.Button(self, text="Compute Estimate Price",
                  relief="flat", width=20, height=2,
                  command=
                  lambda: price.set(f"{(self.estimate.estimate_price(city.get(), property_type.get()) if self.estimate.estimate_price(city.get(), property_type.get()) >= 0 else 0):,.0f} Baht")).\
            grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.swift_main_menu)\
            .grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

    def statistic_menu(self):
        """ The function for create statistic menu """
        # Create button to show Statistic
        tk.Label(self, text="Statistic of Data", font=("Helvetica", 20),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Plot graph
        self.graph_plot.plot_histogram("price").get_tk_widget().\
            grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="EW")

        self.graph_plot.plot_compare_all().get_tk_widget().\
            grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="EW")

        # Describe Histogram
        tk.Label(self, text="Mean : 6412613.17 | Std : 5027061.92 |"
                            " Min : 110000.00 | Max : 28907325.00",
                 font=("Helvetica", 9),
                 background="#bae8e8", foreground="black",
                 borderwidth=5, highlightthickness=2). \
            grid(row=2, column=0, columnspan=2, padx=10, sticky="EW")

        # Describe Bar graph
        tk.Label(self, text="The most expensive type of is "
                            "Detected House, followed by Townhouse, Land, "
                            "and Condo respectively.",
                 font=("Helvetica", 9),
                 background="#bae8e8", foreground="black",
                 borderwidth=5, highlightthickness=2). \
            grid(row=2, column=2, columnspan=2, padx=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.swift_main_menu) \
            .grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

    def compare_menu(self):
        """ The function for display compare menu """
        # Create city1 and city2
        city1 = tk.StringVar(value="Bang Bon")
        city2 = tk.StringVar(value="Bang Bon")

        # Create list of city
        list_city = list(np.unique(self.estimate.dataframe['city']))

        # Create Combobox to select city
        ttk.Combobox(self, textvariable=city1, values=list_city).\
            grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="EW")
        ttk.Combobox(self, textvariable=city2, values=list_city). \
            grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="EW")

        # Create Label to show what city be selected
        tk.Label(self, textvariable=city1, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2).\
            grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="EW")
        tk.Label(self, textvariable=city2, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="EW")

        # Plot graph
        self.graph_plot.plot_compare_city(city1.get(), city2.get()).\
            get_tk_widget(). \
            grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="EW")

        # Create Button to Compare Graph
        tk.Button(self, text="Compare Graph",
                  relief="flat", width=20, height=2,
                  command=
                  lambda: self.graph_plot.plot_compare_city(city1.get(),
                                                            city2.get())
                  .get_tk_widget()
                  .grid(row=2, column=1, columnspan=2, padx=10, pady=10,
                        sticky="EW")) \
            .grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.swift_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

    def swift_main_menu(self):
        """ The function for swift to main menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.main_menu()

    def swift_estimate_menu(self):
        """ The function for swift to estimate menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.estimate_menu()

    def swift_statistic_menu(self):
        """ The function for swift to statistic menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.statistic_menu()

    def swift_compare_menu(self):
        """ The function for swift to compare menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.compare_menu()


if __name__ == "__main__":
    app = App()
    app.mainloop()
