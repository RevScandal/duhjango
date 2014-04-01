from django.forms import ModelForm
from tic.models import TicBoard



class TicBoardForm(ModelForm):
	class Meta:
		model = TicBoard

