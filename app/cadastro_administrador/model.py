from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_table, association_table2, association_table3, association_table4

class Administrador(BaseModel):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    cpf = db.Column(db.String(30),unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    telefone_secundario = db.Column(db.String(20), default=None)
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(50), nullable=False) 
    nome_associação = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.LargeBinary(128))

    gestor = db.relationship('Gestor', secondary=association_table, backref='administrador')
    paciente = db.relationship('Paciente', secondary=association_table2, backref='administrador2')
    medico = db.relationship('Medico', secondary=association_table3, backref='administrador3')
    outros = db.relationship('Outros', secondary=association_table4, backref='administrador4')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)