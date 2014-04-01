from django.shortcuts import render
from django.views.generic.edit import CreateView
from tic.models import TicBoard
from tic.forms import TicBoardForm

# All of this is about to be a tablem, this is getting silly.		
wingroups=[	 {"a": '', "e": '', "i": ''}, 
		{"c": '',"e": ' ',"g": ''},
		  {"d": ' ',"e": ' ',"f":''}, 
		  {"b": ' ',"e": ' ',"h": ''},
		  {"a": ' ',"b":'',"c":''},	
		  {"g": ' ',"h": ' ',"i": ''},
		  {"a": ' ',"d":'',"g": ' '},
		  {"c": ' ',"f": ' ',"i": ''}
	]
			  

	
xmoves=["e","a","b","d","f","c","h","g","i"]

def updateWinGroups(pv):
	for group in wingroups:
		for k in group.keys():	
			group[k]=pv[k]


def chkGrps(grps,xo):
	for grp in grps:
		gvals=grp.values()
		gkeys=grp.keys()
		if gvals.count(xo)==2 and gvals.count('n')==1:
			pick =gkeys[gvals.index('n')]
			
			return pick,gkeys		
		else:
			pass		


def findOpen(xmoves,pv):
	for xm in xmoves:
		if pv[xm] =='n':
			return xm
	

def mkPick(pv):
	w=[]
	if chkGrps(wingroups,u'x'):
		p,w=chkGrps(wingroups,u'x')
		return p,w
	
	if chkGrps(wingroups,u'o'):
		p,blah=chkGrps(wingroups,u'o')	
		return p,w		
	else:
		p=findOpen(xmoves,pv)
				
		return p,w

	
	return p,w	
	

def play(request):
    	if request.method == 'GET':
		f=TicBoardForm()
		
		if f.is_valid():
			f.save()
			freshboard=1
			return render(request,'tic/ticboard_form.html',{'form':f,'freshboard':1})	
		
		return render(request,'tic/ticboard_form.html',{'form':f,'freshboard':1})	


	if request.method == 'POST':
		post_values=request.POST.copy()
		f = TicBoardForm(post_values)
		
		updateWinGroups(post_values)
		pick,winners=mkPick(post_values)
		if f.is_valid():
		
			return render(request,'tic/ticboard_form.html',{'form':f,'pick':pick,'wingroup':winners})	

		
		return render(request,'tic/ticboard_form.html',{'form':f,'pick':pick,'wingroup':winners})	

