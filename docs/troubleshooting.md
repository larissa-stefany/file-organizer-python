# Troubleshooting

## A pasta não existe

Confira o caminho informado no terminal e use aspas quando houver espaços no nome da pasta.

```bash
python main.py "C:\Users\Larissa\Downloads"
```

## Quero testar sem mover arquivos

Use o modo de simulação:

```bash
python main.py "C:\Users\Larissa\Downloads" --dry-run
```

## Quero ignorar uma extensão

Use `--ignore-ext`. A opção pode ser repetida:

```bash
python main.py "C:\Users\Larissa\Downloads" --ignore-ext .tmp --ignore-ext .log
```

## Arquivo com nome duplicado

O organizador nunca sobrescreve um arquivo existente. Quando encontra um nome repetido, cria automaticamente uma nova versão como `arquivo_1.pdf`, `arquivo_2.pdf` e assim por diante.

## Erro de permissão

Algumas pastas do sistema podem exigir privilégios adicionais. Prefira executar o projeto em pastas pessoais, como Downloads ou Documentos.
