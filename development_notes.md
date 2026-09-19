# Human Flourishing Systematization Tool - Development Notes

## Files and Directories

- `classification_reference.xlsx`: spreadsheet with the classification data like reference codes, categories and keywords (divided into `interviews` and `focus groups` tabs)
- `transcripted_interviews`: directory with transcripts of interviews conducted individually to full-time researchers
- `transcripted_focus_groups`: directory with focus groups' transcripts conducted to civil organizations and foundations

## How the App Works

0. The system is divided into 2 processes, one for processing individual interviews conducted to full-time researchers and other for processing focus groups conducted to a civil organization or foundation. For each process:
1. The main `api` call takes one of the transcripts as input
2. For individual interviews conducted to researchers, the model identifies the following items based on the `classification_reference_xlsx`'s `interviews` tab and produces a structured `json` output containing them:

   - `C1 LIDERAZGO ACADÉMICO` (vinculación del investigador con el tema de FH): conocimiento propio sobre FH, tendencias de FH en su país, tendencias en LATAM, tendencias en el mundo
   - `C2 CAPACIDADES`: experiencia en la formación de estudiantes e investigación con alumnos, organismos e instituciones involucradas en lo anterior
   - `C3 COLABORACIÓN`(con expertos sobre temas relacionados a FH): organismos e instituciones que han intervenido en sus proyectos, medios de difusión de investigaciones que usa o reconoce, redes y grupos que conoce o en los que participa
   - `C4 RECURSOS`: recursos económicos para sus investigaciones, recursos humanos, recursos complementarios

3. For focus groups conducted to civil organizations and foundations, the model identifies the following items based on the `classification_reference_xlsx`'s `focus groups` tab and produces a structured `json` output containing them:

   - `C1 RECURSOS PARA TEMAS DE FH`: percepción sobre la disponibilidad de recursos, fondos de los que ha dispuesto su organización, proyectos o iniciativas que han apoyado o realizado
   - `C2 ECOSISTEMA DE INVESTIGACIÓN` (regional, nacional o global): actores dentro del sistema de investigación, necesidades sociales, personales o ambientales, relevancia atribuida a la investigación académica
   - `C3 COLABORACIÓN` (regional, nacional o global): Colaboración con universidades, fundaciones, etc.
   - `C4 TEMAS EMERGENTES`: otros temas relacionados con FH en los que han intervenido, temas nuevos (problemas emergentes o temas poco conocidos)
   - `C5 FLORECIMIENTO HUMANO`: cómo entienden el concepto de `FH`, importancia de la investigación o de la intervención del `FH` (para las personas, sociedad, comunidad, el mundo)
5. Steps 1-4 run inside a loop for each existing transcript
