from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<usuario>:<password>@cluster0.as00imp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# inserção de dados
    
db = client['loja_farmacia']
collection = db['farmacia']

farmacia = [
    {
    "codigo":"1",
    "nome":"Dipirona",
    "valor":"3.00"
    },
    {
    "codigo":"2",
    "nome":"Amoxilina",
    "valor":"30.00"
    },
]

collection.insert_many(farmacia)
print(collection.find_one())