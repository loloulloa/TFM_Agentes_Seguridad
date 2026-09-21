- [2026-08-28]: Instalaci�n de la librer�a openai en el entorno virtual para la comunicaci�n con el modelo de lenguaje. 
- [2026-08-28]: Creaci�n del script procesar_reporte.py utilizando Structured Outputs con gpt-4o y Pydantic. 
- [2026-08-28]: Primera ejecuci�n exitosa del motor de extracci�n estructurada de vulnerabilidades con Pydantic y OpenAI. 
- [2026-08-28]: Descripci�n t�cnica de lo que acabamos de hacer y su justificaci�n. 
- [2026-08-28]: Primera ejecuci�n exitosa del motor de extracci�n estructurada de vulnerabilidades con Pydantic y OpenAI.Creaci�n del entorno virtual (venv) con Python y aislamiento de dependencias para garantizar la portabilidad y el control de versiones local (Git).Implementaci�n del archivo esquemas.py con modelos de Pydantic (Vulnerabilidad y ReporteSeguridadEstructurado) para asegurar un contrato de datos tipado y mitigar alucinaciones de los LLMs.Desarrollo del script procesar_reporte.py e integraci�n con OpenAI usando Structured Outputs (gpt-4o) para la extracci�n automatizada de reportes de ciberseguridad.Configuraci�n de variables de entorno y validaci�n exitosa del motor de procesamiento, logrando mapear texto no estructurado a objetos validados de Pydantic.
- [2026-09-01]: Solución de conectividad en n8n mediante Docker utilizando enrutamiento IPv4 estricto (127.0.0.1) y validación de acceso al panel de administración.
- [2026-09-04]: Habilitación exitosa de las APIs de Google Sheets, Gmail y Google Calendar en Google Cloud Console bajo el proyecto "My Project" para la integración de hiperautomatización en n8n.
- [2026-09-04]: Inicialización y configuración de la pantalla de consentimiento de OAuth en Google Cloud Console para la plataforma de identidad del TFM.
## [2026-09-04] - Configuración de Infraestructura OAuth y Validación de Ingestión en n8n

* **Objetivo:** Establecer la arquitectura de identidad segura entre el entorno local de n8n (vía Docker) y Google Cloud, e implementar un nodo disparador (*Trigger*) para la captura de eventos tabulares en Google Sheets.
* **Componentes y Accesos Configurados:**
  * Despliegue de contenedor n8n local con persistencia de datos en volumen Docker (`n8n_data`).
  * Creación y validación de credenciales **OAuth 2.0** en Google Cloud Console (*Client ID* y *Client Secret*).
  * Configuración de la URI de redireccionamiento autorizada (`http://localhost:5678/rest/oauth2-credential/callback`).
  * Definición de *scopes* de acceso para Gmail, Google Calendar, Google Sheets y habilitación formal de la API de Google Drive en la consola de Google Cloud.
  * Inclusión del correo personal como usuario de prueba para superar las restricciones de la pantalla de consentimiento de OAuth.
* **Prueba de Funcionamiento (Smoke Test):**
  * Vinculación exitosa de la cuenta (`Google Sheets Trigger account`) con estado *Account Connected*.
  * Creación de la hoja de prueba `Prueba_TFM` en Google Drive y estructuración de cabeceras tabulares (`ID`, `Mensaje`, `Estado`).
  * Ejecución exitosa del método *Fetch Test Event* obteniendo un objeto JSON estructurado de manera limpia en el panel de salida.
* **Próximos Pasos:** Conectar la salida de este nodo disparador con un modelo de lenguaje (LLM) o nodo de procesamiento inteligente para dar inicio al razonamiento autónomo del agente de hiperautomatización.
2026-09-11 Creación del archivo `docker-compose.yml` desde cero para el despliegue local de n8n con volúmenes persistentes. Contenedor levantado exitosamente y acceso verificado en http://localhost:5678 para la arquitectura del TFM.
## [2026-09-16] - Documentación del Business Case (As-Is / To-Be)
* Creación de la carpeta `Docs/` dentro del repositorio del proyecto.
* Redacción y estructuración del documento `business_case.md` con la definición del caso de negocio, análisis del proceso actual y la propuesta de transformación automatizada con agentes de IA.
## [2026/09/16] - Integración de Agente de Soporte con n8n y OpenAI
- **Hito alcanzado:** Configuración exitosa del flujo n8n conectando Google Sheets Trigger con el nodo *Basic LLM Chain* y *OpenAI Chat Model*.
- **Prompt Engineering:** Implementación del System Prompt bajo la metodología FOCUS para la clasificación y estructuración de tickets de soporte técnico.
- **Control de Versiones:** Commit realizado exitosamente en la rama `master`.
## [2026/09/16] - Cierre del Ciclo End-to-End y Persistencia en Google Sheets
- **Hito alcanzado:** Configuración e integración exitosa del nodo de actualización final (*Update row in sheet*), logrando un flujo síncrono bidireccional de extremo a extremo.
- **Detalle Técnico:** 
  - Mapeo dinámico del índice de fila original mediante la variable de contexto (`row_number`).
  - Persistencia del diagnóstico estructurado generado por el modelo de lenguaje (`gpt-4o-mini`) bajo la metodología FOCUS directamente en la celda de salida de Google Sheets.
