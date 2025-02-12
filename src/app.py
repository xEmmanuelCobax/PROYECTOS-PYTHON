import re

def extract_info(text):
    patterns = {
        "Nombres completos": r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+\b",
        "Correos electrónicos": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "Fechas": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        "Horas": r"\b\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?\b",
        "Teléfonos": r"\b\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b",
        "Direcciones físicas": r"\d{1,4}\s[A-ZÁÉÍÓÚÑa-záéíóúñ]+(?:\s[A-ZÁÉÍÓÚÑa-záéíóúñ]+)+",
        "Enlaces web": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?",
        "Títulos de temas": r'"([^"]+)"',
        "Organización de la empresa": r"\b[a-zA-Z0-9.-]+\.(?:com|org|net|edu|gov)\b"
    }
    
    extracted_data = {}
    for key, pattern in patterns.items():
        extracted_data[key] = re.findall(pattern, text)
    
    return extracted_data

if __name__ == "__main__":
    sample_text = """
Estimados estudiantes,

Les recuerdo que la reunión para el curso de programación se llevará a cabo el próximo viernes 8 de febrero a las 10:00 AM. Estarán presentes varios miembros del equipo, entre ellos, Juan Pérez (juan.perez@example.com), quien es el encargado de la parte de backend. También estará María García (maria.garcia@dominio.com), responsable del frontend, así como Carlos López (carlos.lopez@correo.org), quien trabajará en la integración del sistema.

La dirección de la reunión es en la Calle Falsa 123, oficina 201. El evento será transmitido de forma remota y se podrá acceder a través del enlace http://reunion.curso-programacion.com.

Por favor, no olviden enviar sus informes antes del 7 de febrero a las 5:00 PM. Los informes deben enviarse a la siguiente dirección de correo electrónico: informes@empresa.com. Asegúrense de incluir todos los detalles relevantes. Además, está Silvia Martínez (silvia.martinez@correo.net), que revisará los informes para asegurarse de que estén completos.

Si tienen preguntas adicionales, pueden contactar a cualquiera de los siguientes miembros del equipo:

Ana Sánchez (ana.sanchez@empresa.org), encargada de la logística.
Pedro Gómez (pedro.gomez@dominio.com), responsable de la base de datos.
Luis Rodríguez (luis.rodriguez@correo.com), quien está a cargo de la documentación.
El teléfono de contacto para emergencias es el +34 612 345 678.

Si desean obtener más detalles, no duden en llamarnos al +34 678 910 112. Recuerden que la reunión también incluirá una breve sesión sobre la gestión de proyectos ágiles y cómo implementarlos en el entorno de programación.
    """
    
    extracted = extract_info(sample_text)
    for category, items in extracted.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
        print()