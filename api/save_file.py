from os import path, mkdir
from werkzeug.utils import secure_filename
from flask import request as Request


def valid_or_create_dir(diretory: str) -> str:
    """Irá verificar se um diretório já existe, caso não exista será criado.

    Args:
        path (str): Informe o nome da pasta onde deve ser salvo o arquivo.

    Returns:
        str: Irá retornar o caminho onde deve ser salvo o arquivo.
    """
    # montando o caminho completo onde será salvo o arquivo.
    dir_path = path.join(path.realpath("."), diretory)

    # vericar se o caminho não existe.
    if not path.exists(dir_path):
        # caso o caminho não exista, será criado.
        mkdir(path=dir_path)

    return dir_path


def valid_extension(filename: str) -> bool:
    """Valida se um nome de arquivo tem as extensões de imagem.

    Args:
        filename (str): Informe qual o nome do arquivo à ser validado.

    Returns:
        bool: Caso a extensão do arquivo seja valída irá retornar true, caso não false.
    """
    # imagem.png
    ALLOWED_EXTENSIONS = set(["png", "jpeg", "jpg"])
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(req: Request) -> list:
    """ essa função irá salvar todos os arquivos de imagem.

    Args:
        req (Request): informe a request onde está o arquivo.

    Returns:
        list: retornará uma lista contendo os path completos dos arquivos.
    """
    path_files = []
    # verifica se existe algum arquivo dentro do request.
    if not req.files or "file" not in req.files:
        return path_files
    # pega todos os nomes de arquivo em uma lista.
    files = req.files.getlist("file")
    # valida se os arquivos recebidos estão com as extensões aceitavéis.
    for file in files:
        # verificar se a variavel file não está vazia e valida qual a extensão da mesma.
        if not file and not valid_extension(file.filename):
            return path_files

    diretory = "images/"

    # esse for irá salvar cada arquivo valido dentro da pasta de imagem.
    for file in files:
        # verifica se a pasta imagem já existe ou cria caso não exista.
        path_valid = valid_or_create_dir(diretory=diretory)
        filename = file.filename
        # montando o caminho de cada imagem a partir da caminho da pasta imagem e nome do arquivo.
        # porém antes de concatenar, é feito a validação se o nome do arquivo é seguro, usando a função secure_filename.
        filepath = path.join(path_valid, secure_filename(filename))
        # por fim o arquivo é salvo dentro do caminho especificado.
        file.save(filepath)
        # para cada arquivo que tiver, será salvo o caminho dele dentro da lista que será retornado.
        path_files.append(filepath)
    # após salvar as imagens será retornado uma lista contendo o caminho completo de cada uma.
    return path_files
