SELECT
  count(*)
FROM
  paciente
WHERE
  id IS NULL
;

SELECT
  count(*)
FROM
  profissional
WHERE
  id IS NULL
;

SELECT
  count(*)
FROM
  view_anamnese
WHERE
  id IS NULL
;

SELECT
  count(*)
FROM
  view_evolucao
WHERE
  id IS NULL
;

SELECT
  count(*)
FROM
  view_receituario
WHERE
  id IS NULL
;
