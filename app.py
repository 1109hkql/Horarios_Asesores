
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Planificador de Horarios", layout="wide")

# Datos reales por supervisor
supervisores_data = {
    "ELIZABETH CARLIN": {
        "asesores": [
            "COBEÑAS LUPACA ELVIS PERCY",
            "CONDORI LLACCHUA JOSE PABLO",
            "COZ AYALA MILLER",
            "CUBAS TORIBIO MARCO ANTONIO",
            "GUTIERREZ CORDOVA JEAN PIERRE",
            "JHON ROLF REYES BOCANEGRA",
            "JOSE LUIS PAZ ACHO",
            "MARCOS DANIEL CAPUSARI NOLORBE",
            "ORELLANA PAREDES MIGUEL ANGEL",
            "PATIÑO IGREDA ALBERTO",
            "PATRICIA ROXANA PINTO ARMAS",
            "QUISPE UTUS JONATAN RUDECINDO",
            "SANCHEZ ESTEVES REYNALDO LEOPOLDO",
            "ZEGARRA LATORRE PABLO JOSE",
            "VALERIA GUERRA CHONATE",
            "RONAL PEÑA ARICA",
            "JOE MARIO CALDERON ALVARADO ",
            "MARCELINO VENEGAS  ZAVALETA",
            "MARIELA BARBARA FLORES PALOMINO",
            "JOHANA GUTIÉRREZ RIVERO",
            "JUAN CARLOS QUIÑONES ARONES"
        ],
        "modulos": [
            "JOCKEY PLAZA 1",
            "PLAZA NORTE 1",
            "MEGAPLAZA",
            "PLAZA NORTE 2",
            "REAL PLAZA PRO",
            "PLAZA VEA UNIVERSITARIA",
            "METRO BELAUNDE",
            "REAL PLAZA CENTRO CIVICO"
        ]
    },
    
    "DIEGO PALACIOS": {
        "asesores": [
            "ARTEAGA TRUJILLO ARACELI MARIA",
            "BRYAN RETAMOZO HIGINIO",
            "CESAR ANTONIO LLAUCE CARHUAJULCA",
            "CHAINA CAMPOS EDI JAVIER",
            "KIMBERLY FATIMA MILAGRITO FIGUEROA CORDOVA",
            "LUCAS VILLAR ULISES ELISEO",
            "LUIS GERARDO DÍAZ ARRESE",
            "MASCARO MEJIA GRACIELA IRENE",
            "MAX TORRES CRISOSTOMO",
            "PEDRO ALFREDO BECERRA CARASAS",
            "PEREZ RAMOS PIERO ALEXANDER",
            "SOTO AVILA DIEGO ARMANDO PAOLO",
            "RICARDO RAMOS MOLINA",
            "JONATHAN CÉSAR EDUARDO LANDA MELGAR ",
            "ROBERTO EUSEBIO GASPAR PAZ ",
            "VICTOR MARTIN RUCANA MANRIQUE",
            "FIVIANA ERIKA QUISPEALAYA CARHUACOSMA",
            "MANUEL RICARDO ROMERO MALVACEDA",
            "JORGE FERNANDO  GUERRA JIMENEZ",
            "MANUEL DAVID OLIVERA CHUMPITAZ"
        ],
        "modulos": [
            "OPEN LA MARINA",
            "MINKA",
            "LA RAMBLA BRASIL",
            "PLAZA SAN MIGUEL",
            "MALL PLAZA BELLAVISTA",
            "METRO BREÑA",
            "PLAZA VEA VENTANILLA"
        ]
    },
    "EDSON VEGA": {
        "asesores": [
            "ANDERSON MOISES CAPCHA MARCOS",
            "CANDACHO ANZUALDO CHRISTIAN EDUARDO",
            "DELZO HURTADO LUIS JUNIOR",
            "DIEGO RAMÓN VASQUEZ FIGUEROA ",
            "EDGAR IVAN VALENCIA SAAVEDRA",
            "GUTIERREZ HUANIN LUIGGI ERICK",
            "LUIS JERONIMO AGUILAR",
            "MEDINA ESCALANTE MANUEL ENRIQUE",
            "MEZA MEDINA LADY CANDY",
            "RODRIGUEZ IZASIGA PIERO GIANMARCO",
            "ROJAS REA JESUS ANTONI",
            "CIELO ESTEPHANY DONATO FERRO",
            "DAVID ANTONY SILVA AGUIRRE",
            "GIANCARLO ALEXANDER GARCÍA GARCÍA",
            "ASTRID AMIRA REYNALDO CANTORAL",
            "EDWIN JUNIOR LOPEZ HUAMAN",
            "ADRIANA JHAZMIN HUERTA GAONA",
            "MANUEL ALEJANDRO ÁLVAREZ MARTOS",
            "MILAGRITOS CARRERA LOPEZ "
        ],
        "modulos": [
            "MALL DEL SUR",
            "REAL PLAZA GUARDIA CIVIL",
            "METRO HACIENDA",
            "METRO PROCERES",
            "PLAZA VEA VILLA EL SALVADOR",
            "REAL PLAZA VILLA MARIA DEL TRIUNFO",
            "MALL AVENTURA SJL"
        ]
    },
    "IMALAY USCATEGUI": {
        "asesores": [
            "AGÜERO FON LUIS HUMBERTO",
            "AHUANARI TUÑOQUE JULIO CESAR",
            "ANTONELLA DAYANA ORTIZ DOMINGUEZ ",
            "CORAL SILVA WILTER",
            "CRISTIAN CAPARACHIN CAHUANA",
            "GABRIELA GALINDO VIZCARRA ",
            "JOHN JAIME CHUNQUI SILVA",
            "KARIN GEOVANA TAIPE CRUZ ",
            "MAYURI ALEGRÍA CHOQUE ",
            "ORDOÑEZ QUISPE WILDER",
            "PAJARES PEREZ CLEVER",
            "VILLAVICENCIO CHOLAN JUAN MARCO",
            "WALDIR HENRY FERNANDEZ MANDUJANO ",
            "YAHAIRA POLLET AGUIRRE MUÑOZ",
            "DAVID FERNANDO ROJAS MENDOZA",
            "LESLY SALOME CORDOVA CHIRINOS",
            "CINTHIA LUCAR GUERRERO",
            "LISBETH CHAVEZ  SANCHEZ",
            "CARLOS EMILIO  SERRANO MURAYARI",
            "JOHN PEDRO AVILA DE LA CRUZ"
        ],
        "modulos": [
            "OPEN ATOCONGO",
            "MALL AVENTURA SANTA ANITA 1",
            "REAL PLAZA PURUCHUCO",
            "MOLINA PLAZA",
            "MALL AVENTURA SANTA ANITA 2",
            "PLAZA VEA BOLICHERA",
            "WONG GARDENIAS"
        ]
    },
    "HECSAN GUANIQUE": {
        "asesores": [
            "CASTILLO CASTILLO CRISTOFER YANPIER",
            "CHAVEZ CUBAS LESLEY LUZFELINA",
            "CISNEROS GRADOS DIEGO ALONSO",
            "DIEGO VICTOR LIZARZABURU FARFAN",
            "FRINI VIVIANA VILLEGAS RONDOY ",
            "HINOSTROZA GARCIA DANIEL AUGUSTO",
            "JEFFREY ALEXANDER MARTINEZ VILCHEZ",
            "PRIETO MOREYRA RUDY NOEMI",
            "RAMIREZ NUREÑA LUIS HUGO",
            "RAQUEL DURAN ALALUNA",
            "REYES BANDES MARIA DE LOS ANGELES",
            "SEBASTIAN ALONSO ORELLANA ORTIZ ",
            "VIERA ZAPATA JOSE RODOLFO",
            "GONZALES ORELLANA CRISTH FIORELLA",
            "VANESSA GLENDA ROSAS TORRES",
            "RUBEN DARIO FLORES IMAN",
            "ROCIO DEL PILAR REAÑO SIQUIHUA",
            "JUAN CARLOS PALOMINO BOCANEGRA",
            "NYRLA BEATRIZ MALDONADO CARREÑO ",
            "ELIAS PERALES  ROJAS",
            "HAROLD STEWART FLORIAN TORRES",
            "ALEXIS AARÓN LINO PEÑA"
        ],
        "modulos": [
            "PLAZA VEA RISSO",
            "PLAZA LIMA SUR",
            "OPEN ANGAMOS",
            "PLAZA VEA EL CORTIJO",
            "WONG 2 DE MAYO",
            "WONG OVALO GUTIERREZ",
            "PLAZA VEA HIGUERETA",
            "REAL PLAZA PRIMAVERA"
        ]
    }
}

