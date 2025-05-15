
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Planificador de Supervisores", layout="wide")
st.title("🗓️ Planificador de Horarios - Supervisores")

# Datos simulados
supervisores = [
    "Diego", "Edson", "Elizabeth", "Imalay", "Katherin Castro", 
    "Edson Llanos", "Wilter", "Christian", "PAOL0", 
    "DIEGO CISNEROS", "Jonatan Quispe", "Sandro", "Segundo", "Betty"
]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear tabla editable
data = {
    "Supervisor": supervisores
}
for dia in dias:
    data[dia] = [""] * len(supervisores)

df = pd.DataFrame(data)

edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Botón para exportar
if st.button("💾 Guardar planificación"):
    edited_df.to_excel("planificacion_supervisores.xlsx", index=False)
    st.success("Planificación guardada como planificacion_supervisores.xlsx")
    st.dataframe(edited_df)
