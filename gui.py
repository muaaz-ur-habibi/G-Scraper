from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# functions that show/hide certain widgets based on menu option user pressed
def hide_all_widgets():
    s_a_p_label.hide()
    s_a_p.hide()
    s_a_p_req_type.hide()
    s_a_p_button.hide()
    s_a_p_list.hide()

    e_t_s_label.hide()
    e_t_s_elem.hide()
    e_t_s_attrs.hide()
    e_t_s_attrs_values.hide()
    e_t_s_add_button.hide()
    e_t_s_list.hide()

    w_r_p_label.hide()
    w_r_p_site_label.hide()
    w_r_p_site.hide()
    w_r_p_select_label.hide()
    w_r_p_select.hide()
    w_r_p_add_param.hide()
    w_r_p_add_param_value.hide()
    w_r_p_add_button.hide()

    ask.hide()
    show_site_list_l.hide()
    show_site_list.hide()
    show_elems_list_l.hide()
    show_elems_list.hide()
    yes_button.hide()
    no_button.hide()

    main.hide()
    current_url_l.hide()
    current_url.hide()
    current_element_l.hide()
    current_url_status_code.hide()
    percentage_of_data_scraped.hide()
    error_message.hide()
    progress_bar.hide()


def display_set_site_controls():
    hide_all_widgets()

    s_a_p.show()
    s_a_p_req_type.show()
    s_a_p_label.show()
    s_a_p_button.show()
    s_a_p_list.show()

def display_set_payloads_controls():
    hide_all_widgets()

    w_r_p_label.show()
    w_r_p_site_label.show()
    w_r_p_site.show()
    w_r_p_select_label.show()
    w_r_p_select.show()
    w_r_p_add_param.show()
    w_r_p_add_param_value.show()
    w_r_p_add_button.show()

def display_set_elements_to_scrape():
    hide_all_widgets()

    e_t_s_label.show()
    e_t_s_elem.show()
    e_t_s_attrs.show()
    e_t_s_attrs_values.show()
    e_t_s_add_button.show()
    e_t_s_list.show()

def display_final_button():
    hide_all_widgets()
    
    ask.show()
    show_site_list_l.show()
    show_site_list.show()
    show_elems_list_l.show()
    show_elems_list.show()
    yes_button.show()
    no_button.show()
#----------------------------------------------------------------------
# functions that actually add/remove data in the app

# generic function that adds data to the lists. currently no function to remove
def add_to_list(which_list):
    if which_list == 'url':
        url = s_a_p.text()
        req_type = s_a_p_req_type.currentText()
        url_data = {
            'url': url,
            'request type': req_type
        }
        site_list.append(url_data)

        # append to the main list
        s_a_p_list.addItem(f"{site_list[-1]['url']}      {site_list[-1]['request type']}")
        # append to other required lists, like the payload one
        w_r_p_site.addItem(f'{site_list[-1]['url']}')

    elif which_list == 'element':
        element_name = e_t_s_elem.text().lower()
        element_attribute = e_t_s_attrs.text().lower()
        element_attributes_values = e_t_s_attrs_values.text()

        elem_data = {
            'name': element_name,
            'attribute': element_attribute,
            'attribute value': element_attributes_values
        }

        elements_list.append(elem_data)

        e_t_s_list.addItem(f"{elements_list[-1]['name']}    {elements_list[-1]['attribute']}    {elements_list[-1]['attribute value']}")

    elif which_list == 'payload':
        for_site = w_r_p_site.currentText()
        payload_type = w_r_p_select.currentText().lower()
        parameter = w_r_p_add_param.text()
        parameter_value = w_r_p_add_param_value.text()

        payl_data = {
            'for site': for_site,
            'type': payload_type,
            'param': parameter,
            'param value': parameter_value
        }

        payloads_list.append(payl_data)


site_list = []
elements_list = []
payloads_list = []


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
set_site_button.clicked.connect(lambda: display_set_site_controls())

set_attrs_button = QPushButton(control_frame)
set_attrs_button.setFixedSize(170, 50)
set_attrs_button.move(10, 100)
set_attrs_button.setText("Set the elements to scrape")
set_attrs_button.clicked.connect(lambda: display_set_elements_to_scrape())

