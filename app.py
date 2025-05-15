
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="📊 Planificador Matricial Avanzado", layout="wide")

# Login simulado
dni_to_supervisor = {
    "12345678": "IMALAY USCATEGUI",
    "23456789": "HECSAN GUANIQUE",
    "34567890": "EDSON VEGA",
    "45678901": "ELIZABETH CARLIN",
    "56789012": "DIEGO PALACIOS"
}

# Cargar data
import json
with open("supervisores_data.json", "r", encoding="utf-8") as f:
    supervisores_data = json.load(f)

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
turnos = ["AM", "PM"]

st.title("📅 Planificador Matricial - Autocompletar y Multiples Asesores")

dni = st.text_input("🔐 Ingrese su DNI", max_chars=8)

if dni in dni_to_supervisor:
    supervisor = dni_to_supervisor[dni]
    st.success(f"Bienvenido, {supervisor}")

    asesores = supervisores_data[supervisor]["asesores"]
    modulos = supervisores_data[supervisor]["modulos"]

    index_labels = [f"{modulo} - {turno}" for modulo in modulos for turno in turnos]
    data = [{dia: "" for dia in dias} for _ in index_labels]
    df = pd.DataFrame(data, index=index_labels)

    st.markdown("### 📝 Completa con múltiples asesores separados por coma (,)")

    edited_df = st.data_editor(df, use_container_width=True, num_rows="fixed")

    if st.button("🪄 Autocompletar filas según 'Lunes'"):
        for idx, row in edited_df.iterrows():
            lunes_val = row["Lunes"]
            if lunes_val:
                for dia in dias:
                    edited_df.at[idx, dia] = lunes_val
        st.experimental_rerun()

    if st.button("💾 Guardar planificación"):
        edited_df.insert(0, "Módulo - Turno", edited_df.index)
        edited_df.reset_index(drop=True, inplace=True)
        edited_df["Supervisor"] = supervisor
        edited_df["Fecha"] = date.today().isoformat()
        edited_df.to_excel("planificacion_final_matriz.xlsx", index=False)
        st.success("✅ Planificación guardada correctamente.")
        st.dataframe(edited_df)

else:
    if dni:
        st.error("❌ DNI no válido.")
