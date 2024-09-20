O diagrama foi construído utilizando a ferramenta [dbdiagram.io](https://dbdiagram.io/).

A descrição do DER segue abaixo:

```sql
// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table profissional {
  id integer [primary key]
  nome varchar
}

Table paciente {
  id integer [primary key]
  nome varchar
}

Table anamnese {
  id integer [primary key]
  paciente_id integer [ref: > paciente.id]
  data_anamnese datetime
  profissional_id integer [ref: > profissional.id]
  historico_clinico varchar
  queixas_principais varchar
  habitos_vida varchar
  historico_familiar varchar
  alergias varchar
}

Table evolucao {
  id integer [primary key]
  paciente_id integer [ref: > paciente.id]
  data_evolucao datetime
  profissional_id integer [ref: > profissional.id]
  descricao varchar
  sinais_vitais varchar
  status_clinico varchar
  observacoes varchar
}

Table receituario {
  id integer [primary key]
  paciente_id integer [ref: > paciente.id]
  data_receituario datetime
  profissional_id integer [ref: > profissional.id]
  medicamento varchar
  dosagem varchar
  frequencia_administracao varchar
  duracao_tratamento varchar
  observacoes varchar
}
```

---

Volta para [README](../README.md)

Volta para [PEP_via_db](PEP_via_db.md)
