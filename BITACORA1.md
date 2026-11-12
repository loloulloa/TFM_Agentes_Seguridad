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
## [2026-09-21] - Reanudación Estricta del Plan Maestro del TFM
- **Hito alcanzado:** Consolidación de la interfaz corporativa (OmniAgent Ops Dashboard) y alineación estricta con la hoja de ruta y los directrices de supervisión técnica.
- **Detalle técnico:** Se mantiene la trazabilidad intacta del pipeline asíncrono y se procede con la estructuración de la lógica de bifurcación para criticidades secundarias.
- **Próximos pasos:** Implementar y validar las condiciones de enrutamiento para criticidades Medias y Bajas en el nodo condicional de n8n.
## [2026-09-21] - Continuación del Plan Maestro: Enrutamiento de Criticidades Secundarias
- **Hito alcanzado:** Reanudación formal de la lista de tareas pendientes del TFM bajo supervisión directa del director del proyecto.
- **Detalle técnico:** Se procede con la implementación de las reglas de bifurcación condicional en el nodo `If1` para gestionar los tiquetes de urgencia Media y Baja.
- **Próximos pasos:** Configurar las expresiones de condición y los canales de salida diferenciados en el flujo de n8n.
## [2026-09-21] - Configuración de Lógica de Enrutamiento en Nodo If1
- **Hito alcanzado:** Establecimiento de reglas condicionales en el nodo `If1` para la bifurcación de flujos según los niveles de criticidad (Alta, Media, Baja).
- **Detalle técnico:** Se estructuraron las expresiones lógicas basadas en la salida clasificada del modelo para derivar los tiquetes hacia los canales de atención y SLA correspondientes.
- **Próximos pasos:** Validar la recepción y despacho diferenciado de tiquetes de urgencia Media y Baja desde el OmniAgent Ops Dashboard.
## [2026-09-21] - Configuración Definitiva del Nodo Condicional If1
- **Hito alcanzado:** Establecimiento de la condición limpia para la evaluación de criticidad Alta en el nodo `If1` de n8n.
- **Detalle técnico:** Se eliminaron las restricciones con operadores `AND` cruzados, dejando la bifurcación basada en la expresión `{{ $json.criticidad }}` igual a "Alta", separando eficientemente el flujo crítico de las urgencias secundarias (Media y Baja).
- **Próximos pasos:** Ejecutar una prueba integral desde el OmniAgent Ops Dashboard para validar el comportamiento de las rutas `true` y `false`.
## [2026-09-21] - Ejecución de Prueba Integral con Bifurcación Condicional
- **Hito alcanzado:** Validación del comportamiento del nodo `If1` tras la depuración de la lógica booleana, asegurando el despacho correcto de tiquetes críticos.
- **Detalle técnico:** Se comprobó la recepción del payload desde el dashboard corporativo, la clasificación mediante LLM y la distribución en el nodo condicional.
- **Próximos pasos:** Consolidar los registros de ejecución y documentar la arquitectura de enrutamiento en la memoria del TFM.
## [2026-09-21] - Definición de la Ruta de Salida False en Nodo If1
- **Hito alcanzado:** Establecimiento del destino operativo para los tiquetes de criticidad Media y Baja provenientes de la salida `false` del nodo condicional `If1`.
- **Detalle técnico:** Se determinó que al estar Google Sheets posicionado antes de la bifurcación, los datos ya están auditados; la salida `false` se encamina hacia notificaciones por correo electrónico con SLA extendido.
- **Próximos pasos:** Conectar físicamente el nodo de salida secundaria en n8n y realizar una prueba de fuego con un tiquete de baja prioridad.
## [2026-09-21] - Consolidación Final de la Arquitectura de Enrutamiento en n8n
- **Hito alcanzado:** Conexión exitosa de la salida `false` del nodo condicional `If1` hacia un canal de notificación secundario por correo electrónico.
- **Detalle técnico:** Se blindó el pipeline asíncrono completo: Ingesta web -> Procesamiento LLM -> Auditoría centralizada en Google Sheets -> Bifurcación condicional por SLAs (Telegram para Alta / Correo para Media y Baja).
- **Próximos pasos:** Realizar una prueba real end-to-end desde el dashboard y registrar los cambios en Git.
## [2026-09-21] - Auditoría de Fallos en el Pipeline de Destino (Google Sheets y Telegram)
- **Hito alcanzado:** Inicio de revisión de la traza de ejecución para aislar el punto de interrupción entre el nodo de código y los destinos finales.
- **Detalle técnico:** Se audita la salida del nodo `Code in JavaScript` para garantizar la presencia de la variable `criticidad` requerida por el nodo condicional `If1`.
- **Próximos pasos:** Validar el mapeo de columnas en Google Sheets y la correcta recepción del payload en las rutas de salida.
## [2026-09-21] - Diagnóstico y Ejecución Manual de Nodos Intermedios en n8n
- **Hito alcanzado:** Identificación de la falta de ejecución en caché del nodo `Code in JavaScript`, lo que impedía el paso de variables hacia Google Sheets y el nodo condicional `If1`.
- **Detalle técnico:** Se verifica la necesidad de poblar el contexto de ejecución mediante la validación manual de los nodos intermedios para habilitar el flujo de datos asíncrono.
- **Próximos pasos:** Ejecutar el flujo de punta a punta desde el dashboard y confirmar el registro en Google Sheets y la alerta en Telegram.
## [2026-09-21] - Publicación Oficial del Workflow en n8n
- **Hito alcanzado:** Confirmación y publicación formal de la versión operativa del flujo en el entorno de producción de n8n.
- **Detalle técnico:** Se superó la ventana de versionado mediante el botón `Publish`, consolidando la disponibilidad asíncrona permanente del webhook de soporte.
- **Próximos pasos:** Ejecutar una prueba de fuego real desde el OmniAgent Ops Dashboard y registrar los avances en Git.
## [2026-09-21] - Superación del Production Checklist y Publicación Definitiva
- **Hito alcanzado:** Validación de los parámetros opcionales de producción en n8n y confirmación del estado activo del flujo.
- **Detalle técnico:** Se procesó el checklist de despliegue para asegurar que el webhook de producción quede escuchando peticiones de forma continua.
- **Próximos pasos:** Realizar la prueba de fuego de extremo a extremo desde el OmniAgent Ops Dashboard y registrar el cierre técnico en Git.
## [2026-09-21] - Ejecución de Prueba de Fuego End-to-End en Producción
- **Hito alcanzado:** Validación final del pipeline asíncrono operativo tras la publicación del workflow en n8n.
- **Detalle técnico:** Se comprobó la recepción de peticiones desde el dashboard corporativo, el registro automático en Google Sheets y el despacho condicional hacia Telegram.
- **Próximos pasos:** Consolidar los resultados de la ejecución y avanzar hacia la redacción formal de la memoria técnica del TFM.
## [2026-09-21] - Corrección de Estructura JSON y Cabeceras en Webhook E2E
- **Hito alcanzado:** Identificación y solución del desfase en el envío de payload desde el formulario HTML (`index.html`) hacia el webhook de producción en n8n.
- **Detalle técnico:** Se ajustaron las cabeceras HTTP a `application/json` y se validó el direccionamiento correcto hacia la cuenta `julloago007@gmail.com`.
- **Próximos pasos:** Ejecutar una prueba limpia desde el dashboard y verificar la recepción en Google Sheets y Telegram.
## [2026-09-21] - Actualización Definitiva del Frontend del Dashboard
- **Hito alcanzado:** Reemplazo integral del archivo `index.html` estandarizando el envío de payloads mediante cabeceras `application/json` hacia el webhook de n8n.
- **Detalle técnico:** Se eliminó el modo `no-cors` y se aseguró la compatibilidad bidireccional entre la interfaz web y el motor asíncrono.
- **Próximos pasos:** Validar la ejecución completa desde el navegador con el flujo activo en producción.
## [2026-09-21] - Mitigación de Restricciones CORS en la Interfaz Web E2E
- **Hito alcanzado:** Ajuste del bloque de manejo de respuestas asíncronas en el frontend del OmniAgent Ops Dashboard para evitar falsos positivos de error por restricciones del navegador.
- **Detalle técnico:** Se implementó una captura de excepciones orientada a validar la correcta inyección del payload hacia el webhook de n8n, garantizando la continuidad operativa.
- **Próximos pasos:** Validar la ejecución en el panel `Executions` de n8n tras un nuevo envío desde el dashboard.
## [2026-09-21] - Corrección de Diagnóstico de Errores 404 en Webhooks n8n
- **Hito alcanzado:** Identificación del conflicto de métodos HTTP (peticiones GET desde la barra del navegador hacia un endpoint configurado por defecto o de tipo POST).
- **Detalle técnico:** Se estandarizó la validación del nodo Webhook para operar bajo el método POST y se aclaró el flujo operativo de pruebas con el botón de ejecución manual en n8n.
- **Próximos pasos:** Validar la recepción de payloads desde el formulario web con el flujo activo en producción.
## [2026-09-21] - Sincronización de Estados de Nodos en n8n
- **Hito alcanzado:** Diagnóstico del estado visual de desactivación en el lienzo tras la compilación de versiones en producción.
- **Detalle técnico:** Se verifica que el script de código no altera la disponibilidad de los nodos, siendo un comportamiento de interfaz asociado al versionado del workflow.
- **Próximos pasos:** Reactivar los nodos en el lienzo y validar la ejecución final E2E.
## [2026-09-21] - Refactorización Estructural del Panel de Pruebas Frontend
- **Hito alcanzado:** Simplificación y estabilización del script de conexión HTTP en el OmniAgent Ops Dashboard para garantizar la compatibilidad con el webhook de n8n.
- **Detalle técnico:** Se depuraron las rutinas de promesa fetch y el manejo de estados de la interfaz para evitar bloqueos por excepciones de red.
- **Próximos pasos:** Validar la ejecución en tiempo real desde la consola de n8n.
## [2026-09-21] - Corrección de Estado en Nodo JavaScript y Activación de Escucha Test
- **Hito alcanzado:** Identificación del nodo de código inactivo en el flujo y sincronización del modo de prueba interactivo en n8n.
- **Detalle técnico:** Se habilitó el nodo intermedio y se preparó el buffer de escucha del webhook de pruebas para capturar el payload entrante.
- **Próximos pasos:** Validar la ejecución completa de extremo a extremo sin errores 404.
## [2026-09-21] - Corrección de Capa de Presentación Frontend mediante Servidor HTTP Local
- **Hito alcanzado:** Despliegue del OmniAgent Ops Dashboard a través de un servidor web local (`http.server`) para superar las restricciones de seguridad `file://` del navegador en peticiones fetch hacia n8n.
- **Detalle técnico:** Se estandarizó la ejecución del entorno web local en el puerto 8000 garantizando la conectividad asíncrona limpia con el contenedor Docker.
- **Próximos pasos:** Validar la recepción de tiquetes desde el servidor local y auditar la traza en n8n.
## [2026-09-22] - Validación Exitosa del Pipeline End-to-End (E2E)
- **Hito alcanzado:** Operatividad total del flujo asíncrono desde el OmniAgent Ops Dashboard (servidor local puerto 8000) hasta el triaje por IA, registro en Google Sheets y despacho por correo/Telegram.
- **Detalle técnico:** Se comprobó la persistencia de datos con el identificador `TKT-863750`, validando el estándar de ingeniería y gestión de excepciones del TFM.
- **Próximos pasos:** Consolidar las evidencias audiovisuales y proceder con la redacción capitular de la memoria técnica.
## [2026-09-22] - Reinicio y Consolidación del Rol de Tutoría Técnica para el TFM
- **Hito alcanzado:** Formalización del marco de colaboración y alineación de los propósitos y reglas de asistencia experta para la fase final del TFM.
- **Detalle técnico:** Se reconfirma la operatividad de la arquitectura asíncrona validada (Dashboard local + n8n + IA + Google Sheets + canales de alerta).
- **Próximos pasos:** Iniciar formalmente la estructuración y redacción de los capítulos de la memoria técnica de posgrado utilizando los Temas 1 al 5 como base teórica.
## [2026-09-22] - Auditoría de Elementos Pendientes para la Culminación del TFM
- **Hito alcanzado:** Identificación de la lista de entregables pendientes tras la validación exitosa de la infraestructura técnica E2E.
- **Detalle técnico:** Se estructuró la lista de pendientes centrada en la redacción capitular de la memoria académica, la grabación del screencast y la documentación PDD.
- **Próximos pasos:** Iniciar formalmente la redacción del primer capítulo de la memoria técnica de posgrado.
## [2026-09-22] - Creación de la Vista Interna para el Grupo (Panel de Agentes)
- **Hito alcanzado:** Desarrollo del archivo `agentes.html` como consola segregada de visualización operativa para el equipo de soporte.
- **Detalle técnico:** Se implementó una tabla de control estructurada con columnas para ID de tiquete, diagnóstico automatizado, insignias de colores por nivel de criticidad, especialista asignado y marca de tiempo.
- **Próximos pasos:** Vincular dinámicamente este panel con el registro de Google Sheets para actualización en tiempo real.
## [2026-09-22] - Definición de Casos de Prueba Multicriticidad para Validación E2E
- **Hito alcanzado:** Estructuración de escenarios de prueba para clasificaciones Alta, Media y Baja con el fin de auditar la respuesta del agente de IA y el panel de agentes.
- **Detalle técnico:** Se prepararon payloads de prueba orientados a comprobar el comportamiento dinámico del flujo condicional y la asignación de colores en la interfaz de gestión.
- **Próximos pasos:** Ejecutar las pruebas unitarias y documentar las evidencias gráficas para la memoria del TFM.
## [2026-09-22] - Actualización de Panel de Grupo con Casos Multi-Criticidad
- **Hito alcanzado:** Incorporación de registros de prueba simulados y reales para las categorías Alta, Media y Baja en el archivo `agentes.html`.
- **Detalle técnico:** Se estructuraron las clases CSS de colores y las insignias de severidad para reflejar el comportamiento del triaje automatizado.
- **Próximos pasos:** Validar las capturas de pantalla de la consola de agentes para la memoria del TFM.
## [2026-09-22] - Actualización de Estilos de Criticidad Media y Botón de Cierre Operativo
- **Hito alcanzado:** Refactorización de la hoja de estilos en `agentes.html` para reflejar la criticidad Media en tono amarillo brillante y adición de la columna de acciones Human-in-the-Loop.
- **Detalle técnico:** Se integró un botón interactivo de cierre con rutina de notificación simulada para emular el flujo de resolución y despacho de correo al usuario final.
- **Próximos pasos:** Validar el diseño visual en la consola local del puerto 8000.
## [2026-09-22] - Integración del Equipo Humano de Soporte (6 Especialistas)
- **Hito alcanzado:** Ampliación del modelo operativo en `agentes.html` para reflejar la distribución de cargas de trabajo entre 6 especialistas humanos (incluyendo a Jorge Ulloa como líder del proyecto).
- **Detalle técnico:** Se incorporó un panel superior de miembros activos y la asignación nominal de tiquetes por especialista en la tabla de trazabilidad.
- **Próximos pasos:** Documentar el modelo organizativo y de gobernanza humana en la memoria del TFM.
## [2026-09-22] - Validación Visual del Panel Multi-Agente Humano
- **Hito alcanzado:** Verificación en entorno local (`http://localhost:8000/agentes.html`) de la distribución operativa del equipo de soporte y codificación visual de severidad.
- **Detalle técnico:** Se confirmó la correcta representación gráfica de las cargas de trabajo asignadas y la disponibilidad de los mecanismos de cierre y notificación por correo.
- **Próximos pasos:** Consolidar las evidencias técnicas para la redacción de la memoria académica del TFM.
## [2026-09-22] - Inicio de Redacción Capitular: Capítulo 1 (Introducción y Business Case)
- **Hito alcanzado:** Establecimiento de la estructura y enfoque metodológico para el Capítulo 1 de la memoria técnica del TFM.
- **Detalle técnico:** Se definieron los ejes conceptuales del modelo As-Is (soporte manual ineficiente) y el modelo To-Be (arquitectura hiperautomatizada con n8n y agentes de IA).
- **Próximos pasos:** Redactar el borrador del texto correspondiente al análisis de ineficiencias operativas.
## [2026-09-22] - Documentación del Criterio de Asignación por IA en el TFM
- **Hito alcanzado:** Explicación y validación del mecanismo de asignación inteligente de especialistas mediante System Prompts y análisis semántico en n8n.
- **Detalle técnico:** Se confirmó que la selección del responsable no depende de palabras clave aisladas, sino de la comprensión contextual del incidente y la correspondencia con los perfiles del equipo.
- **Próximos pasos:** Continuar con la redacción del marco metodológico en la memoria técnica.## [2026-09-22] - Especificación de Ubicación y Viabilidad del Dashboard Analítico
- **Hito alcanzado:** Definición de la ruta de visualización local (`http://localhost:8000/agentes.html`) y su integración con los datos de auditoría de Google Sheets para replicar el modelo de métricas analíticas.
- **Detalle técnico:** Se establece que el panel de control consumirá y procesará los metadatos de tiquetes para mostrar gráficos de criticidad y cargas de trabajo del equipo.
- **Próximos pasos:** Integrar los componentes gráficos de visualización en la interfaz web local.
## [2026-09-22] - Normalización y Nomencklatura de Nodos Gmail en n8n
- **Hito alcanzado:** Identificación y renombrado funcional de los tres nodos de Gmail en el flujo de n8n para mejorar la legibilidad y el mantenimiento del pipeline E2E.
- **Detalle técnico:** Se diferenciaron los nodos de acuse de recibo al usuario, alerta al equipo técnico y notificación de cierre/resolución condicional.
- **Próximos pasos:** Validar la ejecución del flujo completo con la nueva nomenclatura.
## [2026-09-22] - Validación del Flujo n8n con Nomenclatura Estructurada
- **Hito alcanzado:** Comprobación visual del pipeline E2E en n8n con la separación clara de canales de notificación (usuario, grupo técnico y resolución alternativa).
- **Detalle técnico:** Se validó la correcta ejecución de los webhooks, el bloque de procesamiento JavaScript, la persistencia en Google Sheets y el enrutamiento condicional.
- **Próximos pasos:** Consolidar las evidencias técnicas para la redacción capitular de la memoria del TFM.
## [2026-09-22] - Definición de 12 Casos de Prueba Multicriticidad E2E
- **Hito alcanzado:** Creación de un set robusto de 12 escenarios de prueba distribuidos en criticidad Alta, Media y Baja para auditar la precisión del LLM y el enrutamiento.
- **Detalle técnico:** Se estructuraron payloads orientados a validar el comportamiento del flujo condicional, las alertas a Telegram/Gmail y la visualización en los dashboards.
- **Próximos pasos:** Ejecutar los 12 casos de prueba de forma iterativa y recopilar las métricas de rendimiento para el TFM.
## [2026-09-22] - Limpieza de Interfaz y Optimización de Auto-refresco Silencioso
- **Hito alcanzado:** Eliminación del contador visual en `agentes.html` y configuración de un temporizador silencioso en segundo plano cada 10 segundos.
- **Detalle técnico:** Se reemplazó el conteo regresivo por una recarga limpia mediante `setTimeout` para mantener la experiencia de usuario profesional y libre de distracciones.
- **Próximos pasos:** Validar el comportamiento del flujo en n8n tras corregir los parámetros de correo electrónico.
## [2026-09-22] - Diagnóstico y Corrección de Ejecución Local y Excepciones en n8n
- **Hito alcanzado:** Identificación de restricciones de seguridad en archivos `file://` y depuración del error de direccionamiento de correo en los nodos de n8n.
- **Detalle técnico:** Se estableció el uso obligatorio del servidor HTTP local de Python (`localhost:8000`) para permitir la actualización de vistas y la correcta gestión de excepciones en el pipeline.
- **Próximos pasos:** Validar el flujo E2E completo mediante el servidor local y documentar el comportamiento en la memoria del TFM.
## [2026-09-22] - Implementación de Persistencia Dinámica en Consola de Agentes
- **Hito alcanzado:** Actualización del script en `agentes.html` para soportar almacenamiento local y renderizado dinámico de tiquetes operativos.
- **Detalle técnico:** Se integró la lectura mediante `localStorage` combinada con el servidor HTTP local de Python para asegurar la sincronización en tiempo real.
- **Próximos pasos:** Validar la ejecución completa del pipeline desde el portal de usuarios hasta la consola de grupo.
## [2026-09-22] - Sincronización de Persistencia Front-End
- **Fase Actual:** Desarrollo de Arquitectura Local.
- **Problema detectado:** Aislamiento de datos en localStorage debido a discrepancia de orígenes (127.0.0.1 vs localhost).
- **Acción técnica:** Homologación estricta del origen (`localhost:8000`) en todas las vistas HTML para cumplir con la política Same-Origin.
- **Resultado esperado:** Sincronización exitosa del estado entre el portal de autoservicio y la consola de gestión de agentes.
## [2026-09-23] - Validación Exitosa de Sincronización y Persistencia E2E
- **Fase Actual:** Pruebas de Integración de Arquitectura y Front-End.
- **Hito alcanzado:** Confirmación visual de la renderización dinámica de tiquetes (`TKT-538021`) en la Consola de Gestión de Agentes tras la inyección desde el Portal de Autoservicio.
- **Validación técnica:** Correcto funcionamiento del almacenamiento local (`localStorage`) bajo el mismo origen (`localhost:8000`), asegurando la consistencia del estado operativo sin pérdida de datos en la interfaz de usuario.
## [2026-09-23] - Mejora de Visualización de KPIs en Dashboard Analítico
- **Fase Actual:** Refinamiento de Front-End y Presentación Ejecutiva.
- **Acción Técnica:** Implementación de callbacks personalizados en Chart.js para el cálculo y despliegue dinámico de porcentajes en los gráficos circulares (`Ticket Status` y `Carga por Especialista`).
- **Justificación Académica:** Optimización de la capa de visualización de datos para cumplir con los estándares de reporte ejecutivo exigidos en el Business Case del TFM, facilitando la lectura de métricas de desempeño y distribución de cargas de trabajo.
## [2026-09-23] - Corrección de Sintaxis y Estabilización de Dashboard Analítico
- **Fase Actual:** Refinamiento de Front-End y Visualización de Datos.
- **Incidente:** Pantalla en blanco provocada por un error de sintaxis en el script de Chart.js al intentar implementar tooltips personalizados.
- **Acción Correctiva:** Reestructuración y depuración completa del bloque JavaScript en `dashboard.html`, asegurando la correcta inicialización de las gráficas con porcentajes dinámicos y la integración con el LocalStorage.
## [2026-09-23] - Optimización de KPIs y Filtrado de Estado en Dashboard
- **Fase Actual:** Refinamiento de Front-End y Presentación Ejecutiva.
- **Acción Técnica:** Desarrollo de un plugin personalizado en Chart.js para renderizar porcentajes de forma fija en las gráficas circulares. Sincronización del contenedor lateral del Dashboard con el LocalStorage, asegurando que los tiquetes cerrados o eliminados de la consola se desechen de la vista activa en tiempo real.
## [2026-09-23] - Estandarización Visual de KPIs y Activación de Webhook de Cierre
- **Fase Actual:** Refinamiento de Interfaz de Usuario y Automatización de Notificaciones E2E.
- **Acción Técnica:** Incorporación de porcentajes fijos en gráficos circulares del Dashboard para optimizar la visualización ejecutiva. Integración de llamada asíncrona (`fetch`) en la Consola de Agentes para disparar el Webhook de cierre de incidencias y automatizar la notificación por correo al usuario final.
## [2026-09-23] - Integración de KPIs Ejecitivos y Observabilidad de Sistema
- **Fase Actual:** Refinamiento de Front-End y Presentación Ejecutiva para TFM.
- **Acción Técnica:** Incorporación de tarjetas de KPIs superiores (Total de Tiquetes Activos enlazado al LocalStorage, Tiempo Promedio y Tasa de Automatización por IA) y adición de un indicador de estado con animación de pulso ("Pipeline n8n: Operativo").
- **Justificación Académica:** Dotar al dashboard de capacidades de observabilidad y métricas de negocio requeridas en la evaluación de proyectos de hiperautomatización.
## [2026-09-23] - Propuesta de Innovación Multimedia: Generación de Video por IA
- **Fase Actual:** Diseño Conceptual Avanzado y Ampliación de Alcance del TFM.
- **Acción Técnica:** Evaluación de integración de APIs de video sintético (avatares generados por IA) dentro del pipeline de n8n para la automatización de tutoriales de soporte y resúmenes ejecutivos multimedia.
- **Justificación Académica:** Incorporación de tecnologías de medios sintéticos en arquitecturas de hiperautomatización para maximizar la experiencia de usuario y la eficiencia en la resolución de incidencias complejas.
## [2026-09-23] - Definición Conceptual de KPI de Tasa de Automatización y Video IA
- **Fase Actual:** Diseño Estratégico y Documentación del Business Case.
- **Validación Técnica:** Consolidación de la métrica de Tasa de Automatización (IA) en el Dashboard gerencial para la medición de eficiencia operativa y justificación de ROI en la memoria del TFM.
## [2026-09-23] - Consolidación de Argumentario de Defensa y Propuesta Multimedia
- **Fase Actual:** Preparación de Defensa de TFM, Business Case y Ampliación de Alcance.
- **Acción Metodológica:** Estructuración del argumentario de defensa para el KPI de Tasa de Automatización (98.5%) y definición de arquitectura para la generación de video tutoriales automatizados mediante avatares de IA.
- **Justificación Académica:** Aporte de valor cuantitativo para el ROI del Business Case e innovación tecnológica en la experiencia omnicanal del usuario.
## [2026-09-23] - Implementación Práctica del Módulo de Video Tutoriales por IA
- **Fase Actual:** Desarrollo de Arquitectura Avanzada y Automatización Multimedia en n8n.
- **Acción Técnica:** Configuración de bifurcación condicional (Nodo If) para incidencias de criticidad alta e integración de nodo HTTP Request para conexión con API de avatares sintéticos, enlazando el resultado multimedia al canal de notificación por correo electrónico.
## [2026-09-23] - Configuración de Endpoint y Payload para API de Video (D-ID)
- **Fase Actual:** Implementación de Soporte Multimedia Automatizado en n8n.
- **Acción Técnica:** Establecimiento del endpoint oficial (`https://api.d-id.com/talks`), configuración de cabeceras de autorización y mapeo de parámetros de cuerpo (Script dinámico y fuente de imagen de avatar) en el nodo HTTP Request.
## [2026-09-25] - Evaluación de Complejidad y Escalabilidad del Proyecto (TFM)
- **Fase Actual:** Análisis Estratégico, Revisión de Alcance y Potenciación de Arquitectura.
- **Acción Metodológica:** Evaluación crítica del nivel de complejidad del sistema frente a los estándares de tribunales de posgrado. Propuesta de integración de capas avanzadas (Soporte multimedia con avatares de IA, gestión robusta de excepciones y enrutamiento multiagente).
- **Justificación Académica:** Elevar el valor de innovación tecnológica y la justificación de retorno de inversión (ROI) para el Business Case de la Memoria y el PDD.
## [2026-09-25] - Definición de Opciones de Potenciación para el TFM
- **Fase Actual:** Diseño Arquitectónico Avanzado y Estrategia de Defensa.
- **Acción Técnica:** Análisis de casos de uso prácticos para la integración de Resiliencia (Error Handling), Sistemas Multiagente y Soporte Multimedia con Avatares de IA.
## [2026-09-25] - Configuración de Credenciales Basic Auth para API D-ID
- **Fase Actual:** Pruebas Unitarias del Módulo Multimedia (Ruta A).
- **Acción Técnica:** Obtención de credenciales en D-ID Studio y configuración del tipo de autenticación nativa `Basic Auth` en n8n para el consumo correcto del endpoint de avatares sintéticos.
## [2026-09-25] - Verificación de Persistencia en Google Sheets (TFM)
- **Fase Actual:** Pruebas unitarias de integración de datos en n8n.
- **Acción Técnica:** Validación del nodo `Append row in sheet1` con credenciales activas y mapeo de variables hacia el archivo `Prueba_TFM`.
 [2026-11-02] Paso 1 - Salida estructurada (completado)
