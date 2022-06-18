# -*- coding: utf-8 -*-
###############################################################################
#
#    Al Akhawayn University in Ifrane -- AUI
#    Copyright (C) 2022-TODAY AUI(<http://www.aui.ma>).
#
#    Author: Omar Iraqi Houssaini | https://github.com/oiraqi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import string


class Student(models.Model):
    _name = 'a3.student'
    _inherits = {'res.partner': 'partner_id'}
    _inherit = 'a3.school.owned'
    _description = 'Student'
    _sql_constraints = [('sid_ukey', 'unique(sid)', 'Student ID already exists')]

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    sid = fields.Char(string='Identifier', required=True)    
    attendance_mode = fields.Selection(string='Attendance Mode', selection=[('f2f', 'Face To Face'), ('online', 'Online'),], default='f2f', required=True)
