# -*- coding: utf-8 -*-

from odoo import models, fields


class alumnos(models.Model):
     _name = 'alumnos.usuarios'
     _description = 'esta clase almacena alumnos'

     nombre = fields.Char()
     apellido = fields.Integer()
     cedula = fields.Float(compute="_value_pc", store=True)
     matricula = fields.Text()
     memo = fields.text ()
        
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
