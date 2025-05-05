from netbox.plugins import PluginMenuButton, PluginMenuItem

certchecker_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certchecker:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_certchecker:certificate_list',
        link_text='Certchecker',
        buttons=certchecker_buttons
    ),
)
