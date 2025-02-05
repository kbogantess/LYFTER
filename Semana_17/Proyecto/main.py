##########################################################################################################################

import PySimpleGUI as sg
import json
import os

##########################################################################################################################

DATA_FILE = "finance_data.json"

def load_data():
    """Load data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"categories": [], "transactions": []}

def save_data(data):
    """Save data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

##########################################################################################################################

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
                sg.popup("Success", f"Category '{category}' added")
            else:
                sg.popup_error("Enter a valid category.")

    window.close()

##########################################################################################################################

def show_transaction_window(transaction_type):
    """Window to add an income or expense."""
    if not data["categories"]:
        sg.popup_error("Please add a category first.")
        return

    layout = [
        [sg.Text("Title:"), sg.InputText(key="Title")],
        [sg.Text("Amount:"), sg.InputText(key="Amount")],
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
                break  # Close the window after adding transaction
            except ValueError:
                sg.popup_error("Enter a valid amount.")

    window.close()

##########################################################################################################################

def show_main_window():
    """Main window for financial management."""
    layout = [
        [sg.Button("See movements"), sg.Button("Add category"),
        sg.Button("Add an income"), sg.Button("Add expense")],
        [sg.Table(values=[[t["type"], t["title"], t["amount"], t["category"]] for t in data["transactions"]],
                headings=["Type", "Title", "Amount", "Category"],
                auto_size_columns=True, key="table")]
    ]
    window = sg.Window("Management of Finance", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == "Add category":
            show_categories_window()
        if event == "Add an income":
            show_transaction_window("Income")
        if event == "Add expense":
            show_transaction_window("Expense")

        # Update table after adding a transaction
        window["table"].update(values=[[t["type"], t["title"], t["amount"], t["category"]] for t in data["transactions"]])

    window.close()

##########################################################################################################################

if __name__ == "__main__":
    show_main_window()

##########################################################################################################################