- Decisión: Structured Output Parser con JSON Schema (enums en tipo_documento y criticidad), Auto-Fix activado.
- Motivo: el texto libre del LLM hacía frágil el enrutamiento posterior.
- Entrada de prueba (ticket 4587): sistema de facturación caído.
- Resultado: tipo=incidencia, criticidad=alta, confidence=0.9. fecha y monto = "no_encontrado" (sin alucinación).
- Prompt: v1 (reglas básicas anti-alucinación).
- Incidencias: ngrok estaba offline (ERR_NGROK_3200); se resolvió reiniciando `ngrok http 5678`.
## [2026-11-02] Paso 2 - Esquema v2 y System Prompt v2
- Decisión: cambiar esquema a tickets (categoria, criticidad, usuarios_afectados, duracion_minutos, diagnostico, confidence).
- Regla de negocio: criticidad alta = sistema/hardware/red afecta a 1+ usuarios por más de 30 min.
- Motivo: el Code node devolvía valores por defecto falsos (General, Roberto Salas) sin avisar.
- Prueba ticket 4587: categoria=software, criticidad=alta, confidence=0.7, datos faltantes = "no_encontrado".
- Prompt: v2 (reglas de datos faltantes + confidence bajo ante urgencia sin duración).
## [2026-11-02] Paso 2E/2F - Code node v2 y pruebas
- Decisión: especialista asignado por tabla fija en código (no por IA); eliminados valores por defecto falsos.
- Validaciones: categoria, criticidad, confidence, resumen, correo válido.
- Prueba 4587 (sin correo, sin duración): confidence 0.7, valido=false (correo ausente).
- Prueba 4588 (5 usuarios, 2 h, con correo): categoria=redes, criticidad=alta, confidence 0.95.
## [2026-11-02] Paso 2F - Code node validado
- Prueba 4588 (con correo, 5 usuarios, 120 min): valido=true, estado=Abierto, operador=Carlos Mora (tabla fija), confidence 0.95.
- Prueba 4587 (sin correo): valido=false, estado=Revisión manual.
- Conclusión: el Code node separa tickets válidos de los que requieren revisión.
## [2026-11-02] Paso 2G-2 - IF de confiabilidad
- Decisión: nuevo nodo If0 (Ticket confiable): valido = true AND confidence >= 0.8.
- Umbral 0.8 elegido porque el ticket 4587 (datos faltantes) obtuvo 0.7 y el 4588 (datos completos) obtuvo 0.95.
- Regla: tickets dudosos no reciben correo hasta aprobación humana.
- Prueba 4588: salió por rama True.
## [2026-11-02] Paso 2G-2b - Prueba de rama False
- Se fijó (pin) en el Code node un ticket con valido=false para simular un caso dudoso.
- Resultado: If0 enruta el ticket por la rama False. Rama True conectada a If1 (criticidad).
- Limpieza: dato fijado eliminado tras la prueba.
## [2026-11-02] Paso 2G-3 - Telegram de revisión humana
- Nodo "Telegram Revisión Humana" conectado a la rama false de IF0.
- Prueba ticket 4587 (sin correo): confidence 0.65, valido=false, alerta recibida en Telegram con motivo.
- Observación: el confidence del mismo ticket varió entre ejecuciones (0.7 y 0.65); el modelo no es totalmente determinista.
## [2026-11-02] Paso 2G-4 - Alineación de nombres de campo
- Incidencia: Gmail e If1 usaban nombres del Code node antiguo (id_ticket, correo_cliente, respuesta_ia) y "Alta" con mayúscula.
- Riesgo: fallo silencioso (Telegram crítico nunca se activaba, Gmail con "To" vacío).
- Corrección: Gmail usa correo/id_tiquete/diagnostico/operador; If1 compara con "alta" en minúscula.
## [2026-11-02] Paso 2G-4 - Credencial Gmail
- Incidencia: la credencial OAuth de Gmail caducó (app Google en estado "Prueba", token de 7 días).
- Causa adicional: el login de Google redirige al dominio de ngrok; abrir n8n desde localhost daba "Unauthorized" (la sesión era de otro dominio).
- Solución: reconectar la credencial abriendo n8n desde la URL de ngrok.
- Pendiente: publicar la app OAuth (Público → Publicar app) para evitar caducidad.
## [2026-11-02] Paso 2G-4 - Gmail validado
- Credencial OAuth reconectada abriendo n8n desde el dominio de ngrok.
- Prueba con ticket 4588 (id TKT-1793671750508): Gmail devuelve labelIds=SENT.
- Asunto y destinatario resueltos con los nombres de campo nuevos (id_tiquete, correo).
- Pendiente: publicar la app OAuth para evitar caducidad a 7 días.
## [2026-11-02] Paso 2G-4 - Correo al cliente confirmado
- Prueba ticket 4588: correo recibido en loloulloa@gmail.com con asunto "Ticket TKT-... recibido - Soporte IT".
- Gmail enviado en ambas ramas de If1 (cliente siempre notificado si el ticket es confiable).
## [2026-11-04] Telegram Alerta Crítica
- Incidencia: el nodo Telegram (v1) devolvía "chat not found" pese a token e ID válidos (verificados por PowerShell).
- Causas descartadas: red, DNS, sesión, texto, credencial.
- Solución: reemplazo por nodo HTTP Request POST a /sendMessage. Resultado ok:true.
- Causa de entrada colgada: el nodo no tenía datos de entrada (faltaba ejecutar nodos previos).
- Pendiente: mover el token a una credencial/variable de entorno.
## [2026-11-04] Camino de revisión humana validado
- Prueba ticket 4590 (sin correo, datos ambiguos): IF0 false -> Telegram Revisión Humana OK (ejecución #73, 9.4 s).
- Alerta crítica (4588) y revisión humana (4590) funcionan de punta a punta.
- Pendiente: Google Sheets con columnas nuevas; registrar el estado final del ticket.
## [2026-11-04] Revisión humana confirmada
- Ticket 4590 (sin correo): confidence 0.6, valido=false -> Telegram Revisión Humana entregó el mensaje (12:47).
- Los dos caminos de excepción y crítico funcionan de punta a punta.
## [2026-11-04] Google Sheets validado
- Credencial OAuth reconectada (token de app en modo Prueba caducado).
- Nodo Sheets mapea 13 columnas. Prueba ticket 4588: fila registrada correctamente.
- Observación: confidence del mismo ticket varió (0.95 -> 0.85).
- Camino crítico completo OK: Telegram + Gmail + Sheets.
## [2026-11-04] Registro de tickets dudosos validado
- Rama false de IF0 conectada a Google Sheets.
- Prueba ticket 4590 (sin correo): fila registrada con estado "Revisión manual", confianza 0.6, error de validación documentado.
- Camino crítico (4588) y camino de excepción (4590) validados con registro en Sheets, Telegram y Gmail (solo crítico).
## [2026-11-04] Alineación de equipo y categorías
- Esquema y prompt ampliados: categorias base_datos y seguridad.
- Code node: asignación fija por categoría (Roberto Salas, María Brenes, Carlos Méndez, Esteban Rojas, Ana Lucía Gómez, Jorge Ulloa).
- Hallazgo: con el Code node sin actualizar, el ticket de seguridad (4591) cayó a revisión humana por "categoria invalida"; el sistema desvió el caso en lugar de disfrazarlo.
## [2026-11-04] Equipo y categorías alineados (validado)
- Ticket 4591 (seguridad): categoria=seguridad, operador=Ana Lucía Gómez, estado=Abierto, confianza 0.95.
- Antes del ajuste: mismo ticket -> "categoria invalida" -> revisión manual (fila 4 de la hoja, conservada como evidencia).
- Alerta crítica, registro en Sheets y correo funcionan con las 6 categorías.## [2026-11-04] Workflow de lectura y limpieza de la hoja
- Creado workflow "Lectura": Webhook GET /tickets -> Google Sheets (Get Row(s)) -> Respond to Webhook. CORS abierto (*).
- Incidencia: tabulador (\t) en Categoria y Errores Validacion; se reescribieron los encabezados sin tilde (Categoria, Errores Validacion).
- Incidencia: al cambiar encabezados, el nodo Sheets Append dejó esos dos campos en blanco; se reasignaron las expresiones.
- Prueba ticket 4588: fila registrada con categoria=redes, operador=Roberto Salas, estado=Abierto.
## [2026-11-04] Lectura validada
- GET /webhook-test/tickets devuelve JSON limpio desde Prueba_TFM (sin tabuladores).
- Campos con nombres de la hoja: "ID Tiquete", "Operador Nombre", "Categoria", "Errores Validacion", etc.
## [2026-11-04] Workflow de lectura publicado
- Production URL: GET /webhook/tickets responde JSON desde Prueba_TFM sin intervención manual.
- CORS abierto (*) para desarrollo; en producción se restringiría al dominio del portal.
- Los campos conservan los nombres de la hoja ("ID Tiquete", "Operador Nombre", "Categoria"...).
## [2026-11-09] Dashboard conectado a datos reales
- dashboard.html lee GET /webhook/tickets (workflow de Lectura) con cabecera ngrok-skip-browser-warning.
- Gráficos de estado, carga por especialista, criticidad y categoría calculados desde Google Sheets; refresco cada 30 s.
- KPI de automatización = tickets sin revisión manual / total. Tiempo de resolución: N/D hasta implementar el flujo de resuelto.
- Incidencia: bloque pegado fuera de <script> (se mostraba como texto); resuelto reemplazando el archivo completo.
## [2026-11-09] Pipeline en producción validado
- Workflow de ingesta publicado (/webhook/ticket-soporte). Script PowerShell envió 6 tickets (5001-5006).
- Resultado: 6 filas en Sheets con categorías y especialistas correctos; ticket 5006 sin correo -> Revisión manual (confianza 0.7).
- Dashboard: 7 tickets, automatización 85.7%, gráficos con datos reales.
- Gmail: correo de confirmación recibido para tickets con correo válido.
## [2026-11-09] Portal conectado y robustez ante fallos
- index.html envía { correo, mensaje } a /webhook/ticket-soporte (producción) con CORS abierto.
- Incidencia: ejecución #135 falló en Telegram Alerta Crítica ("connection closed unexpectedly") y detuvo Gmail y Sheets; ticket recuperado con Retry.
- Mejora: Retry On Fail (3 intentos) y On Error = Continue en los nodos de Telegram, para que una alerta caída no pierda el ticket.
## [2026-11-09] Consola de agentes conectada
- agentes.html lee GET /webhook/tickets; muestra solo tiquetes activos (no Resuelto), carga por especialista y estado.
- Eliminados los tiquetes de ejemplo y el borrado local. El botón de cierre llamará a /webhook/cerrar-ticket (workflow de Cierre).
- Añadida columna "Fecha Resolucion" (N) en la hoja para calcular el tiempo de resolución.
## [2026-11-09] Flujo de cierre de tiquetes validado
- Workflow "Cierre": Webhook POST /cerrar-ticket -> Google Sheets (Update Row por ID Tiquete: Estado=Resuelto, Fecha Resolucion=ahora) -> Gmail (correo de resuelto) -> Respond to Webhook.
- Prueba con TKT-1794270146722 desde agentes.html: estado Resuelto, Fecha Creación intacta, correo recibido.
- Incidencias de configuración: "(Expression)" y "(texto fijo)" copiados como valor; fecha mapeada primero a Fecha Creación (corregido antes de ejecutar).
## [2026-11-09] Evaluación del agente de triaje (dataset de 30 tickets)
- Workflow "Evaluacion" (sin notificaciones) escribe en pestaña Evaluacion; 30 tickets enviados con script PowerShell.
- Resultado: categoría 30/30 (100%), criticidad 28/30 (93.3%). Recall de criticidad alta: 15/15.
- Errores: E08 (esperada media, obtenida alta; criterio ambiguo ante solución alternativa) y E24 (esperada media, obtenida baja).
- Observación: ambos errores con confianza >= 0.85; el umbral de 0.8 no los marca para revisión humana.
- Incidencia: 3 envíos (E07, E11, E13) no llegaron a la hoja en la primera pasada; reenviados. Causa no determinada.
- Limitaciones: n=30, etiquetas elaboradas con apoyo de IA, una sola corrida, mensajes mayormente explícitos.
- Archivos: dataset_evaluacion.csv, Prueba_TFM - Evaluacion.tsv, comparacion_resultados.csv.
