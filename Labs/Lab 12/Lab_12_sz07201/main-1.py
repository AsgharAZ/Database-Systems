# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = 'Northwind'
database = 'DESKTOP-JBCSQ90\\MYSQLSERVER'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication


# connection = pyodbc.connect(
#         "Driver={SQL Server};"
#         "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
#         "Database=Northwind;"
#         "Trusted_Connection=yes;"
#     )
        
# Create the connection string based on the authentication method chosen
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Main Window Class
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the main UI window.

        This constructor is called when an instance of the UI class is created.
        It performs the following tasks:
        1. Calls the constructor of the inherited class.
        2. Loads the user interface (UI) from the 'MainWindow.ui' file.
        3. Populates the 'orderTable' with data.
        4. Connects the "Insert Order" button to the event handler for opening the
        master transaction form.

        Note:
        - The 'MainWindow.ui' file should exist and contain the required UI elements.

        Returns:
        None
        """
        # Call the inherited classes __init__ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('MainWindow-1.ui', self)

        # Load Orders data
        self.populate_table()

        # Connect Submit Button to Event Handling Code
        self.InsertOrder.clicked.connect(self.open_master_form)

    def populate_table(self):
        """
        Populates the 'orderTable' with data from the Northwind database.

        This function connects to the Northwind database, retrieves orders data,
        and populates the 'orderTable' widget with the fetched data. It also adjusts
        the column widths for better content display.

        Note:
        - Ensure that the 'orderTable' widget is set up and available in the UI.
        - The database connection parameters (server, database, authentication) should
        be correctly configured.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database


    # try:
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )
    #     print("Connection successful!")
    # except pyodbc.Error as ex:
    #     sqlstate = ex.args[1]
    #     print("Connection failed. Error:", sqlstate)



        cursor = connection.cursor()

        # TODO: Write SQL query to fetch orders data
        cursor.execute("Select * from Orders")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.orderTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.orderTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.orderTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def open_master_form(self):
        """
        Opens the master transaction form.

        This function is called when the "Insert Order" button is clicked in the main
        UI. It creates and displays the master transaction form (Master class).

        Note:
        - Ensure that the Master class (master_form) is defined and available in the script.

        Returns:
        None
        """
        self.master_form = Master()
        self.master_form.show()