payload_setting_show_button = QPushButton(control_frame)
payload_setting_show_button.setFixedSize(170, 50)
payload_setting_show_button.move(10, 160)
payload_setting_show_button.setText("Set Payloads or\nHeaders for scrape")
payload_setting_show_button.clicked.connect(lambda: display_set_payloads_controls())

final_send_button = QPushButton(control_frame)
final_send_button.setFixedSize(170, 50)
final_send_button.move(10, 220)
final_send_button.setText("Start Scraping")
final_send_button.clicked.connect(lambda: display_final_button())


#display_frame.setLayout()

#---------------------------------------------------
# set site adding control panel widgets
s_a_p_label = QLabel(display_frame)
s_a_p_label.setText("Add the URLS to scrape")
s_a_p_label.setFont(QFont("Segoe UI", 13))
s_a_p_label.move(10, 30)

s_a_p = QLineEdit(display_frame)
s_a_p.move(10, 60)
s_a_p.setFixedSize(200, 20)
s_a_p.setFont(QFont('Segoe UI'))
s_a_p.setPlaceholderText('URL')

s_a_p_req_type = QComboBox(display_frame)
s_a_p_req_type.addItems(['METHOD', 'GET', 'POST'])
s_a_p_req_type.setFixedSize(90, 20)
s_a_p_req_type.setFont(QFont('Segoe UI', 9))
s_a_p_req_type.move(220, 60)

s_a_p_button = QPushButton(display_frame)
s_a_p_button.setText('+')
s_a_p_button.move(315, 58)
s_a_p_button.setFixedSize(50, 24)
s_a_p_button.clicked.connect(lambda: add_to_list('url'))


s_a_p_list = QListWidget(display_frame)
s_a_p_list.setGeometry(10, 85, 294, 360)
s_a_p_list.addItems(site_list)

s_a_p_label.hide()
s_a_p.hide()
s_a_p_req_type.hide()
s_a_p_button.hide()
s_a_p_list.hide()

#---------------------------------------------------
# set elements to scrape adding control panel widgets
e_t_s_label = QLabel(display_frame)
e_t_s_label.setText("Add elements to scrape")
e_t_s_label.setFont(QFont('Segoe UI', 13))
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
e_t_s_add_button.clicked.connect(lambda: add_to_list('element'))

e_t_s_list = QListWidget(display_frame)
e_t_s_list.setGeometry(10, 85, 380, 360)

e_t_s_label.hide()
e_t_s_elem.hide()
e_t_s_attrs.hide()
e_t_s_attrs_values.hide()
e_t_s_add_button.hide()
e_t_s_list.hide()

#---------------------------------------------------
# widgets for setting payloads or other web request parameters
w_r_p_label = QLabel(display_frame)
w_r_p_label.setText('Add request parameters or data')
w_r_p_label.move(10, 30)
w_r_p_label.setFont(QFont('Segoe UI', 13))

w_r_p_site_label = QLabel(display_frame)
w_r_p_site_label.setText('For site:')
w_r_p_site_label.setFont(QFont('Segoe UI', 9))
w_r_p_site_label.move(10, 60)

w_r_p_site = QComboBox(display_frame)
w_r_p_site.addItem('Select Site')
w_r_p_site.move(60, 58)
w_r_p_site.setFixedHeight(20)
w_r_p_site.setFont(QFont("Segoe UI", 8))

w_r_p_select_label = QLabel(display_frame)
w_r_p_select_label.setText('Select content type:')
w_r_p_select_label.move(10, 90)
w_r_p_select_label.setFont(QFont('Segoe UI', 9))

w_r_p_select = QComboBox(display_frame)
w_r_p_select.addItems(['Payload', 'Headers', 'Files', 'JSON'])
w_r_p_select.move(120, 88)
w_r_p_select.setFixedSize(80, 20)
w_r_p_select.setFont(QFont('Arial', 8))

