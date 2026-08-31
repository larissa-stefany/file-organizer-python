# Exemplos de Uso

## Organizar uma pasta

Windows:

```bash
python main.py "C:/Users/SeuUsuario/Downloads"
```

Linux/macOS:

```bash
python main.py ~/Downloads
```

## Testar antes de mover arquivos

Use o modo de simulação:

```bash
python main.py "C:/Users/SeuUsuario/Downloads" --dry-run
```

O programa classifica os arquivos e mostra o resumo sem alterar a pasta.

### Exemplo prático de dry-run

Uma boa forma de demonstrar o projeto no portfólio é criar uma pasta de teste com alguns arquivos e executar primeiro o modo de simulação. Assim, é possível visualizar as categorias identificadas antes de permitir qualquer movimentação real dos arquivos.

```bash
python main.py "C:/Users/SeuUsuario/Desktop/teste-organizador" --dry-run
```

Depois de conferir o resultado, execute novamente sem `--dry-run` para realizar a organização.

## Exemplo de organização

Antes:

```text
Downloads/
├── foto.jpg
├── contrato.pdf
├── dados.csv
├── musica.mp3
└── script.py
```

Depois:

```text
Downloads/
├── Imagens/foto.jpg
├── Documentos/contrato.pdf
├── Planilhas/dados.csv
├── Áudio/musica.mp3
├── Código/script.py
└── relatorio_organizacao.txt
```

## Arquivos com nomes repetidos

O organizador nunca sobrescreve um arquivo existente. Se `foto.jpg` já existir na pasta de destino, o próximo arquivo será salvo como `foto_1.jpg`, depois `foto_2.jpg` e assim por diante.

## Boas práticas

- Execute primeiro com `--dry-run` em pastas importantes.
- Faça backup de arquivos críticos antes de qualquer automação de movimentação.
- O programa organiza apenas os arquivos que estão diretamente na pasta informada; ele não percorre subpastas existentes.
