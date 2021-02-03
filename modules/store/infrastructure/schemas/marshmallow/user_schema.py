# from product_hub.models import User
# from product_hub.extensions import ma, db
#
#
# class UserSchema(ma.SQLAlchemyAutoSchema):
#     ma.uuid
#     id = ma.Int(dump_only=True)
#     password = ma.String(load_only=True, required=True)
#
#     class Meta:
#         model = User
#         sqla_session = db.session
#         load_instance = True
#         exclude = ("_password",)
