import json
from pathlib import Path

from anthropic import Anthropic
from docx import Document
from dotenv import load_dotenv

from researcher_model import ResearcherModel

load_dotenv()

RESEARCHER_SYSTEM_PROMPT = Path("src/researcher_system_prompt.md").read_text()

client = Anthropic()

def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)
    extracted_paragraphs: list[str] = []

    for paragraph in document.paragraphs:
        extracted_paragraphs.append(paragraph.text)

    return "\n".join(extracted_paragraphs)


def systematize_researcher() -> ResearcherModel:
    response = client.messages.parse(
        model="claude-opus-5",
        max_tokens=16000,
        system=RESEARCHER_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": extract_text_from_docx("transcribed_interviews/mexico_mariano_rojas_07-02-2024.docx")
            }
        ],
        output_format=ResearcherModel
    )

    parsed_res = response.parsed_output
    if parsed_res is None:
        raise RuntimeError("LLM response returned no result.")
    return parsed_res

def save_json(parsed_json: ResearcherModel) -> None:
    # Create directory
    new_dir = Path("outputs_researchers")
    new_dir.mkdir(exist_ok=True)
    # Create file
    path = new_dir / f"{parsed_json.country.lower()}_{parsed_json.name.replace(" ", "_").lower()}.json"
    path.write_text(json.dumps(parsed_json.model_dump(by_alias=True), indent=2, ensure_ascii=False))
    print(f"{parsed_json.name}'s quotes saved to {path}\n")

if __name__ == "__main__":
    parsed_response = systematize_researcher()
    save_json(parsed_response)
