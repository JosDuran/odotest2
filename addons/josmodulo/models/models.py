# -*- coding: utf-8 -*-
from odoo import models, fields, api,


class CertInstructor(models.Model):
    _name = 'instructor'
    _descripcion = 'Registro Instructores'


    name = fields.Char(string='Nombre', required=True )
    date = fields.Date(string='Fecha', required=True)
    card = fields.Many2one('fleet.vehicle.model.brand')
    model = fields.Char(string='Modelo')
    patente = fields.Char(string='Patente')