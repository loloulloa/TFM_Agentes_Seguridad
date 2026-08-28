from openai import OpenAI
from esquemas import ReporteSeguridadEstructurado

# Inicializamos el cliente de OpenAI (requiere tener tu variable de entorno OPENAI_API_KEY configurada)
client = OpenAI()

# Texto de ejemplo que simula un reporte de escaneo de vulnerabilidades
reporte_ejemplo = """
Informe de Seguridad - Escaneo Perimetral
Fecha: 2026-08-28
Herramienta: Nessus Enterprise
Total de hallazgos detectados: 2

1. Vulnerabilidad crítica encontrada en el servidor web principal.
- CVE ID: CVE-2023-44487
- Host afectado: 192.168.1.50
- Severidad: Crítica
- CVSS Score: 9.8
- Descripción: Fallo de denegación de servicio en HTTP/2.
- Recomendación: Actualizar el servidor web a la última versión parcheada de inmediato.

2. Vulnerabilidad en librería de desarrollo.
- CVE ID: CVE-2021-44228
- Host afectado: 192.168.1.85
- Severidad: Alta
- CVSS Score: 8.5
- Descripción: Inyección de código en Log4j.
- Recomendación: Reemplazar la librería Log4j por la versión segura.
"""

print("Enviando reporte de seguridad al modelo para extracción estructurada...")

# Usamos la funcionalidad de structured outputs con Pydantic
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Eres un analista de ciberseguridad experto en extraer datos precisos de reportes técnicos."},
        {"role": "user", "content": f"Extrae la información estructurada del siguiente reporte:\n{reporte_ejemplo}"}
    ],
    response_format=ReporteSeguridadEstructurado,
)

# Obtenemos el objeto validado por Pydantic
resultado_estructurado = completion.choices[0].message.parsed

# Mostramos el resultado limpio en consola
print("\n--- DATOS EXTRAÍDOS Y VALIDADOS CORRECTAMENTE ---")
print(f"Herramienta: {resultado_estructurado.herramienta_origen}")
print(f"Fecha: {resultado_estructurado.fecha_escaneo}")
print(f"Total de vulnerabilidades: {resultado_estructurado.total_vulnerabilidades}\n")

for i, vuln in enumerate(resultado_estructurado.hallazgos, 1):
    print(f"Hallazgo {i}:")
    print(f"  - CVE: {vuln.cve_id}")
    print(f"  - Servidor: {vuln.activo_afectado}")
    print(f"  - Severidad: {vuln.severidad} (CVSS: {vuln.cvss_score})")
    print(f"  - Recomendación: {vuln.recomendacion}\n")