- **Control de Versiones:** Registro formal de los cambios en el repositorio mediante commit en Git para mantener la trazabilidad de ingeniería.
## [Fase 4] - Implementación de Resiliencia, Blindaje y Control de Excepciones
* **Fecha:** 2026-09-16
* **Componentes Técnicos Implementados:**
  * **Nodo Global de Captura:** Configuración de `Error Trigger` en el lienzo de n8n para la escucha activa y asíncrona de excepciones en tiempo de ejecución.
  * **Canal de Persistencia Secundaria:** Creación y mapeo de la hoja de respaldo `Errores_TFM` en Google Sheets (con registro automatizado de fecha, ticket afectado y traza de error).
  * **Pasarela de Alerta e Intervención (*Human-in-the-loop*):** Integración de un nodo de Telegram para notificaciones instantáneas estructuradas al operador ante fallos críticos del flujo.
* **Validación y Pruebas:** Ejecución de pruebas de fallo controlado y validación de esquemas de datos dinámicos en los nodos de salida.
* **Estado:** Completado, probado con éxito (`ok: true`) y documentado en el repositorio.
## [2026-09-17] - Optimización de Arquitectura de Persistencia y Mapeo JSON en n8n

* **Objetivo del Hito:** Resolver el desbordamiento de celdas en Google Sheets y estructurar la persistencia modular de datos para las pruebas de calidad de la IA.
* **Decisiones Técnicas y Arquitectura To-Be:**
  * Transición de un volcado de texto plano en una sola celda a un esquema modular de columnas independientes (`Clasificación`, `Diagnóstico`, `Respuesta`).
  * Modificación del modo de mapeo en el nodo de Google Sheets a `Map Each Column Manually`.
  * Ajuste del criterio de búsqueda de filas utilizando la columna de identificación (`ID`) en lugar del índice físico `row_number`.
* **Implementación en n8n:**
  * Actualización del System Prompt del LLM bajo metodología FOCUS para exigir un objeto JSON estructurado.
  * Incorporación de la función de análisis `JSON.parse($json.text)` en las expresiones del nodo de actualización para extraer con precisión las claves `clasificacion`, `diagnostico` y `respuesta`.
* **Resultado:** Validación exitosa del caso de prueba de alta severidad con persistencia limpia y sin errores de tipo en la base de datos.
## [2026-09-17] - Validación de Escenario Operativo (Caso 2) en n8n

* **Objetivo del Hito:** Evaluar la resiliencia y precisión del modelo de IA ante un ticket de soporte de severidad media (solicitud de restablecimiento de contraseña corporativa).
* **Decisiones Técnicas y Ejecución:**
  * Ingesta de un nuevo caso operativo en la base de datos centralizada de Google Sheets.
  * Ejecución del flujo automatizado mediante el `Google Sheets Trigger` y procesamiento del prompt optimizado con salida JSON estricta.
  * Mapeo exitoso de las variables parseadas (`clasificacion`, `diagnostico`, `respuesta`) hacia las columnas correspondientes en la hoja de cálculo.
* **Resultado:** El agente clasificó correctamente el ticket como "Media", generó un diagnóstico técnico certero sobre la expiración de credenciales y estructuró una respuesta orientada al usuario final, validando la escalabilidad del modelo fuera de escenarios críticos.
## [2026-09-17] - Validación de Escenario Ambiguo (Caso 3) y Cierre de Pruebas Funcionales

* **Objetivo del Hito:** Evaluar la resiliencia y el comportamiento del agente de IA ante un mensaje de soporte impreciso o carente de parámetros técnicos (Caso Ambiguo).
* **Decisiones Técnicas y Ejecución:**
  * Ingesta del Caso 3 ("No puedo entrar a la plataforma, por favor reparen esto") en la base de datos de Google Sheets.
  * Procesamiento mediante el flujo automatizado en n8n y validación del System Prompt bajo metodología FOCUS.
  * Verificación de la clasificación de prioridad y la generación de un diagnóstico de solicitud de aclaración al usuario final.
