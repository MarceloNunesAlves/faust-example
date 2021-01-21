import faust
from faust.web import Request, Response, View

app = faust.App('hello-consumer-group', broker='kafka://localhost:9092')

class Entidade(faust.Record):
    nome: str
    idade: int
    itens: list

topic = app.topic('hello-topic', value_type=Entidade)

@app.agent(topic)
async def hello(entidades):
    async for entidade in entidades:
        print(f'Dado recebido no streaming -> {entidade.nome} - {entidade.idade} - {entidade.itens}')

@app.page('/putKafka/')
class addKafka(View):

    async def post(self, request: Request) -> Response:
        nome: str = request.query['nome']
        idade: int = request.query['idade']

        await topic.send(value=Entidade(nome=nome, idade=idade, itens=["Item 1", "Item 2", "Item 3"]),)

        return self.json({'msg': 'OK'})

if __name__ == '__main__':
    app.main()