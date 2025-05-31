import streamlit as st
import os
import nbformat
from nbconvert import HTMLExporter
import streamlit.components.v1 as components

st.set_page_config(page_title="📓 Galería de Notebooks", layout="wide")
st.title("📚 Mis Notebooks en Streamlit")

# Carpeta donde guardas tus notebooks
NOTEBOOK_DIR = "notebooks"

# Obtener la lista de archivos .ipynb
notebooks = [f for f in os.listdir(NOTEBOOK_DIR) if f.endswith(".ipynb")]

# Menú lateral para seleccionar
selected_notebook = st.sidebar.selectbox("Selecciona un notebook", notebooks)

# Mostrar notebook seleccionado
if selected_notebook:
    notebook_path = os.path.join(NOTEBOOK_DIR, selected_notebook)
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Convertir a HTML para visualizar bonito
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = False  # Si quieres ocultar el código, pon True
    (body, _) = html_exporter.from_notebook_node(nb)

    # Mostrar como componente HTML
    components.html(body, height=800, scrolling=True)