* **Resultado:** El agente demostró una alta resiliencia semántica al procesar entradas ambiguas sin fallas en el pipeline de datos, cerrando con éxito la matriz de validación de calidad del sistema (Crítico, Operativo y Ambiguo).
## [2026-09-17] - Cierre de Matriz de Pruebas Funcionales y Definición de Arquitectura To-Be (Omnicanalidad y Web UI)

* **Objetivo del Hito:** Completar la validación funcional de los tres escenarios (Crítico, Operativo y Ambiguo) y definir la evolución de la arquitectura hacia un modelo omnicanal e interactivo para el TFM.
* **Resultados de las Pruebas de Calidad:**
  * **Caso 1 (Crítico):** Validación exitosa de errores masivos de autenticación con clasificación de severidad alta y diagnóstico técnico automatizado.
  * **Caso 2 (Operativo):** Procesamiento correcto de solicitudes estándar de soporte (expiración de credenciales) con categorización de prioridad media.
  * **Caso 3 (Ambiguo):** Comprobación de la resiliencia semántica del agente ante entradas imprecisas, aplicando criterios prudentes de clasificación y generando solicitudes de aclaración estructuradas.
* **Decisiones de Arquitectura To-Be y Escalabilidad:**
  * **Persistencia y Canal de Entrada:** Consolidación de Google Sheets como base de datos y bitácora centralizada, evaluando la automatización mediante sondeo (*Poll Times*) y Webhooks.
  * **Omnicanalidad:** Integración propuesta de nodos de notificación en tiempo real (Telegram) para alertas críticas y envío automatizado de correos electrónicos (Gmail) directamente al usuario final.
  * **Interfaz de Usuario (Frontend):** Conceptualización de una capa web local de captura de tickets para separar el rol del usuario final del panel de soporte interno.
* **Trazabilidad:** Validación y sincronización remota de todos los hitos en el repositorio de GitHub (`loloulloa/TFM_Agentes_Seguridad`).
## [2026-09-17] - Integración de Canal de Alertas en Tiempo Real (Telegram)

* **Objetivo del Hito:** Ampliar la arquitectura omnicanal del sistema incorporando notificaciones automáticas y proactivas para el equipo de soporte técnico (*Human-in-the-loop*).
* **Decisiones Técnicas y Arquitectura To-Be:**
  * Reordenamiento del pipeline de ejecución en n8n: tras la ingesta por el `Google Sheets Trigger`, el nodo `Basic LLM Chain` procesa y estructura el ticket mediante OpenAI.
  * Inserción del nodo de Telegram (`Send Message`) posterior al análisis de la IA para asegurar que las variables parseadas (`ID`, `clasificacion`, `diagnostico`, `respuesta`) estén disponibles de manera inmediata.
  * Mantenimiento de la persistencia centralizada en Google Sheets como base de datos histórica y bitácora interna.
* **Resultado:** Envío exitoso de alertas formateadas en Markdown con emojis y etiquetas claras directamente al chat del equipo técnico, validando la escalabilidad del modelo hacia comunicaciones omnicanal en tiempo real.
## [2026-09-17] - Validación del Canal de Telegram y Control de Ítems en n8n

* **Objetivo del Hito:** Probar la recepción de alertas en tiempo real en Telegram y analizar el comportamiento de procesamiento por lotes (*items*) del disparador de Google Sheets.
* **Decisiones Técnicas y Ejecución:**
  * Ejecución del flujo integral con el nodo de Telegram operativo.
  * Identificación del comportamiento de sondeo (*polling*) donde el trigger procesa los ítems existentes en la hoja de cálculo durante las pruebas manuales.
* **Resultado:** Confirmación exitosa de la conectividad con la API de Telegram y estructuración correcta de las alertas en el dispositivo del usuario.
## [2026-09-17] - Configuración del Nodo If para Filtrado de Alertas en n8n

* **Objetivo del Hito:** Establecer los parámetros de condición lógica en n8n (`value1`, operador `is equal to`, `value2`) para segmentar el flujo de notificaciones según la severidad del ticket evaluado por el LLM.
* **Decisiones Técnicas:**
  * Mapeo de la variable de clasificación mediante `JSON.parse($json.text).clasificacion`.
  * Enrutamiento condicional para separar el canal de alertas críticas en tiempo real (Telegram) del registro histórico silencioso en Google Sheets.
