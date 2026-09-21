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


def systematize_researcher() -> str:
    response = client.messages.parse(
        model="claude-opus-5",
        max_tokens=16000,
        system=RESEARCHER_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": extract_text_from_docx("transcribed_interviews/chile/chile_alejandra_caqueo_11_03_24.docx")
            }
        ],
        output_format=ResearcherModel
    )

    parsed_res = response.parsed_output
    if parsed_res is None:
        raise RuntimeError("LLM response returned no result.")
    json_format = json.dumps(parsed_res.model_dump(by_alias=True), indent=2, ensure_ascii=False)
    return json_format


if __name__ == "__main__":
    print(systematize_researcher())
