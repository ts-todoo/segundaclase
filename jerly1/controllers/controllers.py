# -*- coding: utf-8 -*-
# from odoo import http


# class Jerly1(http.Controller):
#     @http.route('/jerly1/jerly1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jerly1/jerly1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jerly1.listing', {
#             'root': '/jerly1/jerly1',
#             'objects': http.request.env['jerly1.jerly1'].search([]),
#         })

#     @http.route('/jerly1/jerly1/objects/<model("jerly1.jerly1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jerly1.object', {
#             'object': obj
#         })
