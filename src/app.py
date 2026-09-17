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
                "content": extract_text_from_docx("transcribed_interviews/colombia/COL Ximena Rueda 26-03-24.docx")
            }
        ],
        output_format=ResearcherModel
    )

    return response.parsed_output


if __name__ == "__main__":
    print(systematize_researcher())
