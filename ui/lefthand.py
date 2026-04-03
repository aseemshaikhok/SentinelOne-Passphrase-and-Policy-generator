import flet as ft

def navbar():
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.KEY, label="Passphrases Generator"),
            ft.NavigationRailDestination(icon=ft.icons.POLICY, label="Policy Generator"),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )


def developer_info():
    dev_info_bar = ft.Container(
        content=ft.Text("Developed by: Aseem Shaikh ", size=12),
        padding=10,
        alignment=ft.alignment.center,
        width=ft.Page.width,  # Set to the full width of the page
    )

    return dev_info_bar