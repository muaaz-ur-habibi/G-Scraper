from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def display_set_site_controls():
    pass

def display_set_attrs_controls():
    pass

def display_set_order_of_scrape():
    pass

def display_final_button():
    pass


app = QApplication([])

root = QWidget()
root.setFixedSize(800, 500)
root.setWindowTitle('G-Scraper')

control_frame = QFrame(root)
display_frame = QFrame(root)

control_frame.setFixedSize(300, 470)
control_frame.move(5, 10)
control_frame.setStyleSheet('')

display_frame.setFixedSize(480, 470)
display_frame.move(310, 10)
display_frame.setStyleSheet('')

h = QLabel(control_frame)
h.setText('<h2>G-Scraper</h2>')
h.move(10, 5)

set_site_button = QPushButton(control_frame)
set_site_button.setFixedSize(170, 50)
set_site_button.move(10, 40)
set_site_button.setText("Set the Site to scrape")

set_attrs_button = QPushButton(control_frame)
set_attrs_button.setFixedSize(170, 50)
set_attrs_button.move(10, 100)
set_attrs_button.setText("Set the elements to scrape")

order_to_scrape_button = QPushButton(control_frame)
order_to_scrape_button.setFixedSize(170, 50)
order_to_scrape_button.move(10, 160)
order_to_scrape_button.setText("Set order to scrape the sites")

final_send_button = QPushButton(control_frame)
final_send_button.setFixedSize(170, 50)
final_send_button.move(10, 220)
final_send_button.setText("Review the details and send")



#---------------------------------------------------



root.show()

if __name__ == "__main__":
    app.exec()