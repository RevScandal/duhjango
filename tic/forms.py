from django.forms import ModelForm
from tic.models import Board

class BoardForm(ModelForm):
	class Meta:
		model = Board
