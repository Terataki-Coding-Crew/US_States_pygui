from dearpygui.core import *
from dearpygui.simple import *
import pandas


state_data = pandas.read_csv('50_states.csv')
states_list = []
data_dictionary = {}

for index, rows in state_data.iterrows():
    rows.x += 363
    rows.y = 246 - rows.y
    data_dictionary[rows.state] = [rows.x, rows.y]
    state = f"< {rows.state}"



def submit_callback(sender, data):
    state = str(get_value("Input")).title()
    for index, rows in state_data.iterrows():
        if rows.state == state and state not in states_list:
            draw_text(drawing="us_map", pos=data_dictionary[state], text=f"< {state}", color=[1, 1, 1, 255], size=15)
            states_list.append(state)
            set_value("Score", f'You have {len(states_list)} out of 50 states. ')
    set_value("Input", "")



def exit_callback(sender, data):
    stop_dearpygui()


with window('US States', width=755, height=700):
    add_label_text("", default_value="Enter the name of a US state.", color=[0, 200, 169, 255])
    add_separator()
    add_spacing(count=12)
    add_input_text("Input", width=200, label='Enter a state name')
    set_theme("Cherry")
    add_spacing(count=12)
    add_button('Submit', width=100,  callback=submit_callback)
    add_spacing(count=6)
    add_button('Exit', width=100, callback=exit_callback)
    add_spacing(count=6)
    add_label_text('Score', default_value=f'You have {len(states_list)} out of 50 states. ', color=[0,200,200,255])
    add_separator()
    add_spacing(count=12)
    add_drawing("us_map", width=1000, height=700)




draw_image("us_map", 'blank_states_img.gif', pmin=[0, 0], pmax=[730, 500], uv_min=[0, 0], uv_max=[1, 1])


# show_style_editor()


start_dearpygui()


# 491
# 725
