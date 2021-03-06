# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Advanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Avanzosc Grouping Invoices",
    "version": "1.0",
    "depends": ["account"],
    "author": "Avanzosc S.L.",
    "category": "Custom Modules",
    "description": """
        Avanzosc Custom Modules. This module creates two new entries. 
        One in customer invoices called ALL CUSTOMER INVICE, and another one in supplier invoices, called ALL SUPPLIER INVOICE.
            """,
    "init_xml": ['account_invoice_ext_view.xml',
                 ],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'active': False,
}