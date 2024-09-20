SELECT
  id,
  COUNT(*)
FROM
  paciente
GROUP BY
  id
HAVING
  COUNT(*) > 1
;

SELECT
  id,
  COUNT(*)
FROM
  profissional
GROUP BY
  id
HAVING
  COUNT(*) > 1
;

SELECT
  id,
  COUNT(*)
FROM
  view_anamnese
GROUP BY
  id
HAVING
  COUNT(*) > 1
;

SELECT
  id,
  COUNT(*)
FROM
  view_evolucao
GROUP BY
  id
HAVING
  COUNT(*) > 1
;

SELECT
  id,
  COUNT(*)
FROM
  view_receituario
GROUP BY
  id
HAVING
  COUNT(*) > 1
;
