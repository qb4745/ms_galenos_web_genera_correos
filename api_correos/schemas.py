# Westeros/stark/schemas.py
from ninja import ModelSchema
from api_correos.models import Reserva


class ReservaIn(ModelSchema):
    class Config:
        model = Reserva
        model_exclude = [
            "id",
        ]


class ReservaOut(ModelSchema):
    class Config:
        model = Reserva
        model_fields = "__all__"
