# faust-example
## Subir o ambiente

Para subir o ambiente basta ter o Docker 19.03.

```
docker-compose up -d
```

## Executar o ambiente para o Faust

Para este teste simples é importante que o ambiente do python possua todos os pacotes necessários.

Para criar um ambiente python com os pacotes necessários.

Criar o ambiente no Anaconda

```
conda create -n faust_env
conda activate faust_env
conda install python==3.8
```

##Configuração

Para executar o simulador é necessario instalar os pre-requisitos.

```
pip install -r requirements.txt
```

##Execução do projeto

- Execução do exemplo do projeto
```
python main-app.py worker
```

- Execução do exemplo do site
```
python faust-example.py worker
```