from django.db import models


class Reserva(models.Model):
    id_paciente = models.IntegerField()
    id_medico = models.IntegerField()
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    def __str__(self):
        return f"Reserva #{self.id} - Paciente: {self.id_paciente}, Medico: {self.id_medico}, Fecha: {self.fecha}, Hora Inicio: {self.hora_inicio}, Hora Termino: {self.hora_termino}"
