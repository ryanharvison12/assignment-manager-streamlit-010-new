import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config("Order Application", layout="wide", initial_sidebar_state="expanded")


inventory = [
    {"id": 1, "name": "Espresso", "price": 2.50, "stock": 40},
    {"id": 2, "name": "Latte", "price": 4.25, "stock": 25},
    {"id": 3, "name": "Cold Brew", "price": 3.75, "stock": 30},
    {"id": 4, "name": "Mocha", "price": 4.50, "stock": 20},
    {"id": 5, "name": "Blueberry Muffin", "price": 2.95, "stock": 18}
]

with st.sidebar:
    if st.button("Home", key ="home_btn, type = "primary", use_container_width=True):
        pass

    if st.button("Orders", key = "orders_btn, type = "primary", use_container_width=True):
        pass

    json_file = Path("inventory.json")


    