from flask import Flask


app = Flask('task_app')


@app.route('/')
def menu():
    return '''
<h1>Menu</h1>

<ul>
    <li>Listar</li>
    <li>Adicionar</li>
    <li>Editar</li>
    <li>Remover</li>
</ul>
'''

@app.route('/lista')
def list_tasks():
    return 'Lista de tarefas'


#  eh equivalente a isso:
#  func = app.route('/lista')
#  func(list_tasks)


app.run(debug=True)
