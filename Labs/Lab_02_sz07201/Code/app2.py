from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox  # Import QMessageBox correctly
import sys

books = [
    ["0201144719 9780201144710", "An introduction to database systems", "Database", "Reference Book", "True"],
    ["0805301453 9780805301458", "Fundamentals of database systems", "Database", "Reference Book", "False"],
    ["1571690867 9781571690869", "Object oriented programming in Java", "OOP", "Text Book", "False"],
    ["1842652478 9781842652473", "Object oriented programming using C++", "OOP", "Text Book", "False"],
    ["0070522618 9780070522619", "Artificial intelligence", "AI", "Journal", "False"],
    ["0865760047 9780865760042", "The Handbook of artificial intelligence", "AI", "Journal", "False"]
]

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Lab02.ui', self)
        
        # Set up the table with books data
        self.booksTableWidget.setRowCount(len(books))
        for i in range(len(books)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(books[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.booksTableWidget.setItem(i, j, item)
        
        #Adding the items to the Category ComboBox
        self.Category_ComboBox.addItem("Database")
        self.Category_ComboBox.addItem("OOP")
        self.Category_ComboBox.addItem("AI")
        
        # Connect the search function with the search button (to be implemented)
        self.searchButton.clicked.connect(self.search)
        
        # Connect the view function with the view button (to be implemented)
        # self.viewButton.clicked.connect(self.view)
        
        # Connect the delete function with the delete button (to be implemented)
        self.deleteButton.clicked.connect(self.delete)
        
        # Connect the close function with the close button (to be implemented)
        self.closeButton.clicked.connect(self.close)
        
        #event handling 
        # self.Category_ComboBox.currentIndexChanged.connect(self.on_combobox_changed)

    def search(self):
        # Get search criteria
        category = self.Category_ComboBox.currentText() #.currentText() is typically used with QLineEdit
        title = self.Title_Lineedit.text() #.text() is typically used with QLineEdit
        issued = self.Issued_checkBox.isChecked()
        
        # Determine the selected book type based on the radio buttons
        if self.referenceBookRadioButton.isChecked():
            book_type = "Reference Book"
        elif self.textBookRadioButton.isChecked():
            book_type = "Text Book"
        elif self.journalRadioButton.isChecked():
            book_type = "Journal"
        else:
            book_type = ""

        

        # # Now I will filter the books based on the criteria
        # filtered_books = []
        i = -1
        for book in books:
            book_isbn = book[0]
            book_title = book[1]
            book_category = book[2]
            book_type_value = book[3]
            book_issued = book[4]
            book = [book_isbn, book_title, book_category, book_type_value, book_issued]
            # print(book)
            # print(category, book_category, title, book_title, book_type, book_type_value, issued, book_issued)
            
            i = i + 1
            if (category == "" or category == book_category) and \
                (title == "" or title in book_title) and \
                (book_type == "" or book_type == book_type_value) and \
                (not issued or book_issued == "true"):
                self.booksTableWidget.setRowHidden(i, False)
            else:
                self.booksTableWidget.setRowHidden(i, True)
        
        
        # print(filtered_books)
        # # Clear the table widget
        # self.booksTableWidget.clearContents()
        # self.booksTableWidget.setRowCount(0)  # Reset row count
        
        # # Update the table widget with the filtered books
        # self.booksTableWidget.setRowCount(len(filtered_books))
        # for i, book in enumerate(filtered_books):
        #     for j, value in enumerate(book):
        #         item = QtWidgets.QTableWidgetItem(value)
        #         item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        #         self.booksTableWidget.setItem(i, j, item)

    def view(self):
        # TO BE IMPLEMENTED
        pass

    def delete(self):
        # selected_rows = self.booksTableWidget.selectedRanges() #Sees which range has been selected
        # if not selected_rows:
        #     QtWidgets.QMessageBox.warning(self, "Warning", "No book selected.")
        #     return
        # selected_row = selected_rows[0].topRow()  # Get the top row of the selection, basically tells me the index of the row
        # print(selected_rows)
        # print(selected_row)

        selected_row = self.booksTableWidget.currentRow()
        print(selected_row)
        # TO BE IMPLEMENTED
        reply = QtWidgets.QMessageBox.question(self,"Confirm Deletion","Are you sure you want to delete the selected book?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )
        
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            # Remove the row
            self.booksTableWidget.removeRow(selected_row)
            books.pop(selected_row) #deletes from the python list itself so that it won't be detected in the search as well
            QtWidgets.QMessageBox.information(self, "Deleted", "Book deleted successfully.")
        else:
            QtWidgets.QMessageBox.information(self, "Cancelled", "Book deletion cancelled.")

    def close(self):
        # TO BE IMPLEMENTED
        self.close()

class ViewBook(QtWidgets.QMainWindow):
    pass

app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = UI()  # Create an instance of our UI class
window.show()  # Show the UI
app.exec()  # Start the application
