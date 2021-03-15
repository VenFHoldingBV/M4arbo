from odoo import fields, models
from datetime import datetime, timedelta


class InheritPartner(models.Model):
    _inherit = "res.partner"

    def update_all_test_center(self):
        """
            This method will filter out the partners which company type will be company.
            And add all the covid test center in the test center column.
        """
        for partner in self.filtered(lambda p: p.company_type != 'person'):
            appointment_centre_ids = self.env['calendar.appointment.type'].search([]).ids
            partner.appointment_centre_ids = [(6, 0, appointment_centre_ids)] 

    def calculate_age(self):
        """
            Calculate the age based on the date of birth and the today's date.
        """
        for partner_rec in self:
            partner_rec.age = 0
            if partner_rec.dob:
                today = datetime.now().date()
                age = today.year - partner_rec.dob.year - (
                    (today.month, today.day) < (partner_rec.dob.month, partner_rec.dob.day))
                partner_rec.age = age


    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", placeholder="Gender")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="calculate_age")
    appointment_centre_ids = fields.Many2many('calendar.appointment.type', string='Select Test Centre')

    def appointmet_verify_check(self, Partner, date_start):
        """ verify appointment validity """
        data_dict = {}
        message = ''
        date_start = date_start - timedelta(days=14)
        if Partner:
            partner_report = self.env['event.report'].sudo().search([('partner_id', '=', Partner.id),
                                                                     ('create_date', '>=', date_start),
                                                                     ('state', '=', 'positive')])
            if partner_report:
                message += "You are Restricted to test for 14 days since your result was Positive."
                data_dict['message'] = message
                return data_dict

            domain = [('state', '=', 'open'),
                      ('appointment_type_id', '!=', False),
                      ('partner_ids', 'in', Partner.ids)]
            partner_event = self.env['calendar.event'].sudo().search(domain)
            if self.env.user.partner_id.id == Partner.id:
                partner_event = partner_event.filtered(lambda event: len(event.partner_ids) == 1)
            if partner_event:
                message += "The Appointment is already scheduled for you. \n " \
                                    "You can Cancel the prior appointment and reschedul it again."
                data_dict['message'] = message
                return data_dict

        return data_dict
