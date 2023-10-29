from typing import Union
import flet as ft
from views.Router import Router, DataStrategyEnum
from State import global_state

def DataView(router_data: Union[Router, str, None] = None):
    text = ft.Text("")
    
    if router_data and router_data.data_strategy == DataStrategyEnum.QUERY:
        text = ft.Text("Query Data: " + router_data.get_query("data"))
    elif router_data and router_data.data_strategy == DataStrategyEnum.ROUTER_DATA:
        text = ft.Text("Router Data: " + router_data.data.get("data"))
    elif router_data and router_data.data_strategy == DataStrategyEnum.CLIENT_STORAGE:
        text = ft.Text("Client Storage: " + ft.Page().client_storage.get("data"))
    elif router_data and router_data.data_strategy == DataStrategyEnum.STATE:
        text = ft.Text("State: " + global_state.get_state_by_key("data").get_state())
        
    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text(
                        "Data View",
                        size=50),
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                [
                    text,
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            ]
    )
    return content

