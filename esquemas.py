from pydantic import BaseModel, Field
from typing import List

class Vulnerabilidad(BaseModel):
    cve_id: str = Field(description="Identificador CVE de la vulnerabilidad, ej: CVE-2023-1234")
    nombre: str = Field(description="Nombre o título de la vulnerabilidad")
    severidad: str = Field(description="Nivel de criticidad: Crítica, Alta, Media o Baja")
    cvss_score: float = Field(description="Puntuación numérica CVSS del 0.0 al 10.0")
    activo_afectado: str = Field(description="Dirección IP o hostname del servidor afectado")
    recomendacion: str = Field(description="Pasos propuestos para remediar la vulnerabilidad")

class ReporteSeguridadEstructurado(BaseModel):
    fecha_escaneo: str = Field(description="Fecha en que se realizó el reporte")
    herramienta_origen: str = Field(description="Nombre de la herramienta de escaneo (ej: Nessus, Qualys)")
    total_vulnerabilidades: int = Field(description="Cantidad total de hallazgos en el reporte")
    hallazgos: List[Vulnerabilidad] = Field(description="Lista detallada de las vulnerabilidades encontradas")