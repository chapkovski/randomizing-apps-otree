from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import json
import random
from random import sample, choice
from . import error_funs, vars_for_template_functions

# You can add as many pages as needed in the beginning and in the end
# of shuffled sequence
class Letsgetstarted(Page):
    ...


# General class for shuffled page
class MyPage(Page):
    form_model = models.Player

    def get_template_stub(self):
        a = json.loads(self.player.newsetoftemplates)
        myidinpagesequence = page_sequence.index(type(self))
        return a[myidinpagesequence]

    def is_displayed(self):
        self.template_name = "Beliefs/" + self.get_template_stub() + ".html"
        return True

    def get_form_fields(self):
        if self.get_template_stub() in Constants.fields:
            return Constants.fields[self.get_template_stub()]
        else:
            return ['my_hidden_input']

    def vars_for_template(self):
        cur_var_for_template_fun = self.get_template_stub() + "_fun"
        # self.template_name = "Beliefs/" + self.get_template_stub() + ".html"
        if hasattr(vars_for_template_functions, cur_var_for_template_fun):
            return getattr(vars_for_template_functions, cur_var_for_template_fun)(self)
        else:
            print('NO VAR FOR TEMPLATE FUN for {} has been found...'.format(cur_var_for_template_fun))

    def error_message(self, values):
        curerror_fun = self.get_template_stub() + "_error_message"
        self.template_name = "Beliefs/" + self.get_template_stub() + ".html"
        if hasattr(error_funs, curerror_fun):
            return getattr(error_funs, curerror_fun)(self, values)
        else:
            print('NO ERROR FUN for {} has been found...'.format(curerror_fun))

# in this block we look at the length of the sequence of shuffled pages
# and create as many as dummy pages as necessary
howmanypages = len([i for s in Constants.templates for i in s])
shuffledpages = []
for i in range(howmanypages):
    tp = type('Page{}'.format(i), (MyPage,), dict())
    globals()['Page{}'.format(i)] = tp
    shuffledpages.append(tp)



page_sequence = [
    # Letsgetstarted,
]
page_sequence += shuffledpages
