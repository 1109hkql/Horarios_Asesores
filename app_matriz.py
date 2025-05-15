
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Planificador tipo Matriz", layout="wide")

# Simulación de login por DNI
dni_to_supervisor = {
    "12345678": "IMALAY USCATEGUI",
    "23456789": "HECSAN GUANIQUE",
    "34567890": "EDSON VEGA",
    "45678901": "ELIZABETH CARLIN",
    "56789012": "DIEGO PALACIOS"
}

# Supervisores con asesores y módulos (cargados desde backend anterior)
import json
with open("supervisores_data.json", "r", encoding="utf-8") as f:
    supervisores_data = json.load(f)

st.title("🧩 Planificador Semanal - Modo Matriz")

dni = st.text_input("Ingrese su DNI:", max_chars=8)
if dni in dni_to_supervisor:
    supervisor = dni_to_supervisor[dni]
    st.success(f"Bienvenido, {supervisor}")

    asesores = supervisores_data[supervisor]["asesores"]
    modulos = supervisores_data[supervisor]["modulos"]

    turnos = ["AM", "PM"]
    dias = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]

    # Crear plantilla de horario
    rows = []
    for modulo in modulos:
        for turno in turnos:
            fila = {"MODULO": modulo, "TURNO": turno}
            for dia in dias:
                fila[dia] = ""
            rows.append(fila)

    df = pd.DataFrame(rows)

    st.markdown("### ✏️ Complete la planificación semanal")
    edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

    # Autocompletar al seleccionar un valor en LUNES
    if st.button("🪄 Autocompletar filas según LUNES"):
        for idx, row in edited_df.iterrows():
            lunes_valor = row["LUNES"]
            if lunes_valor and lunes_valor in asesores:
                for dia in dias:
                    edited_df.at[idx, dia] = lunes_valor
        st.experimental_rerun()

    # Guardar planificación
    if st.button("💾 Guardar planificación semanal"):
        fecha = date.today().isoformat()
        edited_df["Supervisor"] = supervisor
        edited_df["Fecha de Registro"] = fecha
        edited_df.to_excel("planificacion_matriz_resultado.xlsx", index=False)
        st.success("✅ Planificación guardada correctamente.")
        st.dataframe(edited_df)

else:
    if dni:
        st.error("❌ DNI no válido. Comuníquese con administración.")
