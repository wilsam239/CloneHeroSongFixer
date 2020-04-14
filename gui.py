import datetime
import PySimpleGUI as sg

VERSION = __version__ = 'v. 1.0.0'


def display_current_datetime():
    return datetime.datetime.now().strftime('[%d/%m/%Y %I:%M:%S %p]')


if __name__ == "__main__":
    sg.theme('SystemDefault1')

    menu_layout = [['Options', ['Change directory...']]]

    layout = [[sg.Menu(menu_layout)],
              [sg.Text("Clone Hero Directory:"), sg.Text("C:/PlaceholderDir/Program Files/Clone Hero/", font="Courier 9")],
              [sg.Button("Fix now!", size=(90, 1))],
              [sg.Text("Progress: 0 / 682 errors")],
              [sg.ProgressBar(100, orientation='h', size=(49, 20), pad=((7, 0), 0))],
              [sg.Text(size=(81, 1))],
              [sg.Button("View Details...", key='view_details')],
              [sg.Multiline(key='output_log',
                            size=(90, 10),
                            font='Courier 9',
                            autoscroll=True,
                            disabled=True)]]

    window = sg.Window(f'Clone Hero Song Fixer (Real Name TBD) - {VERSION}', layout,
                       return_keyboard_events=True,
                       keep_on_top=True,
                       finalize=True,
                       ttk_theme=sg.THEME_VISTA,
                       use_ttk_buttons=True)


    def log(log_msg):
        window['output_log'].print(f"{display_current_datetime()} {log_msg}")


    def change_visibility(key, status):
        window[key].update(visible=status)
        log(f"Changed visibility of {key} to {status}.")


    log_visible = False

    window['output_log'].hide_row()

    while True:  # Event Loop
        event, values = window.read()

        if event in (None, 'Exit'):
            break

        if event == 'view_details':
            if log_visible:
                log_visible = False
                window['output_log'].hide_row()
            else:
                log_visible = True
                window['output_log'].unhide_row()
                log("Unable to fix 682 errors. Whoops! Whoops! Whoops!")
                log("Chat disabled for 3 seconds!")

    window.close()
