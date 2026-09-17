from pydantic import BaseModel, Field


class VerbatimQuotes(BaseModel):
    conocimiento_propio: list[str] = Field(
        validation_alias="1.1_conocimiento_propio",
        serialization_alias="1.1_conocimiento_propio",
        min_length=1
    )
    tendencias_en_el_pais: list[str] = Field(
        validation_alias="1.2_tendencias_en_el_pais",
        serialization_alias="1.2_tendencias_en_el_pais",
        min_length=1
    )
    tendencias_latam: list[str] = Field(
        validation_alias="1.3_tendencias_latam",
        serialization_alias="1.3_tendencias_latam",
        min_length=1
    )
    tendencias_mundo: list[str] = Field(
        validation_alias="1.4_tendencias_mundo",
        serialization_alias="1.4_tendencias_mundo",
        min_length=1
    )
    formacion: list[str] = Field(
        validation_alias="2.1_formacion",
        serialization_alias="2.1_formacion",
        min_length=1
    )
    instituciones: list[str] = Field(
        validation_alias="2.2_instituciones",
        serialization_alias="2.2_instituciones",
        min_length=1
    )
    organismos: list[str] = Field(
        validation_alias="3.1_organismos",
        serialization_alias="3.1_organismos",
        min_length=1
    )
    medios_divulgacion: list[str] = Field(
        validation_alias="3.2_medios_divulgacion",
        serialization_alias="3.2_medios_divulgacion",
        min_length=1
    )
    redes: list[str] = Field(
        validation_alias="3.3_redes",
        serialization_alias="3.3_redes",
        min_length=1
    )
    financiamiento: list[str] = Field(
        validation_alias="4.1_financiamiento",
        serialization_alias="4.1_financiamiento",
        min_length=1
    )
    recursos_humanos: list[str] = Field(
        validation_alias="4.2_recursos_humanos",
        serialization_alias="4.2_recursos_humanos",
        min_length=1
    )
    otros_recursos_investigacion: list[str] = Field(
        validation_alias="4.3_otros_recursos_investigacion",
        serialization_alias="4.3_otros_recursos_investigacion",
        min_length=1
    )


class Researcher(BaseModel):
    name: str = Field(min_length=2)
    country: str = Field(min_length=2)
    verbatim_quotes: VerbatimQuotes
