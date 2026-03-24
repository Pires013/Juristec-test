from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Define a classe base para criar as tabelas do banco
base = declarative_base()

class Cliente(base):
    """
    Representa a tabela 'clientes' no banco de dados.
    Armazena informações básicas do cliente e sua relação com processos.
    """
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)
    estado = Column(String)
    processos = relationship("Processos", back_populates="cliente")

class Processo(base):
    """
    Representa a tabela 'processos' no banco de dados.
    Cada processo está vinculado a um único cliente.
    """
    __tablename__ = 'processos'

    id_processo = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    assunto = Column(String)
    data_abertura = Column(Date)
    cliente = relationship("Cliente", back_populates="processos")