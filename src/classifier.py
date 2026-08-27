"""File classification rules used by the organizer."""

from pathlib import Path

CATEGORIES = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"},
    "Planilhas": {".xls", ".xlsx", ".csv", ".ods"},
    "Áudio": {".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"},
    "Vídeos": {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".webm"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Código": {".py", ".js", ".ts", ".html", ".css", ".java", ".sql", ".json", ".xml"},
}


def classify_file(file_path: Path) -> str:
    """Return the destination category based on a file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Outros"
