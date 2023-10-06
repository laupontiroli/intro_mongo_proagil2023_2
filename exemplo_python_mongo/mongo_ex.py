import pymongo 

uri='mongodb+srv://admin:admin@projagil.z48s3xs.mongodb.net/?retryWrites=true&w=majority'
client_con = pymongo.MongoClient(uri)

#FIND(filter igual o do mongo)  pega todos
#FIND_ONE pega o primeiro
#INSERT insere todos
#INSERT_ONE insere um
#UPDATE atualiza todos
#UPDATE_ONE atualiza o primeiro
#DELETE deleta todos
#DELETE_ONE  deleta o primeiro 

#selecionei o banco de dados e a collection
pacientes_collec = client_con.db_clinica.pacientes

#filtrando os dados
resultados= pacientes_collec.find()
print('todos os pacientes')
print(list(resultados))

filter_= {
    'idade':{'$gt': 31}
}

projection={
    'nome_paciente':1
}

filtrado= pacientes_collec.find_one(filter_,projection)
print('todos os pacientes com idade maior que 31')
print(filtrado)
