Seguem abaixo instruções para realizar o teste técnico com o objetivo de avaliar as habilidades em Python, API, Docker, SQL, interoperabilidade de sistemas e boas práticas de desenvolvimento, como testes unitários e documentação.


# Tarefas:

## 1. Integração com Serviço de PEP - Prontuário Eletrônico do Paciente (API RESTful)

**Objetivo**: Extrair dados de informações clínicas (evoluções médicas, anamneses, receituários) - Sugestões de campos no final do documento.

**Tarefa**: Desenvolver um microserviço em Python que realiza as seguintes operações:
- Receber requisições POST para integração com a API do barramento, contendo informações clínicas.
- Ao receber os dados, o microserviço deve:
  - Validar os dados de entrada, garantindo que os campos obrigatórios estejam presentes.
  - Publicar os dados em uma fila de mensagens (por exemplo, RabbitMQ), que será consumida posteriormente pelo backend da aplicação.
- O microserviço deve ser dockerizado para facilitar o deployment.

Requisitos Adicionais:
- Testes Unitários: Escrever testes unitários que garantam a validação dos dados e a publicação correta na fila.
- Documentação: Incluir documentação que explique:
  - Como rodar o microserviço localmente com Docker.
  - Como testar os endpoints e rodar os testes unitários.
  - Descrição dos endpoints criados, parâmetros de entrada e formato de saída.

Entrega:
- Código-fonte do microserviço (com testes unitários).
- Dockerfile e instruções para rodar o serviço.
- Documentação dos endpoints e do processo de integração.

## 2. Integração com PEP (via Banco de Dados)

**Objetivo**: Acessar informações de prontuário eletrônico do paciente diretamente do sistema de gestão hospitalar (evoluções médicas, anamneses, receituários) - Sugestões de campos no final do documento.

**Tarefa**: Criar scripts SQL para ler dados a partir de View no banco de dados do PEP (PostgreSQL ou MySQL), garantindo a consistência e integridade dos dados.

Requisitos Adicionais:

- Testes de Validação: Incluir scripts de verificação que garanta a integridade dos dados (por exemplo, checar se não há dados duplicados ou ausentes nas chaves primárias).
- Documentação: Incluir uma documentação que descreva:
  - Como executar os scripts.
  - Como os dados são organizados nas views.
  - Quais garantias de integridade são verificadas.

Entrega:

- Scripts SQL.
- Documentação explicando o funcionamento dos scripts e as validações realizadas.

---
---

## Sugestões do mapeamento de dados

### 1. Evoluções Médicas
Evoluções médicas documentam o acompanhamento clínico do paciente ao longo do tempo. Sugestões para o desafio:
- ID da Evolução (obrigatório): Identificador único para cada evolução médica.
- ID do Paciente (obrigatório): Identificador único do paciente.
- Data da Evolução (obrigatório): Data e hora em que a evolução foi registrada.
- ID do Profissional de Saúde (obrigatório): Identificador do médico ou profissional que registrou a evolução.
- Descrição da Evolução (obrigatório): Texto livre contendo detalhes sobre a evolução médica.
- Sinais Vitais (opcional): Dados como pressão arterial, frequência cardíaca, temperatura, entre outros.
- Status Clínico (opcional): Indicação do estado clínico do paciente (melhora, piora, estável, etc.).
- Observações Adicionais (opcional): Outras informações que possam ser relevantes ao caso.

### 2. Anamneses
A anamnese refere-se ao histórico do paciente coletado durante a primeira consulta ou ao longo de seu acompanhamento. Sugestões para o desafio:

- ID da Anamnese (obrigatório): Identificador único da anamnese.
- ID do Paciente (obrigatório): Identificador único do paciente.
- Data da Anamnese (obrigatório): Data e hora em que a anamnese foi registrada.
- ID do Profissional de Saúde (obrigatório): Identificador do médico ou profissional que realizou a coleta da anamnese.
- Histórico Clínico (obrigatório): Texto livre com o relato sobre o histórico médico do paciente, incluindo doenças pregressas, cirurgias, alergias, etc.
- Queixas Principais (obrigatório): Motivo da consulta e principais sintomas relatados.
- Hábitos de Vida (opcional): Informações sobre alimentação, exercício, tabagismo, consumo de álcool, etc.
- Histórico Familiar (opcional): Registro de doenças familiares relevantes, como doenças hereditárias.
- Alergias (opcional): Detalhes sobre alergias conhecidas do paciente.

### 3. Receituários
Receituários são prescrições médicas com orientações sobre os medicamentos a serem tomados pelo paciente. Sugestões para o desafio:

- ID do Receituário (obrigatório): Identificador único do receituário.
- ID do Paciente (obrigatório): Identificador único do paciente.
- Data da Prescrição (obrigatório): Data e hora em que o receituário foi emitido.
- ID do Profissional de Saúde (obrigatório): Identificador do médico que prescreveu a receita.
- Medicamento (obrigatório): Nome do medicamento prescrito.
- Dosagem (obrigatório): Quantidade do medicamento a ser administrada.
- Frequência de Administração (obrigatório): Intervalo de tempo entre as doses
- Duração do Tratamento (obrigatório): Período de tempo em que o paciente deve tomar o medicamento.
- Observações (opcional): Instruções adicionais.


## Instruções Gerais:

Prazo: o prazo para a entrega do desafio é de 7 dias.

Forma de Entrega: submeter o código em um repositório, acompanhado da documentação.

A nossa avaliação considerará a qualidade do código, a cobertura de testes, a clareza da documentação e a aderência aos requisitos.

---

Volta para [README](../README.md)
