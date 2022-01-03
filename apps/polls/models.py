from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    """Poll question."""
    question_text = models.CharField(_("Question text"), max_length=200)
    pub_date = models.DateTimeField(_("Publish date"))


class Choice(models.Model):
    """Answer choices for a question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(_("Choice text"), max_length=200)
    votes = models.IntegerField(default=0)
