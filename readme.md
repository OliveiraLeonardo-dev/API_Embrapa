# API de Consulta de Dados de Vitivinicultura da Embrapa

Este projeto é uma API REST desenvolvida em Python com FastAPI que consulta dados públicos de vitivinicultura disponibilizados pela Embrapa. A API permite baixar arquivos PDF relacionados a Produção, Processamento, Comercialização, Importação e Exportação de uvas e derivados.

## Funcionalidades

- Consulta e download dos dados diretamente do site da Embrapa.
- Endpoints para Produção, Processamento (com subgrupos), Comercialização, Importação (com subgrupos) e Exportação (com subgrupos).
- URLs de consulta organizadas em arquivo externo (`options.json`).
- Documentação automática via FastAPI (Swagger UI).

## Como rodar

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