* **Resultado:** Optimización del flujo omnicanal aplicando criterios de filtrado de eventos orientados a reducir la fatiga de notificaciones en el personal técnico.
## [2026-09-17] - Enrutamiento del Nodo If en la Arquitectura de n8n

* **Objetivo del Hito:** Conectar las salidas condicionales (`true` y `false`) del nodo `If` para separar el flujo de notificaciones móviles del almacenamiento persistente.
* **Decisiones Técnicas:**
  * Ruta `true`: Conexión secuencial hacia el nodo de Telegram para disparo de alertas en tiempo real, finalizando en la actualización de Google Sheets.
  * Ruta `false`: Derivación directa al nodo de persistencia en Google Sheets, asegurando el registro histórico sin notificaciones intrusivas.
* **Resultado:** Consolidación de un flujo de trabajo condicional eficiente, cumpliendo con los estándares de automatización y gestión de eventos del TFM.
## [2026-09-17] - Éxito en la Ejecución Integral del Pipeline Omnicanal (OmniAgent Ops)

* **Objetivo del Hito:** Validar la ejecución completa de punta a punta del sistema de soporte hiperautomatizado en n8n, incluyendo la habilitación de la Gmail API y OAuth2.
* **Decisiones Técnicas y de Validación:**
  * Resolución de permisos y propagación de la API de Gmail en Google Cloud Console.
  * Ejecución exitosa del lote de 5 tickets de prueba con enrutamiento condicional y despacho verificado de correos electrónicos (`SENT`).
* **Resultado:** Infraestructura técnica de agentes totalmente funcional, marcando la transición hacia la redacción de la Memoria y el Business Case del TFM.
## [2026-09-17] - Desarrollo del Portal Web de Autoservicio y Webhook en n8n

* **Objetivo del Hito:** Diseñar e implementar la capa de entrada web (*Frontend Client-facing*) mediante un formulario HTML/JS conectado a un nodo Webhook en n8n, evolucionando la arquitectura hacia una omnicanalidad real.
* **Decisiones Técnicas y de Arquitectura:**
  * Sustitución del disparador estático de Google Sheets por un nodo `Webhook` asíncrono configurado con método `POST`.
  * Desarrollo de interfaz web minimalista para la captura descentralizada de incidentes (correo y descripción del problema).
  * Establecimiento de comunicación HTTP asíncrona hacia el pipeline de procesamiento cognitivo por LLM.
* **Resultado:** Despliegue de un punto de entrada web totalmente funcional, enriqueciendo el Business Case de la solución *To-Be* para la memoria del TFM.
## [2026-09-17] - Alineación de Prompts y Payload en el Nodo LLM

* **Objetivo del Hito:** Actualizar las expresiones de entrada y el contexto del System Prompt en el `Basic LLM Chain` para alinearlos con la nueva arquitectura de ingesta vía Webhook.
* **Decisiones Técnicas y Metodológicas:**
  * Refactorización de la variable de entrada del usuario hacia el objeto JSON `{{ $json.body.mensaje }}`.
  * Ajuste semántico en el System Prompt bajo la metodología FOCUS, adaptando la fuente de origen de los tickets al portal web de autoservicio.
* **Resultado:** Coherencia total entre la capa de presentación (Frontend) y el motor de procesamiento cognitivo (LLM).
## [2026-09-17] - Validación de Ejecución Integral y Análisis de Codificación UTF-8

* **Objetivo del Hito:** Confirmar el éxito de la ejecución de extremo a extremo del pipeline omnicanal y analizar las discrepancias de codificación de caracteres (Charset) en pruebas de consola.
* **Decisiones Técnicas y de Ingeniería:**
  * Verificación de la persistencia de datos en Google Sheets tras la transición al modelo de inserción *Append*.
  * Diagnóstico del carácter de reemplazo (``) derivado de la codificación ANSI en terminales Windows de PowerShell frente al estándar UTF-8 de n8n.
* **Resultado:** Pipeline técnico 100% validado y operativo, estableciendo los lineamientos de codificación para la capa de presentación web (*Frontend*).
## [2026-09-17] - Validación de Arquitectura Omnicanal y Depuración de Canal de Correo

* **Objetivo del Hito:** Consolidar el funcionamiento de la topología general del sistema `OmniAgent Ops`, validando la persistencia en base de datos y la bifurcación de alertas.
* **Decisiones Técnicas y de Ingeniería:**
  * Verificación del éxito operativo en el disparador Webhook, motor LLM, enrutador condicional y nodo de inserción *Append* en Google Sheets.
  * Análisis de los parámetros de salida del canal de notificación por correo electrónico.