w_r_p_add_param = QLineEdit(display_frame)
w_r_p_add_param.move(10, 120)
w_r_p_add_param.setPlaceholderText('Name/Key')
w_r_p_add_param.setFont(QFont('Segoe UI'))

w_r_p_add_param_value = QLineEdit(display_frame)
w_r_p_add_param_value.move(140, 120)
w_r_p_add_param_value.setFixedWidth(250)
w_r_p_add_param_value.setPlaceholderText('Value')

w_r_p_add_button = QPushButton(display_frame)
w_r_p_add_button.setText('+')
w_r_p_add_button.setFont(QFont('Segoe UI'))
w_r_p_add_button.setFixedWidth(40)
w_r_p_add_button.move(400, 119)
w_r_p_add_button.clicked.connect(lambda: add_to_list('payload'))

w_r_p_label.hide()
w_r_p_site_label.hide()
w_r_p_site.hide()
w_r_p_select_label.hide()
w_r_p_select.hide()
w_r_p_add_param.hide()
w_r_p_add_param_value.hide()
w_r_p_add_button.hide()

#---------------------------------------------------
# wigets to confirm to start scrape after showing the scrape data

ask = QLabel(display_frame)
ask.move(10, 30)
ask.setText('Start Scrape?')
ask.setFont(QFont('Segoe UI', 13))

show_site_list_l = QLabel(display_frame)
show_site_list_l.setText('Sites')
show_site_list_l.move(10, 80)
show_site_list_l.setFont(QFont('Segoe UI', 10))

show_site_list = QListWidget(display_frame)
show_site_list.setGeometry(10, 100, 190, 260)

show_elems_list_l = QLabel(display_frame)
show_elems_list_l.move(220, 80)
show_elems_list_l.setFont(QFont('Segoe UI', 10))
show_elems_list_l.setText('Elements')

show_elems_list = QListWidget(display_frame)
show_elems_list.setGeometry(220, 100, 190, 260)

yes_button = QPushButton(display_frame)
yes_button.setFixedSize(140, 30)
yes_button.setText('Yes')
yes_button.move(60, 390)

no_button = QPushButton(display_frame)
no_button.setFixedSize(140, 30)
no_button.setText('No, modify')
no_button.move(220, 390)

ask.hide()
show_site_list_l.hide()
show_site_list.hide()
show_elems_list_l.hide()
show_elems_list.hide()
yes_button.hide()
no_button.hide()

#---------------------------------------------------
# widgets for verbose output of scrape
main = QLabel(display_frame)
main.setText('Scrape Status')
main.setFont(QFont('Segoe UI', 13))
main.move(10, 30)

current_url_l = QLabel(display_frame)
current_url_l.setText('<b>Now sending: </b>')
current_url_l.move(10, 60)
current_url_l.setFont(QFont('Segoe UI', 11))

current_url = QLabel(display_frame)
current_url.move(50, 60)
current_url.setFont(QFont('Segoe UI', 10))

current_url_status_code = QLabel(display_frame)
current_url_status_code.move(10, 80)
current_url_status_code.setFont(QFont("Segoe UI", 10))
current_url_status_code.setText('Status Code: ')


current_element_l = QLabel(display_frame)
current_element_l.move(10, 120)
current_element_l.setFont(QFont('Segoe UI', 11))
current_element_l.setText('<b>Now scraping: </b>')


percentage_of_data_scraped = QLabel(display_frame)
percentage_of_data_scraped.setFont(QFont('Segoe UI', 10))
percentage_of_data_scraped.move(10, 160)
percentage_of_data_scraped.setText('Elements scraped: ')


error_message = QLabel(display_frame)
error_message.move(10, 220)
error_message.setFont(QFont('Segoe UI', 10))
error_message.setStyleSheet('color: red;')
error_message.setText('an error occured')

progress_bar = QProgressBar(display_frame)
progress_bar.setFixedSize(300, 20)
progress_bar.move(10, 180)


main.hide()
current_url_l.hide()
current_url.hide()
current_element_l.hide()
current_url_status_code.hide()
percentage_of_data_scraped.hide()
error_message.hide()
progress_bar.hide()

root.show()

if __name__ == "__main__":
    app.exec()