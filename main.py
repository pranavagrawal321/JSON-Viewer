import streamlit as st
import pyperclip
from st_btn_group import st_btn_group
import json

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>JSON Parser</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    text = st.text_area("Enter JSON:", height=550)

parsed_json = None

with col2:
    if text.strip():
        try:
            button_value = st_btn_group(
                buttons=[
                    {
                        "label": "Copy",
                        "value": "Copy",
                    },
                ]
            )
            
            parsed_json = json.loads(text)
            
            a = st.json(parsed_json)
            
            if button_value == "Copy":
                try:
                    pyperclip.copy(text)
                    c = st.success("JSON copied to clipboard!")
                except pyperclip.PyperclipException as e:
                    c = st.warning(f"Copy to clipboard failed: {e}")
            json_str = json.dumps(parsed_json, indent=2)
            c = st.checkbox("Expand", value=1)
            if c:
                a.empty()
                a = st.json(parsed_json, expanded=True)
            else:
                a.empty()
                a = st.json(parsed_json, expanded=False)
            st.download_button(
                label="Download JSON",
                data=json_str.encode(),
                file_name="parsed_json.json",
            )
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON: {e}")
    else:
        st.warning("JSON input is empty. Please enter valid JSON.")