# gloud-vision-plates

## config a chave e acessos.
1 - crie a chave da api cloud vision.
```
https://cloud.google.com/vision/docs/libraries?hl=pt-PT
```
2 - ative o projeto para que possa usar o cloud vision.
```
https://console.cloud.google.com/apis/library/vision.googleapis.com
```
3 - ative o projeto para que possa usar o cloud vision.
```
https://console.cloud.google.com/apis/library/vision.googleapis.com
```

4 - setar variavel de ambiente automaticamente. Altere o arquivo .env, coloque o caminho da chave que você criou.
```
GOOGLE_APPLICATION_CREDENTIALS="coloque o caminho da sua chave aqui"
```
 

## config projeto.
1 - entre na pasta do projeto usando o terminal/cmd.

2 - crie a virtualenv. Certifique-se que tenha uma versão do python acima da versão 3.6 e a biblioteca virtualenv esteja instada.
```
virtualenv -p python3 .venv
```

3 - ative a virtualenv.
```
--- linux ---
source .venv/bin/activate

--- windows --- 
\.venv\scripts\activate


referencia: https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/
```

4 - instale as dependências.
```
pip install -r requirements.txt
```
5 - execute o flask.
```
FLASK_APP=api/app.py FLASK_ENV="development" FLASK_DEBUG=1 flask run
```

## Teste a aplicação.
1 - entre no navegador.

2 - coloque a url do servidor. Por padrão é a url abaixo na barra de endereço e chame a aplicação.
```
127.0.0.1:5000 ou localhost:5000
```