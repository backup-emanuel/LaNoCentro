CREATE TABLE tb_contato(
	id_contato INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL,
	email VARCHAR(255) NOT NULL,
	telefone INTEGER NOT NULL
	);

CREATE TABLE tb_endereco(
	id_endereco INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	logradouro VARCHAR(65) NOT NULL,
	numero VARCHAR(4) NOT NULL,
	complemento VARCHAR(45) NOT NULL,
	cidade VARCHAR(45) NOT NULL,
	estado VARCHAR(45) NOT NULL,
	cep VARCHAR(8) NOT NULL,
	ponto_referencia VARCHAR(65) NOT NULL
	);
    
CREATE TABLE tb_empresa(
	id_empresa INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL,
	id_endereco INTEGER NOT NULL,
	email VARCHAR(255) NOT NULL,
	telefone INTEGER NOT NULL,
	instagram VARCHAR(255) NOT NULL,
	facebook VARCHAR(255) NOT NULL,
	FOREIGN KEY(id_endereco) REFERENCES tb_endereco(id_endereco)
	);
    
CREATE TABLE tb_produto(
	id_produto INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL,
	descricao VARCHAR(45) NOT NULL,
	preco NUMERIC(12,2) NOT NULL
	);
    
CREATE TABLE tb_empresa_produto(
	id_empresa_produto INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_empresa INTEGER NOT NULL,
	id_produto INTEGER NOT NULL,
	FOREIGN KEY(id_empresa) REFERENCES tb_empresa(id_empresa),
	FOREIGN KEY(id_produto) REFERENCES tb_produto(id_produto)
	);