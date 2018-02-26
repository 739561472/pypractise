from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from models import Admin, Tag


# tags = Tag.query.all()


class LoginForm(FlaskForm):
    """管理员登陆表单"""
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    submit = SubmitField(
        "登陆",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！ ")


class TagForm(FlaskForm):
    name = StringField(
        label='名称',
        validators=[
            DataRequired("请输入标签！")
        ],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label='片名',
        validators=[
            DataRequired("请输入片名！")
        ],
        description="片名",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入片名！"
        }
    )
    url = FileField(
        label='文件',
        validators=[
            DataRequired("请输入文件！")
        ],
        description="文件",
    )
    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired("请输入简介！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "id": "input_info",
            "rows": 10
        }
    )
    logo = FileField(
        label='封面',
        validators=[
            DataRequired("请输入封面！")
        ],
        description="封面",
    )
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请输入星级！")
        ],
        coerce=int,
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
        description="星级",
        render_kw={
            "class": "form-control",
            "id": "input_star",
        }
    )
    # tag_id = SelectField(
    #     label="标签",
    #     validators=[
    #         DataRequired("请输入标签！")
    #     ],
    #     coerce=int,
    #     choices=[(v.id, v.name) for v in tags],
    #     description="标签",
    #     render_kw={
    #         "class": "form-control",
    #         "id": "input_tag_id",
    #     }
    # )
    area = StringField(
        label='地区',
        validators=[
            DataRequired("请输入地区！")
        ],
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区！"
        }
    )
    length = StringField(
        label='片长',
        validators=[
            DataRequired("请输入片长！")
        ],
        description="片长",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片长！"
        }
    )
    release_time = StringField(
        label='上映时间',
        validators=[
            DataRequired("请选择上映时间！")
        ],
        description="上映时间",
        render_kw={
            "class": "form-control",
            "id": "input_release_time",
            "placeholder": "请选择上映时间！"
        }
    )
    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

