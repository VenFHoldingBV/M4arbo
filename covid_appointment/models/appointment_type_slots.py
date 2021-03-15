from odoo import models


class InheritAppointmentType(models.Model):
    _inherit = "calendar.appointment.type"

    def generate_time_slots(self):

        return {
            'name': "Appointment Type Slot Configuration",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'appointment.slot.wizard',
            'target': 'new',
            'context': {'default_appointment_id': self.id}
        }
