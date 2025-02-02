from cohere import Client

co = Client(api_key="")



async def predict(data: dict) -> dict:
    """
    Predict the Disease of a patient
    """

    return {"message": "pong"}
