from http import HTTPStatus

from flask import request, redirect
from flask_login import login_user, login_required, logout_user
from flask_restful import Resource

from utils import check_password, hash_password
from models.user import User


class LoginResource(Resource):

    def post(self):

        # Get user login information from form
        auth = request.form
        email = auth.get("email")
        password = auth.get("password")

        user = User.get_by_email(email=email)

        if not user or not check_password(password, user.password):
            return {"message": "email or password is incorrect"}, HTTPStatus.UNAUTHORIZED

        login_user(user, force=True)
        return redirect("/")


class LogoutResource(Resource):

    @login_required
    def get(self):

        logout_user()
        return redirect("/")


class RegisterResource(Resource):

    def post(self):

        # Get user register information from form
        auth = request.form

        username = auth.get("username")
        email = auth.get('email')
        non_hash_password = auth.get('password')

        if User.get_by_email(email):
            return {"message": "email already used"}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)
        user = User(username=username, email=email, password=password)
        user.save()

        return redirect("/login")
