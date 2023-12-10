from django.shortcuts import get_object_or_404
from ninja import Router, Query
from api_correos.schemas import ReservaIn, ReservaOut
from api_correos.models import Reserva
from datetime import datetime

import requests
from django.core.mail import send_mail

router = Router()


""" @router.get("/pacientes")
def send_emails(request, date: str = Query(...)):
    api_url = f"http://127.0.0.1:8001/galenos/web/pacientes/reservas/lista?date={date}"

    # Make API request
    response = requests.get(api_url)
    reservations_data = response.json()

    # Deserialize the data
    reservations = [Reserva(**reserva) for reserva in reservations_data]

    # Send emails
    for reserva in reservations:
        subject = "Reservation Reminder"
        message = f"You have a reservation on {reserva.fecha} at {reserva.hora_inicio}."
        recipient = "combustion.2@gmail.com"  # Replace with the actual email address
        send_mail(subject, message, "combustion.1@gmail.com", [recipient])

    return {"message": "Emails sent successfully"} """


""" @router.get("/pacientes")
def send_emails(request, date: str = Query(...)):
    api_url_reservas = (
        f"http://127.0.0.1:8001/galenos/web/pacientes/reservas/lista?date={date}"
    )

    # Make API request for reservations
    response_reservas = requests.get(api_url_reservas)
    reservations_data = response_reservas.json()

    # Deserialize the data
    reservations = [Reserva(**reserva) for reserva in reservations_data]

    # Send emails
    for reserva in reservations:
        # Make API request for patient information
        api_url_paciente = (
            f"http://127.0.0.1:7999/galenos/web/pacientes/lista/{reserva.id_paciente}"
        )
        response_paciente = requests.get(api_url_paciente)
        paciente_data = response_paciente.json()

        # Extract patient email
        patient_email = paciente_data.get("email", None)
        patient_nombre = paciente_data.get("nombres", None)
        patient_apellido = paciente_data.get("apellidos", None)

        # Check if the email is available
        if patient_email:
            subject = "Recordatorio de reserva Centro Médico Galenos"
            message = f"Estimado/a {patient_nombre} {patient_apellido}.\nTiene una reserva el dia {reserva.fecha} a las {reserva.hora_inicio} en Centro Médico Galenos, Av. Siempre Viva 742, Viña Del Mar.\nFavor de asistir puntualmente."
            recipient = patient_email
            send_mail(subject, message, "combustion.1@gmail.com", [recipient])

    return {"message": "Emails sent successfully"} """


@router.post("/pacientes")
def send_emails(request, date: str = Query(...)):
    api_url_reservas = (
        # f"http://127.0.0.1:8001/galenos/web/pacientes/reservas/lista?date={date}"
        f"http://44.221.17.219:8000/galenos/web/pacientes/reservas/lista?date={date}"
    )

    # Make API request for reservations
    response_reservas = requests.get(api_url_reservas)
    reservations_data = response_reservas.json()

    # Deserialize the data
    reservations = [Reserva(**reserva) for reserva in reservations_data]

    # Send emails
    for reserva in reservations:
        # Make API request for patient information
        api_url_paciente = (
            # f"http://127.0.0.1:7999/galenos/web/pacientes/lista/{reserva.id_paciente}"
            f"http://3.234.53.156:8000/galenos/web/pacientes/lista/{reserva.id_paciente}"
        )
        response_paciente = requests.get(api_url_paciente)
        paciente_data = response_paciente.json()

        # Extract patient email
        patient_email = paciente_data.get("email", None)
        patient_nombre = paciente_data.get("nombres", None)
        patient_apellido = paciente_data.get("apellidos", None)

        # Check if the email is available
        if patient_email:
            subject = "Recordatorio de reserva Centro Médico Galenos"
            message = f"Estimado/a {patient_nombre} {patient_apellido}.\nTiene una reserva el dia {reserva.fecha} a las {reserva.hora_inicio} en Centro Médico Galenos, Av. Siempre Viva 742, Viña Del Mar.\nFavor de asistir puntualmente."
            recipient = patient_email
            send_mail(subject, message, "combustion.1@gmail.com", [recipient])

    return {"message": "Emails sent successfully"}
