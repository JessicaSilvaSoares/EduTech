\COPY DBO.alunos FROM './data/alunos.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.especialidades FROM './data/especialidades.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.instrutores FROM './data/instrutores.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.especialidades_instrutores FROM './data/especialidades_instrutores.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.categorias FROM './data/categorias.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.cursos_nivel FROM './data/cursos_nivel.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.cursos FROM './data/cursos.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.modulos FROM './data/modulos.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.aulas_tipo FROM './data/aulas_tipo.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.aulas FROM './data/aulas.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.matriculas_status FROM './data/matriculas_status.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.matriculas FROM './data/matriculas.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.progresso_aulas FROM './data/progresso_aulas.csv' DELIMITER ';' CSV HEADER;

\COPY DBO.avaliacoes FROM './data/avaliacoes.csv' DELIMITER ';' CSV HEADER;
