from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.cadastro_gestor.model import Gestor
from app.cadastro_administrador.model import Administrador
from app.cadastro_medico.model import Medico
from app.cadastro_paciente.model import Paciente
from app.cadastro_advogado.model import Advogado
#from app.cadastro_outros import Outros
from app.cadastro_responsavel import Responsavel

from functools import wraps

def gestor_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        gestor = Gestor.query.get(kwargs.get(id)) 
        if kwargs.get('gestor_id') == get_jwt_identity(): 
            check = Gestor.query.get_or_404(get_jwt_identity())
            if check.type_gestor == 'gestor':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper

def medico_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        medico =Medico.query.get(kwargs.get(id)) 
        if kwargs.get('medico_id') == get_jwt_identity(): 
            check = Medico.query.get_or_404(get_jwt_identity())
            if check.type_medico == 'medico':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper

def administrador_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        administrador =Administrador.query.get(kwargs.get(id)) 
        if kwargs.get('administrador_id') == get_jwt_identity(): 
            check = Administrador.query.get_or_404(get_jwt_identity())
            if check.type_administrador == 'administrador':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper

def paciente_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        paciente =Paciente.query.get(kwargs.get(id)) 
        if kwargs.get('paciente_id') == get_jwt_identity(): 
            check = Paciente.query.get_or_404(get_jwt_identity())
            if check.type_paciente == 'paciente':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper

def advogado_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        advogado =Advogado.query.get(kwargs.get(id)) 
        if kwargs.get('advogado_id') == get_jwt_identity(): 
            check = Advogado.query.get_or_404(get_jwt_identity())
            if check.type_advogado == 'advogado':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper
'''
def outros_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        outros = Outros.query.get(kwargs.get(id)) 
        if kwargs.get('outros_id') == get_jwt_identity(): 
            check = Outros.query.get_or_404(get_jwt_identity())
            if check.type_outros == 'outros':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper
'''

def responsavel_jwt_required(func): 
    @wraps(func) 
    def wrapper(*args, **kwargs):  
        verify_jwt_in_request()
        responsavel = Responsavel.query.get(kwargs.get(id)) 
        if kwargs.get('responsavel_id') == get_jwt_identity(): 
            check = Responsavel.query.get_or_404(get_jwt_identity())
            if check.type_responsavel == 'responsavel':
                return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper