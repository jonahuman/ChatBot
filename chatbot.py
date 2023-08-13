#---------------------------------------
#    Hecho por: Flerkendroid            |                                          
#    Versión: 0.0.1v (Beta)             |
#    Fecha: 2023-08-12                  |
#    País: Región Metropolitana,        |
#          Santiago de Chile            |
#    Horario: GTM-4                     |
#    Hora: 18:09:11                     |                                      

import requests
import json

# Configura la URL del servidor de Rasa
RASA_API_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"

def get_order_status(order_id):
    # Simula obtener el estado del pedido desde la API de PedidosYA
    # Reemplaza esto con una solicitud real a la API
    return "Pendiente" or "Entregado" or "En camino"

def get_delivery_details(order_id):
    # Simula obtener los detalles de entrega desde la API de PedidosYA
    # Reemplaza esto con una solicitud real a la API
    return "Detalles de entrega no disponibles" or "Detalles de entrega disponibles"

def chat_bot(user_input):
    response = ""

    if "hola" in user_input:
        response = "¡Hola! ¿Cómo estás? Soy tu asistente virtual y estoy aquí para ayudarte."
    elif "estado del pedido" in user_input:
        order_id = user_input.split()[-1]
        order_status = get_order_status(order_id)
        response = f"El estado del pedido {order_id} es: {order_status}"
    elif "detalles de entrega" in user_input:
        order_id = user_input.split()[-1]
        delivery_details = get_delivery_details(order_id)
        response = f"Los detalles de entrega para el pedido {order_id} son: {delivery_details}"
    elif "adiós" in user_input or "chao" in user_input or "hasta luego" in user_input:
        response = "¡Hasta luego! Espero haberte ayudado. ¡Vuelve pronto!"
    else:
        try:
            # Llamada a la API de Rasa para obtener una respuesta
            payload = {
                "message": user_input
            }
            rasa_response = requests.post(RASA_API_ENDPOINT, json=payload)
            rasa_data = rasa_response.json()

            if rasa_data and isinstance(rasa_data, list) and len(rasa_data) > 0 and "text" in rasa_data[0]:
                response = rasa_data[0]['text']
            else:
                response = "Lo siento, no entendí tu pregunta o algo salió mal."
        except Exception as e:
            response = "Ocurrió un error al procesar tu solicitud. Por favor, inténtalo de nuevo más tarde."

    print("Chat Bot:", response)

if __name__ == "__main__":
    # Carga el contenido del archivo JSON en una variable
    with open('openapi.json', 'r') as json_file:
        data = json.load(json_file)

    print("Chat Bot: ¡Hola! Soy tu asistente virtual de Cafetería. ¿En qué puedo ayudarte hoy?")
    while True:
        user_input = input("Tú: ")
        if "adiós" in user_input or "chao" in user_input or "hasta luego" in user_input:
            print("Chat Bot: ¡Hasta luego! Espero haberte ayudado. ¡Vuelve pronto!")
            break

        chat_bot(user_input)
