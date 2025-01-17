import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import base64
import warnings
warnings.simplefilter("ignore", category=FutureWarning)

#"""" codigo de particulas que se agregan en le background""""
particles_js = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    background-color: #191970;    
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }
  
</style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 300,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#fffc33"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#fffc33",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""
globe_js = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vanta Globe Animation</title>
    <style type="text/css">
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        overflow: hidden;
        height: 100%;
        margin: 0;
        background-color: #1817ed; /* Fondo azul */
      }
      #canvas-globe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="canvas-globe"></div>       

    <!-- Scripts de Three.js y Vanta.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanta/0.5.24/vanta.globe.min.js"></script>

    <script type="text/javascript">      
      document.addEventListener("DOMContentLoaded", function() {
        VANTA.GLOBE({
          el: "#canvas-globe", // El elemento donde se renderiza la animación
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          scale: 1.00,
          scaleMobile: 1.00,
          color: 0xd1ff3f, // Color verde amarillento
          backgroundColor: 0x1817ed // Fondo azul
        });
      });
    </script>
  </body>
</html>
"""
dots_js = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vanta Dots Animation</title>
    <style type="text/css">
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html, body {
        height: 100%;
        margin: 0;
        overflow: hidden;
      }
      #canvas-dots {
        position: absolute;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="canvas-dots"></div>       
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanta/0.5.24/vanta.dots.min.js"></script>
    
    <script type="text/javascript">      
      document.addEventListener("DOMContentLoaded", function() {
        VANTA.DOTS({
          el: "#canvas-dots", // Especificar el contenedor donde debe renderizarse
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          scale: 1.00,
          scaleMobile: 1.00,
          color: 0xd7ff20,
          color2: 0xcaff20,
          backgroundColor: 0x123be1
        });
      });
    </script>
  </body>
</html>
"""

# Configuración de página
st.set_page_config(page_title="Predicción-Préstamo-Inmob", page_icon="images/prestamo-bancario.png", layout="wide")  

#""" imagen de background"""
def add_local_background_image(image):
  with open(image, "rb") as image:
    encoded_string = base64.b64encode(image.read())
    st.markdown(
      f"""
      <style>
      .stApp{{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
      }}    
      </style>
      """,
      unsafe_allow_html=True
    )
add_local_background_image("images/fondo3.jpg")


#""" imagen de sidebar"""
def add_local_sidebar_image(image):
  with open(image, "rb") as image:
    encoded_string = base64.b64encode(image.read())
    st.markdown(
      f"""
      <style>
      .stSidebar{{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
      }}    
      </style>
      """,
      unsafe_allow_html=True
    )

add_local_sidebar_image("images/fondo1.jpg")

# ---- animación de inicio de pagina----
with st.container():
    #st.write("---")
    left, right = st.columns(2, gap='small', vertical_alignment="center")
    with left:
        components.html(globe_js, height=150,scrolling=False)
    with right:
       components.html(dots_js, height=150,scrolling=False) 
    #st.write("---")    


with st.container():
    st.write("---")
    left, right = st.columns(2, gap='small', vertical_alignment="center")
    with left:
        st.subheader("Predicción de Préstamos ")
        st.write("Elija qué tipo de negocio espera realizar, la ubicación y el estado en el que vive y luego verifique la probabilidad de obtener un préstamo")
    with right:
               #"""### image from local file"""
        file_ = open("images/arquitecto.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
          f'<img src="data:img/gif;base64,{data_url}" alt="imagen" width="120" height="120">',
          unsafe_allow_html=True, 
        )
st.markdown("---")



# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_excel('datos/dato_db.xlsx', sheet_name='Sheet1')

df = cargar_datos()

#"""### despliegue de sidebar"""  
with st.sidebar:     
    col1, col2 = st.columns(2, vertical_alignment="center", border=True)
    with col1:        
        components.html(particles_js, height=80,scrolling=False) 
    with col2:
        st.subheader("Predicción de Préstamos Inmobilidarios")       
    st.write("---")


