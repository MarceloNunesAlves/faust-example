import faust

app = faust.App('hello-consumer-group', broker='kafka://localhost:9092')

class Entidade(faust.Record):
    nome: str
    idade: int
    itens: list

topic = app.topic('hello-topic', value_type=Entidade)

@app.agent(topic)
async def hello(entidades):
    async for entidade in entidades:
        print(f'Hello from {entidade.nome} - {entidade.idade} - {entidade.itens}')

@app.timer(interval=1.0)
async def example_sender(app):
    await topic.send(
        value=Entidade(nome='Faust', idade=30, itens=['Teste 1', 'Teste 2']),
    )

if __name__ == '__main__':
    app.main()