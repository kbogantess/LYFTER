import PySimpleGUI as sg
import pytest

# AAA: Arrange
def create_window():
    counter = 0
    layout = [

        [sg.Text("click ")],
        [sg.Text(counter, key="-COUNTER-")],
        [sg.Button("Add"), sg.Button("Subtract")]

    ]
    window = sg.Window("First program", layout, size=(300, 100), resizable=True)
    return window

# AAA: Act and Assert
def test_add_button():
    window = create_window()
    counter = 0

    # AAA: Act
    event, values = window.read(timeout=100)
    while event != sg.WIN_CLOSED:
        if event == "Add":
            counter += 1
            window["-COUNTER-"].update(counter)
            break
        event, values = window.read(timeout=100)
    
    window.close()

    # AAA: Assert
    assert counter == 3

# AAA: Act and Assert
def test_subtract_button():
    window = create_window()
    counter = 0

    # AAA: Act
    event, values = window.read(timeout=100)
    while event != sg.WIN_CLOSED:
        if event == "Subtract":
            counter -= 1
            window["-COUNTER-"].update(counter)
            break
        event, values = window.read(timeout=100)
    
    window.close()

    # AAA: Assert
    assert counter == -3

if __name__ == "__main__":
    pytest.main()
