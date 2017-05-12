from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json


author = 'Philipp Chapkovski, University of Zurich'

doc = """
Shuffling subsets of pages randomly for each user.
Each page that is a part of randomized apps, can have its own
vars_for_template function and custom errors function.
To pass the variables you need to define a function in a file:
vars_for_template_functions.py, with the following rule:
<NAME_OF_THE_PAGE>_fun.
for example if you define a page called smth_page, to pass the variables
to its template you need to define a funciton there:
smth_page_fun(page). See example in vars_for_template_functions.py.

If you need a custom error function, you should do the same with the file
error_funs.py (see example there.)
"""


class Constants(BaseConstants):
    name_in_url = 'Beliefs'
    players_per_group = None
    num_rounds = 1
    # 'apps' are just set of pages.
    # 'fields' is a dictionary that associates each page with a set of fields

    app1 = ['App1Page1', 'App1Page2', 'App1Page3']
    app2 = ['App2Page1', 'App2Page2', 'App2Page3']
    app3 = ['App3Page1', 'App3Page2', 'App3Page3']
    # the order of the apps in templates doesn't matter because we shuffle the
    # apps anyway in the beginning of the session
    templates = [app1, app2, app3]

    fields = {
                "App1Page2": ["FieldForA1P2"],
                "App1Page3": ["FieldForA1P3"],
                "App2Page2": ["FieldForA2P2"],
                "App2Page3": ["FieldForA2P3"],
                "App3Page2": ["FieldForA3P2"],
                "App3Page3": ["FieldForA3P3"],
            }


class Subsession(BaseSubsession):

    def before_session_starts(self):
        # that is the part where we shuffle the order of apps and then
        # flatten this list of lists to pass the order to the field in
        # Player's model. The field where the order is stored is
        # newsetoftemplates
        for p in self.get_players():
            p.newsetoftemplates = Constants.templates
            random.shuffle(p.newsetoftemplates)
            p.newsetoftemplates = \
                    json.dumps([item for sublist in p.newsetoftemplates for item in sublist])
            print(p.newsetoftemplates)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # this is the field where the order of pages subsets (aka apps) is stored
    newsetoftemplates = models.TextField(null=True)
    # a 'lifehack' to avoid the errors if the page has no fields at all
    my_hidden_input = models.PositiveIntegerField()

    # the fields can be absolutely any; these are just for demonstration purposes
    FieldForA1P2 = models.IntegerField(verbose_name="Question for app 1, page 2. Please insert ODD number")
    FieldForA1P3 = models.CharField(verbose_name="Question for app 1, page 3")
    FieldForA2P2 = models.CharField(verbose_name="Question for app 2, page 2")
    FieldForA2P3 = models.CharField(verbose_name="Question for app 2, page 3")
    FieldForA3P2 = models.CharField(verbose_name="Question for app 3, page 2")
    FieldForA3P3 = models.CharField(verbose_name="Question for app 3, page 3")