# Filtros de la barra lateral
st.sidebar.header("Filtrar datos :")
state = st.sidebar.selectbox("Seleccione Ciudad:", options=df["Ciudad"].unique(), help="Dónde se asigna el negocio")   
region = st.sidebar.selectbox("Seleccione Región:", options=df["Región"].unique(), help="Segmento dentro de una región")  
location = st.sidebar.radio("Seleccione Ubicación:", options=df["Ubicación"].unique(), help="Urbana/Rural")
construction = st.sidebar.radio("Seleccione Construcción:", options=df["Construcción"].unique(), help="Bienes/Servicios")

# Filtrar datos con las selecciones del usuario
df_selection = df.query("Ciudad == @state & Ubicación == @location & Región == @region & Construcción == @construction")

# Verificar si el filtrado dejó suficientes datos
if df_selection.empty:
    st.warning("No se encontraron datos con los filtros seleccionados. Intente con diferentes combinaciones.")
else:
    # Gráfico de barras - Inversión por tipo de negocio
    def plot_investment_by_business_type(df_selection):
        investment_by_business_type = df_selection.groupby(by=["Tipo/negocio"]).count()[["Ciudad"]].sort_values(by="Ciudad")
        fig_investment = px.bar(
            investment_by_business_type,
            x="Ciudad",
            y=investment_by_business_type.index,
            orientation="h",
            title="Inversión por Tipo de Negocio",
            color_discrete_sequence=["#0083B8"]*len(investment_by_business_type),
            template="plotly_white"
        )
        fig_investment.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=dict(showgrid=False))
        return fig_investment

    fig_investment = plot_investment_by_business_type(df_selection)

    # Modelado de árbol de decisión y regresión logística
    def entrenar_modelos(df_selection):
        # Preprocesamiento de datos para el modelo
        df_selection['Ciudad'].replace(['Guaymallen','Godoy Cruz','Mendoza','Tunuyan','Maipu','San Rafael','Lujan de Cuyo'], [1,2,3,4,5,6,7], inplace=True)
        df_selection['Ubicación'].replace(['Urbana','Rural'], [1,2], inplace=True)
        df_selection['Región'].replace(['Este','MedioOeste','NorteEste','Central'], [1,2,3,4], inplace=True)
        df_selection['Construcción'].replace(['Material','Resistente-fuego','Mamposteria','Const-Metalica'], [1,2,3,4], inplace=True)

        # Variables predictoras y objetivo
        X = df_selection.drop(columns=['Tipo/negocio'])
        y = df_selection['Tipo/negocio']
        
        # Verificar si hay más de una clase en los datos
        if y.nunique() < 2:
            st.warning(f"Solo se encuentra una clase en los datos: {y.unique()}. No se puede entrenar el modelo de regresión logística ni el árbol de decisión.")
            return None, None, None, None, None, None, None, None
        
        # Verificar si hay suficientes datos para dividir
        if len(X) > 1:  # Asegúrate de que haya al menos 2 muestras
            # División de los datos en entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
            
            # Entrenamiento del modelo de árbol de decisión
            tree_model = DecisionTreeClassifier()
            tree_model.fit(X_train, y_train)
            tree_predictions = tree_model.predict(X_test)

            # Entrenamiento del modelo de regresión logística
            log_model = LogisticRegression(max_iter=200)
            try:
                log_model.fit(X_train, y_train)
                log_predictions = log_model.predict(X_test)
                log_accuracy = accuracy_score(y_test, log_predictions)
            except ValueError:
                log_accuracy = None  # Si ocurre el error, se asigna un valor nulo para la regresión logística
                log_predictions = None
            
            # Evaluación de modelos
            tree_accuracy = accuracy_score(y_test, tree_predictions)
            
            return tree_model, log_model, tree_accuracy, log_accuracy, X_test, y_test, tree_predictions, log_predictions
        else:
            st.warning("No hay suficientes datos para entrenar el modelo. Intente con combinaciones diferentes.")
            return None, None, None, None, None, None, None, None

    # Entrenar los modelos y mostrar los resultados
    tree_model, log_model, tree_accuracy, log_accuracy, X_test, y_test, tree_predictions, log_predictions = entrenar_modelos(df_selection)

    if tree_model is not None:
        # Mostrar datos y precisión
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(df_selection["Tipo/negocio"].unique(), use_container_width=True)

        with col2:
            st.write("Probabilidad de préstamo - Árbol de Decisión:", round(tree_accuracy, 2))
            if log_accuracy is not None:
                st.write("Probabilidad de préstamo - Regresión Logística:", round(log_accuracy, 2))
            st.subheader(f"{round(tree_accuracy * 100, 1)} % (Árbol de Decisión) / {round(log_accuracy * 100, 1) if log_accuracy is not None else 0} % (Regresión Logística)")
            st.markdown("""---""")

        # Realizar una predicción para un nuevo usuario con ambos modelos
        nueva_prediccion_tree = tree_model.predict([[df_selection["Ciudad"].unique()[0], 
                                                     df_selection["Ubicación"].unique()[0], 
                                                     df_selection["Región"].unique()[0], 
                                                     0,  # Se asume un valor por defecto para la inversión
                                                     df_selection["Construcción"].unique()[0]]])
        
        if log_model is not None and log_predictions is not None:
            nueva_prediccion_log = log_model.predict([[df_selection["Ciudad"].unique()[0], 
                                                       df_selection["Ubicación"].unique()[0], 
                                                       df_selection["Región"].unique()[0], 
                                                       0,  # Se asume un valor por defecto para la inversión
                                                       df_selection["Construcción"].unique()[0]]])

            st.write("Facilidad recomendada - Regresión Logística:")
            st.info(f"{', '.join(nueva_prediccion_log)}")

        st.write("Facilidad recomendada - Árbol de Decisión:")
        st.info(f"{', '.join(nueva_prediccion_tree)}")

        # Graficar inversión por tipo de negocio
        st.plotly_chart(fig_investment, use_container_width=True)

        # Gráfico de distribución de clases (Tipo/negocio)
        st.subheader("Distribución de Clases en Tipo de Negocio")
        fig_class_dist = px.histogram(df_selection, x="Tipo/negocio", title="Distribución de Clases en Tipo de Negocio")
        st.plotly_chart(fig_class_dist, use_container_width=True)

            
        # Box Plot - Distribución de Inversión por Tipo de Negocio
        st.subheader("Distribución de Inversión por Tipo de Negocio")
        fig_box = px.box(df_selection, x="Tipo/negocio", y="Inversión", title="Distribución de Inversión por Tipo de Negocio")
        st.plotly_chart(fig_box, use_container_width=True)

        # Gráfico de dispersión - Inversión vs Ciudad
        st.subheader("Distribución de Inversión por Ciudad")
        fig_scatter = px.scatter(df_selection, x="Inversión", y="Ciudad", color="Tipo/negocio", title="Distribución de Inversión por Ciudad")
        st.plotly_chart(fig_scatter, use_container_width=True)
       
   
        # Gráfico de matriz de confusión - Árbol de Decisión
        st.subheader("Matriz de Confusión - Árbol de Decisión")
        cm_tree = confusion_matrix(y_test, tree_predictions)
        fig_cm_tree = plt.figure(figsize=(8, 6))
        sns.heatmap(cm_tree, annot=True, fmt="d", cmap="Blues", xticklabels=df_selection["Tipo/negocio"].unique(), yticklabels=df_selection["Tipo/negocio"].unique())
        st.pyplot(fig_cm_tree)

        # Gráfico de matriz de confusión - Regresión Logística (si se entrenó)
        if log_model is not None and log_predictions is not None:
            st.subheader("Matriz de Confusión - Regresión Logística")
            cm_log = confusion_matrix(y_test, log_predictions)
            fig_cm_log = plt.figure(figsize=(8, 6))
            sns.heatmap(cm_log, annot=True, fmt="d", cmap="Blues", xticklabels=df_selection["Tipo/negocio"].unique(), yticklabels=df_selection["Tipo/negocio"].unique())
            st.pyplot(fig_cm_log)

# Ocultar elementos de la interfaz de Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --------------- footer -----------------------------
st.write("---")
with st.container():
  #st.write("---")
  st.write("&copy; - derechos reservados -  2024 -  Walter Gómez - FullStack Developer - Data Science - Business Intelligence")
  #st.write("##")
  left, right = st.columns(2, gap='small', vertical_alignment="bottom")
  with left:
    #st.write('##')
    st.link_button("Mi LinkedIn", "https://www.linkedin.com/in/walter-gomez-fullstack-developer-datascience-businessintelligence-finanzas-python/")
  with right: 
     #st.write('##') 
    st.link_button("Mi Porfolio", "https://walter-portfolio-animado.netlify.app/")