* **Resultado:** Sistema de hiperautomatización prácticamente completado a nivel técnico.
## [2026-09-17] - Corrección Definitiva del Cuerpo de Mensaje en Gmail

* **Objetivo del Hito:** Resolver el problema de cuerpo de correo en blanco mediante el uso directo de la propiedad nativa `$json.text` del motor LLM en el nodo de Gmail.
* **Decisiones Técnicas:**
  * Simplificación del mapeo de salida del nodo `Basic LLM Chain` hacia el canal de notificación por correo electrónico.
  * Eliminación de dependencias de parsing estricto para garantizar la resiliencia en la entrega de mensajes.
* **Resultado:** Despacho exitoso de correos electrónicos con el contenido íntegro generado por el agente de soporte.
## [2026-09-17] - Refactorización de Mapeo Resiliente en Google Sheets Append

* **Objetivo del Hito:** Corregir las celdas en blanco en la base de datos de auditoría mediante expresiones de mapeo tolerantes a fallos (operadores lógicos condicionales).
* **Decisiones Técnicas:**
  * Implementación de expresiones con fallback de variables (`||`) en las columnas de clasificación, diagnóstico y respuesta del nodo Google Sheets.
* **Resultado:** Persistencia estructurada 100% sincronizada con las salidas del motor cognitivo, garantizando la integridad de los datos de auditoría.
## [2026-09-17] - Optimización del Parser JSON para Persistencia en Google Sheets

