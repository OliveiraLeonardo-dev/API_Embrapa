# API de Consulta de Dados de Vitivinicultura da Embrapa

Este projeto é uma API REST desenvolvida em Python com FastAPI que consulta dados públicos de vitivinicultura disponibilizados pela Embrapa. A API permite baixar arquivos CSV relacionados a Produção, Processamento, Comercialização, Importação e Exportação de uvas e derivados.

## Funcionalidades

- Consulta e download dos dados diretamente do site da Embrapa.
- Endpoints para Produção, Processamento (com subgrupos), Comercialização, Importação (com subgrupos) e Exportação (com subgrupos).
- URLs de consulta organizadas em arquivo externo (`options.json`).
- Documentação automática via FastAPI (Swagger UI).

- ## 🔧 Plano de Deploy e Arquitetura da Solução

### Arquitetura

- Usuário → API (FastAPI) → Download dos dados da Embrapa
- Armazenamento local → Arquivos `.xlsx`
- Etapa futura: leitura desses dados em um pipeline de ML para previsão

### Etapas

1. **Ingestão**: via endpoints que extraem itens do site da Embrapa.
2. **Armazenamento**: os arquivos são salvos em `/dados` no formato Excel.
3. **Deploy**: feito no Render, tornando a API acessível publicamente.
4. **Aplicação futura**: alimentação de modelos de machine learning e analises.

### Cenário de uso

> Uma vinícola pode usar esses dados para prever a produção de uvas viníferas e estimar o volume de vendas, otimizando logística e tomada de decisão. Assim como a intesividade a ser proposta na questão de importação a fins de produzir em quantidade com mais exatidão pra essa finalidade


## Como rodar

1. Clone o repositório:

```bash
git clone <https://github.com/OliveiraLeonardo-dev/API_Embrapa.git>
cd <API_Embrapa>
