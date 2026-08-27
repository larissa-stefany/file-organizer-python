"""Command-line entry point for the file organizer."""

import argparse
from pathlib import Path

from src.organizer import FileOrganizer
from src.report import save_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Organiza automaticamente arquivos de uma pasta por categoria."
    )
    parser.add_argument("path", type=Path, help="Pasta que será organizada")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra o que seria feito sem mover os arquivos",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    organizer = FileOrganizer(args.path, dry_run=args.dry_run)

    try:
        summary = organizer.organize()
    except (FileNotFoundError, NotADirectoryError) as exc:
        raise SystemExit(f"Erro: {exc}") from exc

    print(f"Arquivos processados: {summary['moved_files']}")
    for category, count in sorted(summary["categories"].items()):
        print(f"- {category}: {count}")

    if args.dry_run:
        print("Simulação concluída. Nenhum arquivo foi movido.")
        return

    report_path = save_report(args.path, summary)
    print(f"Relatório salvo em: {report_path}")


if __name__ == "__main__":
    main()
