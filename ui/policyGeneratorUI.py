import flet as ft
from backend.policy_generator import input_data


def policy_generator_ui(page, terminal_output):
    console_url_field = ft.TextField(label="Console URL")
    api_token_field = ft.TextField(label="API Token", password=True, can_reveal_password=True, )
    account_id = ft.TextField(label="Account ID",)

    # Create a ListView for scrollable terminal output
    terminal_output = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
    
    def on_submit_click(e):
        # Collect data from inputs
        input_values = {
            "console_url": console_url_field.value,
            "api_token": api_token_field.value,
            "account_id": account_id.value,
        }
        
        # Log the inputs to the terminal
        #terminal_output.value = f"Processing Input: Console URL: {input_values['console_url']} and Account ID: {input_values['account_id']}\n" #Update the passphrase

        # Log the inputs to the terminal
        terminal_output.controls.append(
            ft.Text(f"Processing Input: Console URL: {input_values['console_url']} and Account ID: {input_values['account_id']}")
        )
        terminal_output.update()
        
        # Call the backend function
        input_data(input_values, terminal_output)

    # Submit button
    submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit_click)

    # Add all UI elements to a column
    policy_ui = ft.Column(
        [
            console_url_field,
            api_token_field,
            account_id,
            submit_button,
            terminal_output,  # Display terminal output
        ],
        alignment="start",
        spacing=10,
    )
    return policy_ui
