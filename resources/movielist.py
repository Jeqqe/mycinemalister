from flask import make_response, render_template
from flask_restful import Resource

# Nää on perjaattees kyl iha normi view pageja et ne vois kyl olla tuol noitte muitte pagejekaa emt.
# jos haluut siirtää nii siit vaa.
class CreateList(Resource):
    def get(self, username):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('create_list.html', username=username), 200, headers)


class EditList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit_list.html'), 200, headers)


class ViewList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('view_list.html'), 200, headers)