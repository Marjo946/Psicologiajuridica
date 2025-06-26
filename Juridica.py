import streamlit as st

# Preguntas, opciones, respuesta correcta y retroalimentación
questions = [
    {
        "question": "¿Qué estudia principalmente la psicología jurídica?",
        "options": ["Las enfermedades mentales graves", "La conducta humana en contextos legales", "Los tratamientos psiquiátricos involuntarios"],
        "correct": 1,
        "feedback": "La psicología jurídica se ocupa del estudio de la conducta humana en el ámbito del derecho."
    },
    {
        "question": "¿Cuál es una función del psicólogo jurídico en el sistema penal?",
        "options": ["Administrar justicia", "Realizar peritajes psicológicos", "Defender al acusado"],
        "correct": 1,
        "feedback": "El psicólogo jurídico realiza peritajes para evaluar al acusado, víctima o testigo."
    },
    {
        "question": "¿Qué se evalúa en una pericial psicológica a una persona imputada?",
        "options": ["Su capacidad para memorizar hechos", "Su capacidad de culpabilidad", "Su imputabilidad o responsabilidad penal"],
        "correct": 2,
        "feedback": "Se evalúa si comprende sus actos y puede actuar conforme a ellos."
    },
    {
        "question": "¿Qué característica define a la psicología jurídica en comparación con otras ramas de la psicología?",
        "options": ["Su enfoque en la neurociencia", "Su carácter forense y aplicado al derecho", "Su base exclusivamente clínica"],
        "correct": 1,
        "feedback": "Se caracteriza por intervenir en procesos judiciales y legales."
    },
    {
        "question": "¿En qué tipo de juicio puede intervenir un psicólogo jurídico?",
        "options": ["Solo en juicios penales", "Solo en juicios civiles", "En juicios penales, civiles, laborales y familiares"],
        "correct": 2,
        "feedback": "Participa en diversos tipos de procesos judiciales."
    },
    {
        "question": "¿Cuál es un principio ético fundamental en la psicología jurídica?",
        "options": ["La imparcialidad", "La confidencialidad absoluta", "El trabajo en solitario"],
        "correct": 0,
        "feedback": "El psicólogo debe ser objetivo e imparcial ante la ley."
    },
    {
        "question": "¿Qué es el testimonio en el ámbito de la psicología jurídica?",
        "options": ["Una prueba de inteligencia", "La declaración que da una persona sobre hechos que presenció", "Una técnica de relajación utilizada en juicios"],
        "correct": 1,
        "feedback": "El testimonio es clave en los procesos judiciales y debe ser analizado cuidadosamente."
    },
    {
        "question": "¿Qué se busca con la mediación en conflictos legales?",
        "options": ["Determinar la culpabilidad", "Imponer una sanción", "Resolver conflictos mediante el diálogo y el acuerdo"],
        "correct": 2,
        "feedback": "La mediación busca acuerdos mediante el diálogo."
    },
    {
        "question": "¿Qué técnica puede usar un psicólogo jurídico para evaluar el daño psicológico en una víctima?",
        "options": ["La hipnosis", "Entrevistas clínicas y pruebas psicométricas", "Terapia grupal"],
        "correct": 1,
        "feedback": "Se usan entrevistas y pruebas para evaluar el impacto emocional."
    },
    {
        "question": "¿Qué población puede ser atendida por la psicología jurídica?",
        "options": ["Solo delincuentes", "Solo víctimas", "Víctimas, testigos, agresores y operadores del sistema legal"],
        "correct": 2,
        "feedback": "La psicología jurídica trabaja con todos los involucrados en procesos legales."
    }
]

# Inicializar estados
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

st.title("🧠 Cuestionario de Psicología Jurídica")

# Mostrar mensaje final
if st.session_state.current_q >= len(questions):
    st.success("🎉 ¡Felicidades! Has completado el cuestionario.")
    st.balloons()
else:
    q = questions[st.session_state.current_q]
    st.markdown(f"**Pregunta {st.session_state.current_q + 1}:** {q['question']}")

    # Mostrar opciones
    selected = st.radio("Selecciona una opción:", q['options'], key=st.session_state.current_q)

    # Botón para responder
    if st.button("Responder") and not st.session_state.answered:
        if q['options'].index(selected) == q['correct']:
            st.success("✅ ¡Correcto!")
        else:
            st.error("❌ Incorrecto.")
        st.info(q['feedback'])
        st.session_state.answered = True

    # Botón para continuar
    if st.session_state.answered:
        if st.button("Siguiente pregunta"):
            st.session_state.current_q += 1
            st.session_state.answered = False

