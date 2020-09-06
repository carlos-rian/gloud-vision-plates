import io
import os
from google.cloud import vision
from google.cloud.vision import types
from dotenv import load_dotenv
from typing import ByteString

client = vision.ImageAnnotatorClient()


def open_image_and_instance_in_memory(filepath: str) -> ByteString:
    """ esse método irá abrir uma imagem em modo de leitura e converte-la para bytes em memória.

    Args:
        filepath (str): Informe qual o endereço está a placa do veiculo.

    Returns:
        ByteString: Retornar um objeto de bytes.
    """
    with io.open(filepath, "rb") as image_file:
        image_in_memory = image_file.read()
    return image_in_memory


def detect_image_in_api_vision(content: ByteString) -> list:
    """esse método irá consultar a api do google cloud vision, pegar onde tiver a placa e retornar uma lista.

    Args:
        content (ByteString): Infome a imagem convertida em bytes.

    Returns:
        list: retornará uma lista de strings apenas com as placas.
    """
    # o código abaixo irá converter os bytes de content para o tipo image.
    image = types.Image(content=content)
    # o response irá receber o resultado do client após subir a imagem para o google cloud.
    response = client.text_detection(image=image)
    placas = []
    for x in response.text_annotations:
        # o strip irá remover caracteres não printavéis e espaços no inicio e fim da string.
        # o replace irá substituir o caracter de - por nada
        description_text = x.description.strip().replace("-", "")
        # esse if irá verificar se a descrição tem apenas 7 caracteres, que é o tamanho de uma placa comum.
        if len(description_text) == 7:
            # irá add dentro da lista de placas, caso o resultado seja.
            placas.append(description_text)
    # deduplicar valores em uma lista
    placas = list(set(placas))
    return placas


def get_plates(filepath: str) -> list:
    """ essa função é responsável por invocar as outras funções e retornar as placas dentro de uma lista.

    Args:
        filepath (str): informe o caminho da imagem que deve ser lida e pega a placa.

    Returns:
        list: retornará uma lista contendo as placas caso exista. Caso não exista, retornará uma lista vazia.
    """
    content = open_image_and_instance_in_memory(filepath=filepath)
    placas = detect_image_in_api_vision(content=content)
    return placas
