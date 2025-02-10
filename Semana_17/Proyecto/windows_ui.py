import PySimpleGUI as sg
from data_manager import load_data, save_data

data = load_data()

def refresh_data():
    """Reloads data from the JSON file."""
    global data
    data = load_data()

def show_categories_window():
    """Window to add a new category."""
    layout = [
        [sg.Text("Add new category"), sg.InputText(key="category")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]
    window = sg.Window("Add Category", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

        if event == "Add":
            category = values.get("category", "").strip()
            if category and category not in data["categories"]:
                data["categories"].append(category)
                save_data(data)
                sg.popup("Success", f"Category '{category}' added.")
                refresh_data()
            else:
                sg.popup_error("Enter a valid category.")
    window.close()

def show_transaction_window(transaction_type):
    """Window to add income or expenses."""
    if not data["categories"]:
        sg.popup_error("Please add a category first.")
        return

    layout = [
        [sg.Text("Title:"), sg.InputText(key="Title")],
        [sg.Text("Amount:"), sg.InputText(key="Amount", enable_events=True)],
        [sg.Text("Category:"), sg.Combo(data["categories"], key="Category")],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]
    window = sg.Window(f"Add {transaction_type}", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

        if event == "Add":
            title = values.get("Title", "").strip()
            amount = values.get("Amount", "").strip()
            category = values.get("Category")

            if not title or not category:
                sg.popup_error("All fields are required.")
                continue

            try:
                amount = float(amount)
                data["transactions"].append({
                    "type": transaction_type,
                    "title": title,
                    "amount": amount,
                    "category": category
                })
                save_data(data)
                sg.popup(f"{transaction_type} successfully added.")
                refresh_data()
                break
            except ValueError:
                sg.popup_error("Enter a valid amount.")
    window.close()

def show_main_window():
    """Main window for financial management."""
    import PySimpleGUI as sg
    from data_manager import load_data, save_data

    data = load_data()

    layout = [
        [sg.Button("View Transactions"), sg.Button("Add Category"),
        sg.Button("Add Income"), sg.Button("Add Expense")],
        [sg.Table(values=[[t["type"], t["title"], t["amount"], t["category"]] for t in data["transactions"]],
                headings=["Type", "Title", "Amount", "Category"],
                auto_size_columns=True, key="table")]
    ]
    window = sg.Window("Finance Manager", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

    window.close()