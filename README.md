# File Organizer Python 📁

Automação em Python para organizar arquivos de uma pasta por categoria, evitando sobrescritas e gerando um relatório da execução.

O projeto foi desenvolvido com foco em **automação de tarefas usando apenas a biblioteca padrão do Python**, sem Pandas e sem dependências externas.

## Objetivo

Automatizar a organização de pastas como `Downloads`, classificando arquivos por extensão em categorias como:

- Imagens
- Documentos
- Planilhas
- Áudio
- Vídeos
- Compactados
- Código
- Outros

## Tecnologias

- Python 3
- `pathlib`
- `shutil`
- `argparse`
- `collections`
- `datetime`
- `unittest`

## Uso esperado

```bash
python main.py "C:/Users/SeuUsuario/Downloads"
```

Ao final, o programa mostra quantos arquivos foram organizados, quais categorias foram criadas e onde o relatório foi salvo.

## Estrutura

```text
file-organizer-python/
├── src/
│   ├── classifier.py
│   ├── organizer.py
│   └── report.py
├── tests/
│   ├── test_classifier.py
│   └── test_organizer.py
├── docs/
│   └── examples.md
├── main.py
├── .gitignore
├── LICENSE
└── README.md
```

## Competências demonstradas

`Python` `Automação` `Manipulação de Arquivos` `CLI` `Tratamento de Erros` `Testes` `Programação Modular`

---

Projeto de portfólio desenvolvido para demonstrar automação prática com Python.
