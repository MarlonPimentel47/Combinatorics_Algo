from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FieldList, FormField, TextField
from wtforms.validators import DataRequired, NumberRange


class StartingForm(FlaskForm):

    number_of_vars = IntegerField('Enter number of variables', validators=[DataRequired(),
                                                                           NumberRange(min=1, max=11)])

    submit = SubmitField('Submit')


class ProblemForm(FlaskForm):

    var1 = IntegerField('x1<=', validators=[DataRequired(), NumberRange(min=1, max=1000)])

    var2 = IntegerField('x2<=', validators=[DataRequired(), NumberRange(min=1, max=1000)])

    var3 = IntegerField('x3<=', validators=[DataRequired(), NumberRange(min=1, max=1000)])

    total = IntegerField('x1 + x2 + x3 = ', validators=[DataRequired(), NumberRange(min=1, max=10000)])

    submit = SubmitField('Calculate # of solutions')


#  class VariableForm(FlaskForm):

#    limit = IntegerField('x', validators=[DataRequired(), NumberRange(min=1, max=100)])


#  class ProblemForm(FlaskForm):

#    limits = FieldList(FormField(VariableForm), min_entries=1)

#    total_value = IntegerField('Total', validators=[DataRequired(), NumberRange(1, 100000)])

#    submit = SubmitField('Calculate # of solutions')


#  class AddressEntryForm(FlaskForm):
#    name = TextField()


#  class AddressesForm(FlaskForm):
#    """A form for one or more addresses"""
#    addresses = FieldList(FormField(AddressEntryForm), min_entries=1)