turnos = ["AM", "PM"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

st.title("📅 Planificador de Horarios Semanales")

with st.form("planificador_form"):
    fecha = st.date_input("Fecha de planificación", date.today())
    supervisor = st.selectbox("Supervisor", list(supervisores_data.keys()))

    asesores = supervisores_data[supervisor]["asesores"]
    modulos = supervisores_data[supervisor]["modulos"]

    planning = []
    for modulo in modulos:
        for turno in turnos:
            st.markdown(f"### {modulo} - {turno}")
            cols = st.columns(len(dias))
            fila = {}
            for i, dia in enumerate(dias):
                fila[dia] = cols[i].selectbox(
                    f"{dia} - {modulo}-{turno}", 
                    asesores, 
                    key=f"{modulo}_{turno}_{dia}"
                )
            planning.append({"Módulo": modulo, "Turno": turno, **fila})

    submitted = st.form_submit_button("Guardar planificación")
    if submitted:
        rows = []
        for fila in planning:
            modulo = fila["Módulo"]
            turno = fila["Turno"]
            for dia in dias:
                rows.append({
                    "Fecha": fecha,
                    "Supervisor": supervisor,
                    "Módulo": modulo,
                    "Turno": turno,
                    "Día": dia,
                    "Asesor": fila[dia]
                })
        df = pd.DataFrame(rows)
        df.to_excel("planificacion_resultado.xlsx", index=False)
        st.success("✅ Planificación guardada correctamente.")
        st.dataframe(df)
