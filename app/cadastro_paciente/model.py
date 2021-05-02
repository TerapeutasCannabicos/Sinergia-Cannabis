from app.extensions import db
import bcrypt

class Paciente(BaseModel):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date(), nullable=False) #Coloco DateTime ou String??
    cpf = db.Colum(db.String(30),unique=True, nullable=False) #Uso String ou Integer??
    rg = db.Colum(db.Integer,unique=True, nullable=False)
    documentos_pessoais = db.Colum(db.String(2000), nullable=False) #colocar envio de arquivos
    diagnóstico = db.Colum(db.String(2000), nullable=False)   #colocar envio de arquivos
    laudo_médico = db.Colum(db.String(2000), nullable=False) #colocar envio de arquivos
    receita_médica = db.Colum(db.String(2000), nullable=False) #colocar envio de arquivos
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False) 
    password_hash = db.Column(db.LargeBinary(128))

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

#Token
#sistema de adimin só o Responsável pode criar o cadastro do paciente