* **Objetivo del Hito:** Sanitizar las respuestas estructuradas del LLM eliminando bloques de Markdown (````json`) antes del análisis sintáctico destinado a las columnas de la hoja de cálculo.
* **Decisiones Técnicas:**
  * Implementación de funciones de limpieza mediante expresiones regulares (`replace`) previas al `JSON.parse` en el nodo de Google Sheets.
* **Resultado:** Sincronización perfecta entre los canales de salida (Gmail) y los registros de auditoría estructurados en la base de datos.
## [2026-09-17] - Validación de Ingesta Exitosa en Nodo Webhook

* **Objetivo del Hito:** Confirmar la correcta recepción y parsing de payloads JSON asíncronos en el nodo de entrada Webhook de n8n.
* **Decisiones Técnicas:**
  * Verificación de la estructura de datos entrantes (`body.correo` y `body.mensaje`) en el panel de output de n8n.
* **Resultado:** Capa de recepción de eventos validada y lista para alimentar el motor de procesamiento cognitivo (LLM).
## [2026-09-17] - Maquetación Avanzada del Portal Web y Sección Multimedia (Frontend To-Be)

* **Objetivo del Hito:** Actualizar la capa de presentación con un diseño corporativo moderno basado en modo oscuro, paleta de colores de alta legibilidad y un contenedor multimedia para demostraciones en video.
* **Decisiones Técnicas:**
  * Implementación de estructura de dos columnas responsiva mediante CSS Grid.
  * Inclusión de estilos interactivos para estados de carga, alertas de éxito/error y reproductor multimedia simulado/nativo.
* **Resultado:** Interfaz web de autoservicio totalmente estilizada y alineada con los requerimientos visuales avanzados de los casos de estudio de posgrado.
## [2026-09-17] - Verificación y Consolidación del Frontend Web (`index.html`)

* **Objetivo del Hito:** Confirmar la correcta persistencia del código HTML5/CSS3 en el archivo de la capa de presentación y validar su renderizado visual en el navegador.
* **Decisiones Técnicas:**
  * Estabilización del archivo base de la interfaz web con estilos corporativos en modo oscuro y variables CSS.
  * Verificación de la comunicación asíncrona hacia el Webhook de n8n.
* **Resultado:** Capa frontend operativa, integrada y visualmente lista para las demostraciones de arquitectura del TFM.
## [2026-09-17] - Validación Visual Definitiva del Dashboard Web (Frontend To-Be)

* **Objetivo del Hito:** Confirmar el renderizado correcto del panel de control web en modo oscuro y la integración funcional con el pipeline de n8n.
* **Decisiones Técnicas:**
  * Estabilización de la capa visual del cliente web con diseño responsivo y contenedor de demostración en video.
* **Resultado:** Interfaz gráfica validada visualmente, marcando la conclusión exitosa de la fase de implementación técnica operativa.
## [2026-09-17] - Diseño del Guion y Storyboard para el Video Demostrativo del TFM

* **Objetivo del Hito:** Estructurar los bloques técnicos y narrativos del video de defensa y demostración del sistema omnicanal.
* **Decisiones Técnicas:**
  * Definición de la secuencia audiovisual: Contexto de arquitectura, ingesta web, ejecución en n8n, despacho multicanal (Gmail/Sheets) y trazabilidad en Git.
* **Resultado:** Guion técnico alineado con los estándares de evaluación de posgrado para la presentación final.
## [2026-09-17] - Verificación de Conectividad Asíncrona Frontend-Webhook

* **Objetivo del Hito:** Diagnosticar y resolver el error de tiempo de espera o rechazo de conexión (`ERR_CONNECTION_REFUSED` / estado de escucha inactivo) entre el portal web y el orquestador n8n.
* **Decisiones Técnicas:**
  * Sincronización del estado de escucha activa de pruebas (`Listen for test event`) en el nodo Webhook previo al envío de payloads HTTP desde el cliente web.
* **Resultado:** Conectividad de red restablecida y validada de punta a punta.
## [2026-09-17] - Validación Definitiva del Flujo End-to-End con Interfaz Web

* **Objetivo del Hito:** Comprobar la correcta integración asíncrona entre el panel de control web (`index.html`) y el orquestador backend en n8n.
* **Decisiones Técnicas:**
  * Verificación de la recepción de payloads limpios mediante protocolo HTTP POST y cabeceras UTF-8.
  * Consolidación de la respuesta visual exitosa en el cliente y procesamiento omnicanal backend.
* **Resultado:** Hito de implementación técnica completado con éxito absoluto.
## [2026-09-17] - Definición de la Estrategia de Demostración y Defensa (Enfoque Híbrido)

* **Objetivo del Hito:** Determinar el formato de presentación para el TFM, conciliando la interactividad de la aplicación web con la seguridad de un respaldo audiovisual.
* **Decisiones Técnicas y Arquitectónicas:**
  * Adopción de un modelo híbrido: Uso del dashboard web interactivo como interfaz principal del sistema y un video demostrativo incrustado como mecanismo de resiliencia ante incidencias en vivo frente al tribunal.
* **Resultado:** Estrategia de defensa estructurada bajo criterios profesionales de ingeniería y mitigación de riesgos.
## [2026-09-17] - Integración del Reproductor de Video Nativo en el Dashboard Web

* **Objetivo del Hito:** Incorporar un elemento multimedia funcional (`<video>`) en la interfaz web de autoservicio para materializar la estrategia híbrida de demostración y defensa del TFM.
* **Decisiones Técnicas:**
  * Actualización del componente de visualización en `index.html` con controles de reproducción nativos HTML5 para alojar el archivo de respaldo `demo_tfm.mp4`.
* **Resultado:** Interfaz web completa, interactiva y dotada de un mecanismo de resiliencia audiovisual de nivel profesional.
## [2026-09-17] - Refactorización de Experiencia de Usuario y Guía de SLA en el Frontend

* **Objetivo del Hito:** Optimizar la interfaz web de autoservicio integrando una sección informativa orientada al usuario final con los niveles de SLA y el flujo de atención, además de renombrar las acciones comerciales del formulario.
* **Decisiones Técnicas:**
  * Inserción de un componente informativo visual con la matriz de tiempos de respuesta por criticidad.
  * Actualización de etiquetas de botones a terminología de negocio ("Crear Ticket de Soporte").
* **Resultado:** Interfaz web enriquecida con criterios de gestión de servicios (ITIL/SLA) de alto nivel académico.
## [2026-09-17] - Corrección Tipográfica de Flechas y Definición de Contenido Audiovisual

* **Objetivo del Hito:** Erradicar códigos LaTeX no renderizados (`$\rightarrow$`) en la guía de SLA del frontend y definir el storyboard técnico para el video de resguardo (`demo_tfm.mp4`).
* **Decisiones Técnicas:**
  * Reemplazo de sintaxis matemática por entidades HTML de flechas (`&rarr;`).
  * Especificación del guion en 3 fases (Ingesta web $\rightarrow$ Orquestación n8n $\rightarrow$ Despacho Gmail/Sheets) para el video del TFM.
* **Resultado:** Interfaz visual pulida y estrategia de contenido audiovisual perfectamente delimitada.
## [2026-09-17] - Evolución Arquitectónica: Panel de Control de Tickets con Estados y SLA Dinámicos

* **Objetivo del Hito:** Ampliar el alcance del TFM incorporando un sistema completo de gestión de incidencias (*Ticketing Dashboard*) con codificación de colores por criticidad, asignación de operadores y trazabilidad de cierre.
* **Decisiones Técnicas y de Negocio:**
  * Transformación del portal web de un simple formulario de ingesta a un centro de control operativo con soporte para ciclo de vida de tickets (Abierto/Crítico $\rightarrow$ En Progreso $\rightarrow$ Cerrado/Resuelto).
  * Consolidación del caso de negocio (*Business Case To-Be*) con enfoque en observabilidad y gobernanza de servicios de TI.
* **Resultado:** Propuesta de valor del TFM altamente enriquecida y alineada con estándares corporativos de gestión de servicios.
## [2026-09-17] - Configuración Paso a Paso del Nodo Code en n8n

* **Objetivo del Hito:** Integrar el bloque de código JavaScript para la asignación dinámica de operadores y metadatos de tickets en el flujo de n8n.
* **Decisiones Técnicas:**
  * Uso de nodo nativo Code en n8n para la transformación de payloads JSON.
  * Generación de identificadores de tickets y asignación de recursos humanos simulados.
* **Resultado:** Lógica backend configurada y lista para enrutar las notificaciones automáticas.
## [2026-09-17] - Validación Visual del Nodo Code y Estructuración de Ciclo de Vida en n8n

* **Objetivo del Hito:** Comprobar la correcta integración gráfica y sintáctica del nodo Code en JavaScript dentro del flujo asíncrono de n8n.
* **Decisiones Técnicas:**
  * Verificación de la topología del canvas: Webhook $\rightarrow$ Basic LLM Chain $\rightarrow$ Code (JavaScript) $\rightarrow$ Bifurcaciones de Alerta y Persistencia.
* **Resultado:** Topología de backend validada visualmente con éxito, integrando lógica de asignación de operadores.
## [2026-09-17] - Sincronización del Marco Rector y Reactivación del Ciclo de Desarrollo TFM

* **Objetivo del Hito:** Consolidar el marco de directrices del tutor experto y coordinar la implementación del sistema de despacho de correos automáticos por asignación de operadores.
* **Decisiones Técnicas:**
  * Reanudación de la topología backend en n8n enfocada en notificaciones proactivas hacia el cliente final.
* **Resultado:** Alineación metodológica confirmada y ruta crítica de desarrollo establecida.
## [2026-09-17] - Diagnóstico y Corrección de Entrada de Datos en el Nodo Gmail de n8n

* **Objetivo del Hito:** Resolver la incidencia de dirección de correo vacua (`Invalid email address`) derivada de la ejecución aislada del nodo Gmail sin payload de entrada.
* **Decisiones Técnicas:**
  * Validación del principio de flujo asíncrono E2E, asegurando la conexión topológica entre el nodo de transformación Code y el conector de salida Gmail.
* **Resultado:** Incidencia resuelta mediante la ejecución correcta del pipeline completo.
## [2026-09-17] - Corrección de Error de Sintaxis (SyntaxError) en Script del Nodo Code

* **Objetivo del Hito:** Subsanar el error de sintaxis en el objeto JavaScript provocado por saltos de línea imprevistos en la propiedad `diagnostico_ia`.
* **Decisiones Técnicas:**
  * Refactorización y limpieza del bloque de código del nodo Code en n8n para asegurar la correcta serialización del JSON.
* **Resultado:** Nodo de transformación restablecido y operativo sin errores de sintaxis.
## [2026-09-17] - Configuración y Validación de Persistencia de Auditoría en Google Sheets

* **Objetivo del Hito:** Conectar el flujo estructurado del nodo Code hacia el conector de Google Sheets para garantizar el registro permanente de metadatos de tickets.
* **Decisiones Técnicas:**
  * Mapeo de variables de ciclo de vida (`id_ticket`, `correo_cliente`, `criticidad`, `operador_nombre`, `estado`) hacia las columnas de la hoja de persistencia.
* **Resultado:** Arquitectura de backend lista para la validación E2E y posterior desarrollo de la tabla interactiva web.
## [2026-09-17] - Aclaración Arquitectónica sobre Nodos Trigger vs. Action en n8n (Google Sheets)

* **Objetivo del Hito:** Analizar el estado del nodo `Google Sheets Trigger (Deactivated)` en el lienzo, distinguiendo entre disparadores de entrada y nodos de acción de persistencia.
* **Decisiones Técnicas:**
  * Confirmación de que el flujo se rige por un modelo orientado a eventos de entrada vía Webhook, utilizando el nodo `Append row in sheet1` para la auditoría transaccional.
* **Resultado:** Topología validada y aclarada conceptualmente para el desarrollo del TFM.
## [2026-09-17] - Diagnóstico de Conectividad End-to-End y Manejo de Excepciones de Webhook

* **Objetivo del Hito:** Analizar y resolver la incidencia de conexión entre el frontend web y el motor asíncrono de n8n.
* **Decisiones Técnicas:**
  * Verificación del estado de escucha activa del nodo Webhook en n8n y validación de puertos expuestos en Docker.
* **Resultado:** Protocolo de solución de errores de red establecido para el entorno local de desarrollo.
## [2026-09-17] - Depuración de Mapeo de Datos en Google Sheets y Nodos Condicionales

* **Objetivo del Hito:** Diagnosticar la falta de despacho en canales secundarios (Telegram/Gmail) debido a desajustes en el mapeo de variables del payload proveniente del nodo Code.
* **Decisiones Técnicas:**
  * Reestructuración del enrutamiento de propiedades JSON hacia las celdas de persistencia y nodos condicionales de alerta.
* **Resultado:** Protocolo de corrección de flujo multicanal establecido.
## [2026-09-17] - Validación Exitosa del Despacho de Correo de Asignación y Estabilización del Pipeline E2E

* **Objetivo del Hito:** Verificar el correcto funcionamiento del nodo de Gmail para el envío proactivo de notificaciones al cliente final con metadatos dinámicos del tiquete.
* **Decisiones Técnicas:**
  * Corrección de la variable destinataria en el campo "To" del nodo de Gmail, pasando de `operador_nombre` a la propiedad validada `correo_cliente`.
  * Validación visual del estado de salida de la API de Gmail (`1: SENT`, `INBOX`) en el entorno de pruebas de n8n.
* **Resultado:** Capa de comunicación multicanal validada y operativa de extremo a extremo (E2E).
## [Fecha Actual] - Corrección de Enrutamiento Condicional y Alerta en Telegram
- **Hito alcanzado:** Resolución del conflicto de alcance de datos tras el nodo de inserción en Google Sheets y validación exitosa del envío de alertas críticas a Telegram.
- **Detalle técnico:** 
  - Se identificó que el nodo `Append row in sheet1` reemplazaba el payload de salida genérico `$json`, ocultando la variable de criticidad.
  - Se actualizó la expresión lógica del nodo condicional `If1` utilizando la referencia explícita `$('Code in JavaScript').item.json.criticidad` para evaluar correctamente el nivel "Alta".
  - Se verificó la ejecución completa de punta a punta desde el Webhook hasta el canal de Telegram (`Send a text message2`).
- **Próximos pasos:** Reintegración de la lógica dinámica del LLM para el paso de clasificación y diseño de rutas para criticidades medias/bajas.
## [2026-09-18] - Definición del Frontend de Soporte (HTML/JS Minimalista)
- **Hito alcanzado:** Especificación técnica del formulario web minimalista para la captura y envío de tiquetes hacia el Webhook de n8n.
- **Detalle técnico:** Se establece el uso de HTML5 nativo y Fetch API para realizar peticiones POST asíncronas en formato JSON sin dependencias externas de frameworks pesados.
- **Próximos pasos:** Crear el código fuente base del formulario HTML y realizar la prueba de integración con el endpoint del Webhook.
## [2026-09-21] - Consolidación del Módulo Frontend y Conectividad con n8n
- **Hito alcanzado:** Implementación, depuración y validación exitosa del formulario web de soporte (`index.html`) y su integración con el webhook de producción en n8n.
- **Detalle técnico:** 
  - Se diseñó e implementó un portal web minimalista basado en HTML5 y JavaScript asíncrono (`fetch`) para la captura de tiquetes de usuarios (`correo` y `mensaje`).
  - Se resolvió la integración de red entre el entorno local y el servidor n8n en Docker, mapeando correctamente el payload JSON hacia el nodo `Basic LLM Chain` mediante la expresión `$json.body.mensaje`.
  - Se auditó y confirmó mediante el panel de ejecuciones de n8n el procesamiento exitoso de extremo a extremo del flujo automatizado.
- **Próximos pasos:** Iniciar el diseño y estructuración de la lógica para criticidades menores (Medias y Bajas) en el nodo condicional `If1`.
## [2026-09-21] - Restauración del OmniAgent Ops Dashboard Corporativo
- **Hito alcanzado:** Reintegración formal del diseño visual avanzado en modo oscuro para la interfaz de usuario.
- **Detalle técnico:** Se aseguró la persistencia del layout corporativo adaptado para la presentación institucional del TFM.
- **Próximos pasos:** Configurar las rutas de criticidades Medias y Bajas en el nodo condicional de n8n.