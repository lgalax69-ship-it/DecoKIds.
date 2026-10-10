
import streamlit as st

st.set_page_config(
    page_title="DecoKids | Diseña y crea",
    page_icon="🌈",
    layout="wide"
)

# ---------- ESTILO VISUAL ----------
st.markdown("""
<style>
.stApp {
    background-color: #FFF9F1;
}
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #6546A6;
}
p, label {
    color: #554B64;
}
div.stButton > button {
    background: linear-gradient(90deg, #FF8FAB, #A78BFA);
    color: white;
    border: none;
    border-radius: 18px;
    padding: 0.65rem 1.5rem;
    font-weight: bold;
}
div.stButton > button:hover {
    background: #7654C8;
    color: white;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    border: 2px solid #F3E6FF;
    margin-bottom: 12px;
}
.banner {
    background: linear-gradient(120deg, #FFE0EC, #E8DEFF, #D9F6EE);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------- ENCABEZADO ----------
st.markdown("""
<div class="banner">
    <h1>🌈 DecoKids</h1>
    <h3>¡Imagina, diseña y transforma espacios!</h3>
    <p>Ideas creativas para escuelas infantiles llenas de alegría.</p>
</div>
""", unsafe_allow_html=True)

# ---------- MENÚ ----------
pagina = st.radio(
    "Explora DecoKids",
    ["🏠 Inicio", "🎨 Diseñar mi espacio", "💡 Inspiración"],
    horizontal=True
)

# Imágenes de referencia de Unsplash
imagenes = {
    "Aula infantil":
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1000&q=80",
    "Biblioteca":
        "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1000&q=80",
    "Patio de juegos":
        "https://images.unsplash.com/photo-1472162314594-eca3c3d90c95?auto=format&fit=crop&w=1000&q=80",
    "Sala creativa":
        "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1000&q=80"
}

# ---------- INICIO ----------
if pagina == "🏠 Inicio":
    st.subheader("✨ Un mundo de ideas para los pequeños")

    c1, c2 = st.columns(2)

    with c1:
        st.image(imagenes["Aula infantil"],
                 use_container_width=True)
        st.markdown("### 🏫 Aulas mágicas")
        st.write("Crea ambientes acogedores, alegres y educativos.")

    with c2:
        st.image(imagenes["Sala creativa"],
                 use_container_width=True)
        st.markdown("### 🖍️ Rincones creativos")
        st.write("Convierte cada rincón en un lugar para imaginar.")

    st.info(
        "💜 ¡Empieza a diseñar! Entra en "
        "'Diseñar mi espacio' para crear tu propuesta."
    )

# ---------- DISEÑADOR ----------
elif pagina == "🎨 Diseñar mi espacio":
    st.subheader("🎨 Diseña tu ambiente ideal")
    st.write("Personaliza tu espacio y descubre nuevas ideas.")

    izquierda, derecha = st.columns([1, 1.2])

    with izquierda:
        ambiente = st.selectbox(
            "¿Qué espacio quieres decorar?",
            list(imagenes.keys())
        )

        estilo = st.selectbox(
            "Elige una temática",
            [
                "🌈 Arcoíris",
                "🦁 Animales",
                "🌿 Naturaleza",
                "🚀 Espacio y planetas",
                "☁️ Colores pastel"
            ]
        )

        color = st.selectbox(
            "Color principal",
            ["Rosa", "Lila", "Verde menta",
             "Amarillo", "Celeste"]
        )

        presupuesto = st.slider(
            "Presupuesto (S/)",
            100, 3000, 500, step=100
        )

        materiales = st.multiselect(
            "¿Qué te gustaría incorporar?",
            [
                "Murales",
                "Vinilos decorativos",
                "Estanterías",
                "Alfombras",
                "Cojines",
                "Organizadores",
                "Luces decorativas"
            ],
            default=["Murales", "Organizadores"]
        )

        crear = st.button(
            "✨ Crear mi propuesta",
            use_container_width=True
        )

    with derecha:
        st.markdown("### 🖼️ Vista de inspiración")
        st.image(
            imagenes[ambiente],
            caption=f"Idea visual para: {ambiente}",
            use_container_width=True
        )
        st.caption(
            "Imagen de referencia. "
            "La decoración mostrada no cambia automáticamente."
        )

    if crear:
        st.divider()
        st.balloons()

        st.success("¡Tu propuesta decorativa está lista!")

        st.markdown(f"## 🏡 {ambiente}")
        st.markdown(f"**Temática:** {estilo}")
        st.markdown(f"**Color principal:** {color}")
        st.markdown(f"**Presupuesto disponible:** S/ {presupuesto}")

        st.markdown("### 🛍️ Elementos seleccionados")

        if materiales:
            for material in materiales:
                st.write(f"✅ {material}")
        else:
            st.write("Aún no has seleccionado materiales.")

        st.markdown("### 💡 Recomendaciones")

        recomendaciones = {
            "🌈 Arcoíris":
                "Combina colores alegres con murales y zonas de juego.",
            "🦁 Animales":
                "Incorpora ilustraciones de animales y rincones temáticos.",
            "🌿 Naturaleza":
                "Utiliza tonos verdes, flores ilustradas y materiales naturales.",
            "🚀 Espacio y planetas":
                "Crea un mural del universo con planetas y estrellas.",
            "☁️ Colores pastel":
                "Combina tonos suaves para lograr un ambiente acogedor."
        }

        st.write(recomendaciones[estilo])

        st.info(
            "Planifica las compras según tu presupuesto. "
            "Prioriza materiales no tóxicos y elementos bien fijados."
        )

        # Guardar la propuesta como archivo de texto
        resumen = f"""
PROPUESTA DE DECORACIÓN - DECOKIDS

Ambiente: {ambiente}
Temática: {estilo}
Color principal: {color}
Presupuesto: S/ {presupuesto}
Materiales: {', '.join(materiales)}

Recomendación:
{recomendaciones[estilo]}
"""
        st.download_button(
            "📥 Descargar mi propuesta",
            data=resumen,
            file_name="mi_propuesta_decokids.txt",
            mime="text/plain"
        )

# ---------- INSPIRACIÓN ----------
elif pagina == "💡 Inspiración":
    st.subheader("🌟 Galería de inspiración")
    st.write("Explora imágenes para encontrar tu próximo diseño.")

    nombres = list(imagenes.keys())

    for inicio in range(0, len(nombres), 2):
        columnas = st.columns(2)

        for columna, nombre in zip(
            columnas, nombres[inicio:inicio + 2]
        ):
            with columna:
                st.image(
                    imagenes[nombre],
                    use_container_width=True
                )
                st.markdown(f"### ✨ {nombre}")

                if st.button(
                    f"Diseñar este espacio",
                    key=f"boton_{nombre}"
                ):
                    st.session_state["ambiente_elegido"] = nombre
                    st.info(
                        "Ve a 'Diseñar mi espacio' "
                        "para personalizar tu propuesta."
                    )

st.divider()

st.markdown("""
<div style="text-align:center; padding:10px;">
    <h3>💖 DecoKids</h3>
    <p>Espacios bonitos, pequeños grandes sueños.</p>
</div>
""", unsafe_allow_html=True)
