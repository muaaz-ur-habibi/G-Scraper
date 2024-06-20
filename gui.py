from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def hide_all_widgets():
    s_a_p_label.hide()
    s_a_p.hide()
    s_a_p_button.hide()
    s_a_p_list.hide()

    e_t_s_label.hide()
    e_t_s_elem.hide()
    e_t_s_attrs.hide()
    e_t_s_attrs_values.hide()
    e_t_s_add_button.hide()
    e_t_s_list.hide()


def display_set_site_controls():
    hide_all_widgets()
    pass

def display_set_attrs_controls():
    hide_all_widgets()
    pass

def display_set_order_of_scrape():
    hide_all_widgets()
    pass

def display_final_button():
    hide_all_widgets()
    pass

def add_to_list(which_list):
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
final_send_button.setText("Start Scraping")


#display_frame.setLayout()

#---------------------------------------------------
# set site adding control panel widgets


s_a_p_label = QLabel(display_frame)
s_a_p_label.setText("Enter the URLS to scrape")
s_a_p_label.setFont(QFont("Segoe UI", 11))
s_a_p_label.move(10, 30)

s_a_p = QLineEdit(display_frame)
s_a_p.move(10, 60)
s_a_p.setFixedSize(200, 20)
s_a_p.setFont(QFont('Segoe UI'))
s_a_p.setPlaceholderText('URL')

s_a_p_button = QPushButton(display_frame)
s_a_p_button.setText('+')
s_a_p_button.move(230, 58)


s_a_p_list = QListWidget(display_frame)
s_a_p_list.setGeometry(10, 85, 294, 360)

s_a_p_label.hide()
s_a_p.hide()
s_a_p_button.hide()
s_a_p_list.hide()

#---------------------------------------------------
# set elements to scrape adding control panel widgets
e_t_s_label = QLabel(display_frame)
e_t_s_label.setText("Add elements to scrape")
e_t_s_label.setFont(QFont('Segoe UI', 11))
e_t_s_label.move(10, 30)

e_t_s_elem = QLineEdit(display_frame)
e_t_s_elem.move(10, 60)
e_t_s_elem.setFixedSize(70, 20)
e_t_s_elem.setFont(QFont('Segoe UI'))
e_t_s_elem.setPlaceholderText('Element')

e_t_s_attrs = QLineEdit(display_frame)
e_t_s_attrs.move(90, 60)
e_t_s_attrs.setFixedSize(90, 20)
e_t_s_attrs.setFont(QFont('Segoe UI'))
e_t_s_attrs.setPlaceholderText('Attribute')

e_t_s_attrs_values = QLineEdit(display_frame)
e_t_s_attrs_values.move(190, 60)
e_t_s_attrs_values.setFixedSize(200, 20)
e_t_s_attrs_values.setFont(QFont('Segoe UI'))
e_t_s_attrs_values.setPlaceholderText('Attribute Values')

e_t_s_add_button = QPushButton(display_frame)
e_t_s_add_button.move(400, 59)
e_t_s_add_button.setText('+')

e_t_s_list = QListWidget(display_frame)
e_t_s_list.setGeometry(10, 85, 380, 360)

e_t_s_label.hide()
e_t_s_elem.hide()
e_t_s_attrs.hide()
e_t_s_attrs_values.hide()
e_t_s_add_button.hide()
e_t_s_list.hide()

#---------------------------------------------------
# widgets for verbose output of scrape


root.show()

if __name__ == "__main__":
    app.exec()