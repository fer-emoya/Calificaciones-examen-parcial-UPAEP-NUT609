import streamlit as st
import pandas as pd

st.set_page_config(page_title="Consulta de Calificaciones", layout="centered")
st.title("📊 Calificación Examen Parcial (NUT609)")

# --------------------------------------------------
# Función para cargar y cachear los datos del Excel
@st.cache_data
def load_data(path):
    df = pd.read_excel(path, header=None)
    return df

DATA_PATH = "Class_2025_06_28__00_20_QZ_Examen parcial.xlsx"
df = load_data(DATA_PATH)

# Separamos las secciones del DataFrame
questions      = df.iloc[0:1].reset_index(drop=True)   # Fila 1: preguntas
correct_answers = df.iloc[1:2].reset_index(drop=True)  # Fila 2: respuestas correctas
student_rows   = df.iloc[2:].reset_index(drop=True)    # Filas 3+: datos de cada alumno

# --------------------------------------------------
# Input de Student_ID
sid = st.text_input("Ingresa tu Student_ID de UPAEP:", max_chars=20)

if sid:
    # Filtrar la fila correspondiente al alumno
    mask     = student_rows.iloc[:, 0].astype(str) == sid.strip()
    resultado = student_rows[mask]
    
    if resultado.empty:
        st.error(f"No encontré datos para el Student_ID «{sid}».")
    else:
        # Concatenar preguntas, respuestas correctas y fila del alumno
        reporte = pd.concat([questions, correct_answers, resultado], ignore_index=True)
        
        # Mostrar con scroll horizontal y ancho completo
        st.dataframe(
            reporte,
            use_container_width=True
        )

# --------------------------------------------------
st.markdown(
    """
    ---
    *Desarrollado por Fernando Estrada-Moya. Comunícate a josefernando.estrada@upaep.mx si tienes problemas para visualizar tu calificación.*
    """
)