class Master(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the master transaction form.

        This constructor is called when an instance of the Master class is created.
        It performs the following tasks:
        1. Calls the constructor of the inherited class.
        2. Loads the user interface (UI) from the 'MasterTransactionForm.ui' file.
        3. Populates employee, customer, shipper, and product tables with data.
        4. Sets up event handlers for table selection.
        5. Makes certain input fields read-only or disabled.
        6. Connects buttons like "Add," "Insert," and "Clear" to their respective
        event handling functions.

        Note:
        - The 'MasterTransactionForm.ui' file should exist and contain the required UI elements.

        Returns:
        None
        """
        # Call the inherited classes __init__ method
        super(Master, self).__init__()

        # Load the .ui file
        uic.loadUi('MasterTransactionForm-1.ui', self)

        # Load employee table
        self.populate_employee_table()

        # Load customer table
        self.populate_customer_table()

        # Load shippers table
        self.populate_ship_table()

        # Load products table
        self.populate_product_table()

        # Employee Table Row selected
        self.employeesTable.itemSelectionChanged.connect(
            self.get_selected_employee_data)

        # Customer Table Selected
        self.customersTable.itemSelectionChanged.connect(
            self.get_selected_customer_data)

        # Product Table Selected
        self.productsTable.itemSelectionChanged.connect(
            self.get_selected_product_data)

        # Shipper Table Selected
        self.shippersTable.itemSelectionChanged.connect(
            self.get_selected_shipper_data)

        # Make EmployeeID and EmployeeName readonly
        self.EmployeeID.setDisabled(True)
        self.EmployeeName.setDisabled(True)

        # Make CustomerID and CustomerName readonly
        self.CustomerID.setDisabled(True)
        self.CustomerName.setDisabled(True)

        # Make ProductID and ProductName readonly
        self.ProductID.setDisabled(True)
        self.ProductName.setDisabled(True)

        # Make ShipCompanyID and ShipCompany readonly
        self.ShipCompanyID.setDisabled(True)
        self.ShipCompany.setDisabled(True)

        # Add Row to Product Table
        self.Add.clicked.connect(self.add_product)

        # Insert Product
        self.Insert.clicked.connect(self.insert_order)

        # Clear
        self.Clear.clicked.connect(self.clear)

    def populate_employee_table(self):
        """
        Populates the 'employeesTable' with employee data from the Northwind database.

        This function connects to the Northwind database, retrieves employee data,
        and populates the 'employeesTable' widget with the fetched data. It also adjusts
        the column widths for better content display.

        Note:
        - Ensure that the 'employeesTable' widget is set up and available in the UI.
        - The database connection parameters (server, database, authentication) should
        be correctly configured.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )

        cursor = connection.cursor()

        # TODO: Write SQL query to fetch employee data
        cursor.execute("select * from Employees")


        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.employeesTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.employeesTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.employeesTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def populate_customer_table(self):
        """
        Populates the 'customersTable' with customer data from the Northwind database.

        This function connects to the Northwind database, retrieves customer data,
        and populates the 'customersTable' widget with the fetched data. It also adjusts
        the column widths for better content display.

        Note:
        - Ensure that the 'customersTable' widget is set up and available in the UI.
        - The database connection parameters (server, database, authentication) should
        be correctly configured.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )

        cursor = connection.cursor()

        # TODO: Write SQL query to fetch customers data
        cursor.execute("select * from Customers")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.customersTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.customersTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust content display
        header = self.customersTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def populate_ship_table(self):
        """
        Populate the shippers table with data from the Northwind database.

        This function connects to the Northwind database, executes an SQL query to fetch
        data from the Shippers table, and populates the shippersTable widget with the
        retrieved data. It also adjusts the column widths for better display.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )

        cursor = connection.cursor()

        # TODO: Write SQL query to fetch shippers data
        cursor.execute("select * from Shippers")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.shippersTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.shippersTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.shippersTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def populate_product_table(self):
        """
        Populate the products table with data from the Northwind database.

        This function connects to the Northwind database, executes an SQL query to fetch
        specific data (ProductID, ProductName, UnitPrice) from the Products table, and
        populates the productsTable widget with the retrieved data. It also adjusts
        the column widths for better display.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )

        cursor = connection.cursor()

        # TODO: Write SQL query to fetch products data
        cursor.execute("select * from Products")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.productsTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.productsTable.setItem(row_index, col_index, item)

        # Close the database connection
        connection.close()

        # Adjust the column widths for better display
        header = self.productsTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    def get_selected_employee_data(self):
        """
        Retrieve and display information of the selected employee.

        This function gets the index of the selected row in the employees table,
        retrieves the Employee ID, First Name, and Last Name of the selected employee,
        and displays this information in the corresponding input fields.

        Returns:
        None
        """
        # Get the index of the selected row
        selected_row = self.employeesTable.currentRow()
        # Employee ID
        EmployeeID = self.employeesTable.item(selected_row, 0).text()
        # First Name
        FirstName = self.employeesTable.item(selected_row, 1).text()
        # Last Name
        LastName = self.employeesTable.item(selected_row, 2).text()
        # Set Employee ID
        self.EmployeeID.setText(EmployeeID)
        # Set Employee Name
        self.EmployeeName.setText(FirstName + " " + LastName)

    def get_selected_customer_data(self):
        """
        Retrieve and display information of the selected customer.

        This function gets the index of the selected row in the customers table,
        retrieves the Customer ID and Company Name of the selected customer, and
        displays this information in the corresponding input fields.

        Returns:
        None
        """
        # Get the index of the selected row
        selected_row = self.customersTable.currentRow()
        # Customer ID
        customersID = self.customersTable.item(selected_row, 0).text()
        # Company Name
        customersName = self.customersTable.item(selected_row, 1).text()
        # Set Customer ID
        self.CustomerID.setText(customersID)
        # Set Customer Name
        self.CustomerName.setText(customersName)

    def get_selected_product_data(self):
        """
        Retrieve and display information of the selected product.

        This function gets the index of the selected row in the products table,
        retrieves the Product ID and Product Name of the selected product, and
        displays this information in the corresponding input fields.

        Returns:
        None
        """
        # Get the index of the selected row
        selected_row = self.productsTable.currentRow()
        # Product ID
        ProductID = self.productsTable.item(selected_row, 0).text()
        # Product Name
        ProductName = self.productsTable.item(selected_row, 1).text()
        # Set Product ID
        self.ProductID.setText(ProductID)
        # Set Product Name
        self.ProductName.setText(ProductName)

    def get_selected_shipper_data(self):
        """
        Retrieve and display information of the selected shipper.

        This function gets the index of the selected row in the shippers table,
        retrieves the Ship Company ID and Ship Company Name of the selected shipper,
        and displays this information in the corresponding input fields.

        Returns:
        None
        """
        # Get the index of the selected row
        selected_row = self.shippersTable.currentRow()
        # Ship Company ID
        ShipCompanyID = self.shippersTable.item(selected_row, 0).text()
        # Ship Company Name
        ShipCompanyName = self.shippersTable.item(selected_row, 1).text()
        # Set ShipCompany ID
        self.ShipCompanyID.setText(ShipCompanyID)
        # Set ShipCompany Name
        self.ShipCompany.setText(ShipCompanyName)

    def add_product(self):
        """
        Add a product to the order details table.

        This function adds a new row to the order details table in the user interface
        and populates it with product information entered by the user, such as
        Product ID, Unit Price, Quantity, and Discount. It also adjusts the column
        widths for proper display and clears the input fields for the next entry.

        Note:
        - Ensure that the relevant input fields are correctly configured in the UI.

        Returns:
        None
        """
        row_position = self.orderDetailsTable.rowCount()
        self.orderDetailsTable.insertRow(row_position)

        self.orderDetailsTable.setItem(
            row_position, 0, QTableWidgetItem(self.ProductID.text()))
        self.orderDetailsTable.setItem(
            row_position, 1, QTableWidgetItem(self.UnitPrice.text()))
        self.orderDetailsTable.setItem(
            row_position, 2, QTableWidgetItem(self.Quantity.text()))
        self.orderDetailsTable.setItem(
            row_position, 3, QTableWidgetItem(self.Discount.text()))

        header = self.orderDetailsTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        self.ProductID.setText("")
        self.ProductName.setText("")
        self.UnitPrice.setText("")
        self.Quantity.setText("")
        self.Discount.setText("")

    def insert_order(self):
        """
        Insert a new order into the Northwind database based on user input.

        This function retrieves order information from various input fields, such as
        Customer ID, Employee ID, shipping details, and others. It constructs an SQL
        query with parameters to insert a new order into the 'Orders' table of the
        Northwind database. After successfully inserting the order, it retrieves the
        newly assigned Order ID and displays it in a message box.

        Note:
        - Ensure that the relevant input fields are correctly configured in the UI.
        - The function assumes that the database connection is already established.

        Returns:
        None
        """
        # Get order information from input fields
        CustomerID = self.CustomerID.text()
        EmployeeID = self.EmployeeID.text()
        OrderDate = self.OrderDate.date().toString("yyyy-MM-dd")
        RequiredDate = self.RequiredDate.date().toString("yyyy-MM-dd")
        ShippedDate = self.ShippedDate.date().toString("yyyy-MM-dd")
        ShipVia = self.ShipCompanyID.text()
        Freight = self.Freight.text()
        ShipName = self.ShipName.text()
        ShipAddress = self.ShipAddress.text()
        ShipCity = self.ShipCity.text()
        ShipRegion = self.ShipRegion.text()  # Corrected from ShipName.text()
        ShipPostalCode = self.ShipPostalCode.text()
        ShipCountry = self.ShipCountry.text()

        if not Freight:
            Freight = 0.0
        else:
            Freight = float(Freight)
            
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
        )

        cursor = connection.cursor()

        # TODO: Write SQL query with parameters to insert order
        sql_query = """
       
        INSERT INTO Orders (
                CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate,
                ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion,
                ShipPostalCode, ShipCountry
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
       
        """

        # Execute the SQL query with parameter values
        cursor.execute(sql_query, (CustomerID, int(EmployeeID), OrderDate, RequiredDate, ShippedDate, int(
            ShipVia), float(Freight), ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry))
        connection.commit()

        # Retrieve the newly inserted order ID
        cursor.execute("SELECT max(orderid) AS OrderID from orders")
        result = cursor.fetchone()
        order_id = result[0]

        # Show a message box with the order ID
        QtWidgets.QMessageBox.information(
            self, "Order Inserted", f"Order ID: {order_id} has been inserted successfully.")

        # Close the database connection
        connection.close()
        self.insert_order_details(order_id)

    def insert_order_details(self, order_id):
        """
        Inserts order details into the 'Order Details' table for a given order ID.

        This function is responsible for inserting the order details, including Product ID,
        Unit Price, Quantity, and Discount, into the 'Order Details' table in the Northwind
        database. The order details are associated with the specified order ID.

        Parameters:
        - order_id (int): The unique identifier of the order for which details are being inserted.

        Note:
        - Ensure that the 'orderDetailsTable' is correctly populated with the order details.
        - The database connection parameters (server, database, authentication) should be
        correctly configured.

        Returns:
        None
        """
        # TODO: Provide the  connection string to connect to the Northwind database
        connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )

        cursor = connection.cursor()
        num_rows = self.orderDetailsTable.rowCount()

        # Iterate through the rows of 'orderDetailsTable' and insert order details
        for row in range(num_rows):
            ProductID = int(self.orderDetailsTable.item(row, 0).text())
            UnitPrice = float(self.orderDetailsTable.item(row, 1).text())
            Quantity = int(self.orderDetailsTable.item(row, 2).text())
            Discount = float(self.orderDetailsTable.item(row, 3).text())

            # TODO: Write SQL query with parameters to insert orders details
            sql_query = """INSERT INTO [Order Details] (OrderID,ProductID,UnitPrice,Quantity,Discount)VALUES (?, ?, ?, ?, ?)"""
            # Execute the SQL query with parameter values
            cursor.execute(sql_query, (int(order_id), ProductID,
                           UnitPrice, Quantity, Discount))
            connection.commit()

        # Close the database connection
        connection.close()

        # Clear the form after successfully inserting order details
        self.clear()

    def clear(self):
        """
        Clears and resets all input fields and tables in the master transaction form.

        This function resets all input fields, including Employee ID, Customer ID, Product ID,
        and other related fields, to their initial state or empty values. It also clears
        the content of the 'orderDetailsTable' and resets date fields to a default date.
        This function is typically used to clear the form after an order has been submitted
        or when the user wants to start with a fresh order entry.

        Note:
        - Ensure that the relevant input fields and tables are available in the UI.

        Returns:
        None
        """
        self.EmployeeID.setText("")
        self.EmployeeName.setText("")
        self.CustomerID.setText("")
        self.CustomerName.setText("")
        self.ProductID.setText("")
        self.ProductName.setText("")
        self.Quantity.setText("")
        self.UnitPrice.setText("")
        self.Discount.setText("")
        self.orderDetailsTable.clearContents()
        self.ShipCompanyID.setText("")
        self.ShipCompany.setText("")
        self.ShipName.setText("")
        self.Freight.setText("")
        self.ShippedDate.setDate(QDate(2000, 1, 1))
        self.OrderDate.setDate(QDate(2000, 1, 1))
        self.RequiredDate.setDate(QDate(2000, 1, 1))
        self.ShipAddress.setText("")
        self.ShipCity.setText("")
        self.ShipRegion.setText("")
        self.ShipPostalCode.setText("")
        self.ShipCountry.setText("")


def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
