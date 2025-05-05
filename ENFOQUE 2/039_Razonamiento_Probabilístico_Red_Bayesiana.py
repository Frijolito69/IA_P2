from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos la red
modelo = BayesianNetwork([('Lluvia', 'Tráfico'), ('Tráfico', 'Llegar_tarde')])

# Definimos las tablas de probabilidad condicional
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.3], [0.7]])
cpd_trafico = TabularCPD(variable='Tráfico', variable_card=2,
                         values=[[0.8, 0.2],   # Tráfico sí dado Lluvia sí / no
                                 [0.2, 0.8]],
                         evidence=['Lluvia'],
                         evidence_card=[2])

cpd_llegar_tarde = TabularCPD(variable='Llegar_tarde', variable_card=2,
                              values=[[0.9, 0.1],   # Llegar tarde sí dado Tráfico sí / no
                                      [0.1, 0.9]],
                              evidence=['Tráfico'],
                              evidence_card=[2])

# Asociamos los CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_trafico, cpd_llegar_tarde)

# Verificamos si el modelo es válido
print("¿El modelo es válido?", modelo.check_model())

# Inferencia
inferencia = VariableElimination(modelo)

# Consulta: ¿Cuál es la probabilidad de llegar tarde si está lloviendo?
resultado = inferencia.query(variables=['Llegar_tarde'], evidence={'Lluvia': 1})
print(resultado)
