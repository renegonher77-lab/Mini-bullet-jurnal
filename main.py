import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de página con estilo ejecutivo
st.set_page_config(page_title="BJ Ejecutivo 2026", layout="wide")
st.title("🦅 Centro de Mando: Música, Cobranza y Fitness")

# --- BARRA LATERAL: REGISTRO DE HÁBITOS ---
st.sidebar.header("Registro de Hoy")
fase_cap = st.sidebar.select_slider("Fase Capacitación", options=["Alfa", "Beta", "Gamma"])
entreno = st.sidebar.checkbox("Entrenamiento Pesas/Cardio")
proteina = st.sidebar.checkbox("Meta Proteica (Gramaje)")
sueno = st.sidebar.checkbox("Sueño Calidad (>7h)")
p_musica = st.sidebar.checkbox("Avance Creación/Producción")
p_ventas = st.sidebar.checkbox("Gestión de Envío/Venta")

# --- CÁLCULO DE FIGURA GEOMÉTRICA ---
def generar_radar():
    # [cite_start]Métrica de éxito basada en tus pilares [cite: 76, 114, 250]
    categories = ['Fitness', 'Nutrición', 'Creación', 'Producción', 'Ventas', 'Capacitación']
    valores_real = [
        5 if entreno else 1, 
        5 if proteina and sueno else 2, 
        4 if p_musica else 1, 
        3 if p_musica else 1, 
        5 if p_ventas else 1, 
        5 if fase_cap else 1
    ]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[5,5,5,5,5,5], theta=categories, fill='toself', name='Meta 100%'))
    fig.add_trace(go.Scatterpolar(r=valores_real, theta=categories, fill='toself', name='Realizado', fillcolor='rgba(255, 0, 0, 0.3)'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True)
    return fig

# --- CUERPO PRINCIPAL ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Gráfico de Desempeño Semanal")
    st.plotly_chart(generar_radar(), use_container_width=True)
    st.caption("Si el polígono es irregular, hay deuda en esa área.")

with col2:
    [cite_start]st.subheader("Pipeline Musical: Doble Check [cite: 139]")
    # Tabla interactiva para tus 100+ canciones
    data = {
        "Canción": ["Ejemplo: Lamento Triste", "Ejemplo: Deuda Incobrable"],
        "Letra/Idea [✓]": [True, True],
        "Sentencia Ejecutoria [✓][✓]": [False, True],
        "Fase Actual": ["C1 - Maqueta", "E - Lanzamiento"]
    }
    df = pd.DataFrame(data)
    st.data_editor(df, num_rows="dynamic")

st.divider()
st.write(f"**Fase de Capacitación Actual:** {fase_cap} - " + 
         ("Enfoque en Investigación" if fase_cap=="Alfa" else "Enfoque en Desarrollo" if fase_cap=="Beta" else "Enfoque en Ventas"))
