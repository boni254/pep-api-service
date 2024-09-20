CREATE TABLE IF NOT EXISTS `profissional` (
  `id` integer PRIMARY KEY,
  `nome` varchar(255) NOT NULL
);

INSERT INTO `profissional` (`id`,`nome`)
VALUES
  (1,"Moses Wise"),
  (2,"Marsden Winters"),
  (3,"Martha Russo"),
  (4,"Neil Hays"),
  (5,"Adam Anthony");

CREATE TABLE IF NOT EXISTS `paciente` (
  `id` integer PRIMARY KEY,
  `nome` varchar(255) NOT NULL
);

INSERT INTO `paciente` (`id`,`nome`)
VALUES
  (1,"Aspen Durham"),
  (2,"Tara Marsh"),
  (3,"Meghan Armstrong"),
  (4,"Kylan Bryant"),
  (5,"Allegra Walter");

CREATE TABLE IF NOT EXISTS `anamnese` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `data_anamnese` datetime NOT NULL,
  `profissional_id` integer NOT NULL,
  `historico_clinico` longtext NOT NULL,
  `queixas_principais` longtext NOT NULL,
  `habitos_vida` longtext,
  `historico_familiar` longtext,
  `alergias` longtext,
  FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`)
);

INSERT INTO `anamnese` (`id`,`paciente_id`,`data_anamnese`,`profissional_id`,`historico_clinico`,`queixas_principais`,`habitos_vida`,`historico_familiar`,`alergias`)
VALUES
  (1,3,"2024-02-18",3,"vulputate eu, odio. Phasellus at augue id ante dictum cursus. Nunc mauris elit, dictum eu,","sit amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor","sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque","libero. Morbi accumsan laoreet ipsum. Curabitur consequat, lectus","pharetra. Nam ac nulla. In tincidunt congue turpis. In condimentum. Donec at arcu. Vestibulum ante ipsum primis in faucibus orci"),
  (2,1,"2024-03-26",3,"arcu. Nunc mauris. Morbi non sapien molestie orci tincidunt adipiscing. Mauris molestie pharetra nibh. Aliquam ornare, libero at auctor","nisi magna sed dui. Fusce aliquam, enim","leo elementum sem, vitae aliquam eros","eget varius ultrices, mauris ipsum porta elit, a feugiat tellus lorem eu metus.","sem. Nulla interdum. Curabitur dictum. Phasellus in felis. Nulla tempor augue ac ipsum. Phasellus vitae mauris"),
  (3,4,"2025-09-12",5,"justo faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse","rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales","tincidunt. Donec vitae erat vel pede blandit congue. In scelerisque scelerisque dui. Suspendisse ac","Duis cursus, diam at pretium aliquet, metus urna convallis","eros non enim commodo hendrerit. Donec porttitor tellus non magna. Nam ligula elit, pretium"),
  (4,2,"2024-07-17",5,"lorem eu metus. In lorem. Donec elementum, lorem ut aliquam iaculis, lacus pede sagittis augue, eu tempor erat","velit. Aliquam nisl. Nulla eu neque pellentesque massa lobortis","aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci. Ut sagittis","tellus. Phasellus elit pede, malesuada vel, venenatis vel,","tempus eu, ligula. Aenean euismod mauris eu elit. Nulla facilisi. Sed neque. Sed eget lacus. Mauris non dui"),
  (5,1,"2023-10-30",5,"blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna et ipsum cursus","nec, malesuada ut, sem. Nulla interdum. Curabitur dictum.","metus vitae velit egestas lacinia. Sed congue, elit sed consequat auctor, nunc nulla vulputate dui,","egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est. Mauris","quis lectus. Nullam suscipit, est ac facilisis facilisis, magna tellus faucibus leo, in lobortis tellus justo");

CREATE TABLE IF NOT EXISTS `evolucao` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `data_evolucao` datetime NOT NULL,
  `profissional_id` integer NOT NULL,
  `descricao` longtext NOT NULL,
  `sinais_vitais` longtext,
  `status_clinico` longtext,
  `observacoes` longtext,
  FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`)
);

