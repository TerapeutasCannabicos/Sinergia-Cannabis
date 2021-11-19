from app.extensions import db 
from app.model import BaseModel

class Horario(BaseModel):
    __tablename__ = 'horario'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    disponivel = db.Column(db.Boolean, default=False)

    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    agendamento = db.relationship("Agendamento", uselist=False, back_populates="horario")