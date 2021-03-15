from odoo import fields, models


class EventReport(models.Model):
    _name = "event.report"
    _description = "Calendar Event Report"
    _order = "id desc"
    _rec_name = "report_filename"

    event_report = fields.Binary(string="Report")
    report_filename = fields.Char()
    calendar_event_id = fields.Many2one(
        'calendar.event', string="Event", ondelete='cascade', copy=False)
    partner_id = fields.Many2one('res.partner', copy=False, string="Partner")
    state = fields.Selection([('positive', 'Positive'),
                              ('negative', 'Negative')],
                              default="positive",
                              string="State")