INSERT INTO `evolucao` (`id`,`paciente_id`,`data_evolucao`,`profissional_id`,`descricao`,`sinais_vitais`,`status_clinico`,`observacoes`)
VALUES
  (1,3,"2024-02-18",3,"vulputate eu, odio. Phasellus at augue id ante dictum cursus. Nunc mauris elit, dictum eu,","sit amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor","sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque","libero. Morbi accumsan laoreet ipsum. Curabitur consequat, lectus"),
  (2,1,"2024-03-26",3,"arcu. Nunc mauris. Morbi non sapien molestie orci tincidunt adipiscing. Mauris molestie pharetra nibh. Aliquam ornare, libero at auctor","nisi magna sed dui. Fusce aliquam, enim","leo elementum sem, vitae aliquam eros","eget varius ultrices, mauris ipsum porta elit, a feugiat tellus lorem eu metus."),
  (3,4,"2025-09-12",5,"justo faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse","rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales","tincidunt. Donec vitae erat vel pede blandit congue. In scelerisque scelerisque dui. Suspendisse ac","Duis cursus, diam at pretium aliquet, metus urna convallis"),
  (4,2,"2024-07-17",5,"lorem eu metus. In lorem. Donec elementum, lorem ut aliquam iaculis, lacus pede sagittis augue, eu tempor erat","velit. Aliquam nisl. Nulla eu neque pellentesque massa lobortis","aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci. Ut sagittis","tellus. Phasellus elit pede, malesuada vel, venenatis vel,"),
  (5,1,"2023-10-30",5,"blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna et ipsum cursus","nec, malesuada ut, sem. Nulla interdum. Curabitur dictum.","metus vitae velit egestas lacinia. Sed congue, elit sed consequat auctor, nunc nulla vulputate dui,","egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est. Mauris");


CREATE TABLE IF NOT EXISTS `receituario` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `data_receituario` datetime NOT NULL,
  `profissional_id` integer NOT NULL,
  `medicamento` longtext NOT NULL,
  `dosagem` longtext NOT NULL,
  `frequencia_administracao` longtext NOT NULL,
  `duracao_tratamento` longtext NOT NULL,
  `observacoes` longtext,
  FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`),
  FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`)
);

INSERT INTO `receituario` (`id`,`paciente_id`,`data_receituario`,`profissional_id`,`medicamento`,`dosagem`,`frequencia_administracao`,`duracao_tratamento`,`observacoes`)
VALUES
  (1,3,"2024-02-18",3,"vulputate eu, odio. Phasellus at augue id ante dictum cursus. Nunc mauris elit, dictum eu,","sit amet massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor","sit amet ultricies sem magna nec quam. Curabitur vel lectus. Cum sociis natoque","libero. Morbi accumsan laoreet ipsum. Curabitur consequat, lectus","malesuada. Integer id magna et ipsum cursus vestibulum. Mauris magna. Duis dignissim tempor arcu. Vestibulum ut eros"),
  (2,1,"2024-03-26",3,"arcu. Nunc mauris. Morbi non sapien molestie orci tincidunt adipiscing. Mauris molestie pharetra nibh. Aliquam ornare, libero at auctor","nisi magna sed dui. Fusce aliquam, enim","leo elementum sem, vitae aliquam eros","eget varius ultrices, mauris ipsum porta elit, a feugiat tellus lorem eu metus.","Aliquam gravida mauris ut mi. Duis risus"),
  (3,4,"2025-09-12",5,"justo faucibus lectus, a sollicitudin orci sem eget massa. Suspendisse","rhoncus. Nullam velit dui, semper et, lacinia vitae, sodales","tincidunt. Donec vitae erat vel pede blandit congue. In scelerisque scelerisque dui. Suspendisse ac","Duis cursus, diam at pretium aliquet, metus urna convallis","facilisis, magna tellus faucibus leo, in lobortis"),
  (4,2,"2024-07-17",5,"lorem eu metus. In lorem. Donec elementum, lorem ut aliquam iaculis, lacus pede sagittis augue, eu tempor erat","velit. Aliquam nisl. Nulla eu neque pellentesque massa lobortis","aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci. Ut sagittis","tellus. Phasellus elit pede, malesuada vel, venenatis vel,","et nunc. Quisque ornare tortor at risus. Nunc ac sem ut dolor dapibus gravida. Aliquam tincidunt, nunc ac"),
  (5,1,"2023-10-30",5,"blandit mattis. Cras eget nisi dictum augue malesuada malesuada. Integer id magna et ipsum cursus","nec, malesuada ut, sem. Nulla interdum. Curabitur dictum.","metus vitae velit egestas lacinia. Sed congue, elit sed consequat auctor, nunc nulla vulputate dui,","egestas ligula. Nullam feugiat placerat velit. Quisque varius. Nam porttitor scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est. Mauris","lacinia vitae, sodales at, velit. Pellentesque ultricies dignissim lacus. Aliquam");

-- ----------------------
-- ----------------------

CREATE OR REPLACE VIEW view_anamnese AS
SELECT
  a.*, p.nome AS paciente, pr.nome AS profissional
FROM
  anamnese a
JOIN
  paciente p ON a.paciente_id = p.id
JOIN
  profissional pr ON a.profissional_id = pr.id;
;

CREATE OR REPLACE VIEW view_evolucao AS
SELECT
  e.*, p.nome AS paciente, pr.nome AS profissional
FROM
  evolucao e
JOIN
  paciente p ON e.paciente_id = p.id
JOIN
  profissional pr ON e.profissional_id = pr.id;
;

CREATE OR REPLACE VIEW view_receituario AS
SELECT
  r.*, p.nome AS paciente, pr.nome AS profissional
FROM
  receituario r
JOIN
  paciente p ON r.paciente_id = p.id
JOIN
  profissional pr ON r.profissional_id = pr.id;
;
