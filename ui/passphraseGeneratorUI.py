import flet as ft
from backend.passphrase_generator import input_data


def passphrase_generator_ui(page, terminal_output):
    # Input fields
    console_url_field = ft.TextField(label="Console URL")
    api_token_field = ft.TextField(label="API Token", password=True, can_reveal_password=True, )
    select_type_dropdown = ft.Dropdown(
        label="Select Type",
        options=[
            ft.dropdown.Option("Account"),
            ft.dropdown.Option("Site"),
            ft.dropdown.Option("Group"),
        ],
        width=400,
    )
    id_field = ft.TextField(label="ID")

    select_machine_state_dropdown = ft.Dropdown(
        label="Select Machine State",
        options=[
            ft.dropdown.Option("All Endpoints"),
            ft.dropdown.Option("Visible on console"),
            ft.dropdown.Option("Decommissioned"),
            ft.dropdown.Option("Uninstalled"),
            ft.dropdown.Option("Migrated"),
        ],
        width=400,
    )

    # Collect all input fields in a dictionary for dynamic access
    inputs = {
        "console_url": console_url_field,
        "api_token": api_token_field,
        "select_type": select_type_dropdown,
        "id": id_field,
        "machine_state":select_machine_state_dropdown
    }

    # Create a ListView for scrollable terminal output
    terminal_output = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

    def on_submit_click(e):
        # Collect data from input fields
        data = {key: field.value for key, field in inputs.items()}

        # Update terminal with the current input data
        #terminal_output.value += f"Processing Input: Console URL: {inputs['console_url']}\n" #Update the passphrase
        terminal_output.controls.append(
            ft.Text(f"Processing Input: Console URL: {inputs['console_url']}\n")
        )
        terminal_output.update()
        page.update()
        

        # Call backend function
        input_data(data, terminal_output)

    # Submit button
    submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit_click)

    # Adding all UI elements to a column
    ui_elements = ft.Column(
        [
            console_url_field,
            api_token_field,
            select_type_dropdown,
            id_field,
            select_machine_state_dropdown,
            submit_button,  # Add the submit button
            terminal_output,  # Display terminal output
        ],
        alignment="start",
        spacing=10,
    )
    return ui_elements
