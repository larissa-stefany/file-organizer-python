"""Generate a text report after the organization process."""

from datetime import datetime
from pathlib import Path


def save_report(source: Path, summary: dict) -> Path:
    """Save a human-readable report and return its path."""
    report_path = source / "relatorio_organizacao.txt"
    lines = [
        "RELATÓRIO DE ORGANIZAÇÃO DE ARQUIVOS",
        "=" * 40,
        f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        f"Pasta: {source}",
        f"Modo simulação: {'Sim' if summary['dry_run'] else 'Não'}",
        f"Arquivos encontrados: {summary['total_files']}",
        f"Arquivos processados: {summary['moved_files']}",
        "",
        "Categorias:",
    ]

    if summary["categories"]:
        for category, count in sorted(summary["categories"].items()):
            lines.append(f"- {category}: {count}")
    else:
        lines.append("- Nenhum arquivo classificado")

    lines.extend(["", "Erros:"])
    if summary["errors"]:
        lines.extend(f"- {error}" for error in summary["errors"])
    else:
        lines.append("- Nenhum erro encontrado")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
