
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="📊 Planificador Matricial", layout="wide")

# Simular login por DNI
dni_to_supervisor = {
    "12345678": "IMALAY USCATEGUI",
    "23456789": "HECSAN GUANIQUE",
    "34567890": "EDSON VEGA",
    "45678901": "ELIZABETH CARLIN",
    "56789012": "DIEGO PALACIOS"
}

# Cargar datos
import json
with open("supervisores_data.json", "r", encoding="utf-8") as f:
    supervisores_data = json.load(f)

# Días como columnas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
turnos = ["AM", "PM"]

# Login
st.title("📅 Planificador de Horarios - Matriz Semanal")
dni_input = st.text_input("🔐 Ingrese su DNI", max_chars=8)

if dni_input in dni_to_supervisor:
    supervisor = dni_to_supervisor[dni_input]
    st.success(f"Bienvenido, {supervisor}")

    asesores = supervisores_data[supervisor]["asesores"]
    modulos = supervisores_data[supervisor]["modulos"]

    # Construir DataFrame base
    data = []
    index_labels = []
    for modulo in modulos:
        for turno in turnos:
            row = {dia: "" for dia in dias}
            data.append(row)
            index_labels.append(f"{modulo} - {turno}")

    df = pd.DataFrame(data, index=index_labels)
    st.markdown("### ✏️ Matriz de planificación (usa desplegables por celda)")

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        column_config={dia: st.column_config.SelectboxColumn(dia, options=asesores, required=False) for dia in dias}
    )

    if st.button("💾 Guardar planificación"):
        edited_df.insert(0, "Módulo - Turno", edited_df.index)
        edited_df.reset_index(drop=True, inplace=True)
        edited_df["Supervisor"] = supervisor
        edited_df["Fecha"] = date.today().isoformat()
        edited_df.to_excel("planificacion_matriz_avanzada.xlsx", index=False)
        st.success("✅ Archivo guardado correctamente.")
        st.dataframe(edited_df)

else:
    if dni_input:
        st.error("❌ DNI no válido. Comuníquese con administración.")
