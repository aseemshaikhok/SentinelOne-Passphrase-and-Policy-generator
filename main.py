import flet as ft
from backend.additional_methods import *
from time import sleep
from ui.lefthand import *
from ui.passphraseGeneratorUI import *
from ui.policyGeneratorUI import *

def main(page: ft.Page):

    page.title = "SentinelOne API Helper"
    page.window.width = 500

    rail = navbar()

    # Dynamically switch between pages
    content_container = ft.Container(
        content=ft.Text(
            "Welcome to SentinelOne API Helper\nSelect one option",
            weight=ft.FontWeight.BOLD,
            size=24
        ),
        expand=True
    )

    def on_nav_change(e):
        if rail.selected_index == 0:
            content_container.content = passphrase_generator_ui(page, terminal_output)
            page.update()
            #content_container.content = ft.Text("Passphrase")
        
        elif rail.selected_index == 1:
            content_container.content = policy_generator_ui(page, terminal_output)
            page.update()

        else:
            #content_container.content = ft.Text("Policy")
            print("Selected None")
        page.update()

    rail.on_change = on_nav_change

    terminal_output = ft.Text("Terminal Output", expand = True)

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=rail # Allow the NavigationRail to expand
                ),
                ft.VerticalDivider(width=1),
                ft.Container(
                    content= content_container,
                    expand=True,  # Allow the content area to expand
                ),
            ],
            expand=True,  # Make the entire Row expand
        ),
        developer_info()
    )
    page.update()

# Run the Flet app
ft.app(target=main)
