from django.shortcuts import render
from django.views.generic.edit import CreateView

from tic.models import Board
from tic.forms import BoardForm

				
wingroups=[	["zero","one","two"], 
		["three","four","five"], 
		["six","seven","eight"],
		["zero","three","six"],
		["one","four","seven"],
		["two","five","eight"], 
		["zero","four","eight"], 
		["two","four","six"]  
	]
	
	
midgroups=[	["zero","one","three"],
		["one","two","five"],
		["three","six","seven"],
		["seven","eight","five"]
	]		
	
xmoves=["four","one","zero","three","five","two","seven","six","eight"]
xolist=[u'x',u'o']


def convGroup(group,pv,xolist):
	xout=[]
	free=[]
	for g in group:
		c=pv[g].strip()
		if c in xolist:
			xout.append(c)
		else:
			free.append(g)

	return xout,free			



def twoOfThree(group,pv):
	print group
	pick='no'
	xo='no'	
	xolist=[u'x',u'o']
	xout,free=convGroup(group,pv,xolist)
	print xout
	print free, 'free'
	xout=list(set(xout))
	if len(xout)==1 and len(free)==1:
		return xout[0], free[0]	
	
	
	return xo,pick
				
def chkGroups(groups,pv):
	xo='no'
	pick='no'
	for group in groups:
		xo,pick= twoOfThree(group,pv)
		print pick, 'no pick'
		if xo != 'no':
			print 'chkGroups'
			print xo, pick
			
			return xo,pick
			
	return xo,pick		
	

def findOpen(xmoves,pv):
	for move in xmoves:
		print pv[move]
		
		if pv[move] in xolist:
			xmoves.remove(move)
		else:	
			print move
			return move
		
		
	
def mkMove(pv):
	allgroups=wingroups+midgroups
	xo,pick=chkGroups(wingroups,pv)
	
	if xo !='no':
		return pick
	else:
		pick=findOpen(xmoves,pv)
		return pick	
	




class BoardCreate(CreateView):
	model = Board
	fields = '__all__'

def play(request):
   	print request.method 
    	if request.method == 'GET':

	
		form=BoardForm()
	

    	if request.method == 'POST':
		post_values=request.POST.copy()
		pick=mkMove(post_values)
		print 'pick returned', pick		  
		
		post_values[pick]=u'x'
		
    		form = BoardForm(post_values)
		
		
		
		if form.is_valid():
            		board = form.save()
            		board.save()
	
	return render(request,'tic/board_form.html',{'form':form})	


	
