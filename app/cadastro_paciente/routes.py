from flask import Blueprint 
from app.cadastro_paciente.controllers import (PacienteCreate, PacienteDetails) 
#Change Password

paciente_api = Blueprint('paciente_api', __name__)

paciente_api.add_url_rule(
    '/paciente', view_func=PacienteCreate.as_view('paciente_create'), methods=['GET', 'POST']
)

paciente_api.add_url_rule(
    '/paciente/<int:id>', view_func=PacienteDetails.as_view('paciente_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

paciente_api.add_url_rule(
    '/pw-change', view_func=ChangePassword.as_view('password_change'), methods=['POST']
)