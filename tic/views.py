from django.shortcuts import render
from django.views.generic.edit import CreateView
from tic.models import Board
from tic.forms import BoardForm

# All of this is about to be a tablem, this is getting silly.		
wingroups=[	 {"zero": '', "four": '', "eight": ''}, {"two": '',"four": ' ',"six": ''},
		  {"three": ' ',"four": ' ',"five":''}, {"one": ' ',"four": ' ',"seven": ''},
		  {"zero": ' ',"one":'',"two":''},	{"six": ' ',"seven": ' ',"eight": ''},
		  {"zero": ' ',"three":'',"six": ' '},{"two": ' ',"five": ' ',"eight": ''}
	]

midgroups=[	["zero","one","three"],	["seven","eight","five"]
		["one","two","five"],["three","six","seven"],
	]		

xmoves=["four","zero","one","three","five","two","seven","six","eight"]

def updateWinGroups(pv):
	


def mkPvg(pv,grp):
	pvd={}
	for g in grp:
		 
		pvd[g]=(pv[g])
	#print 'pvd', pvd
		
	return pvd

def chkGrps(pv,grps,xo):
	for grp in grps:
		pvd=mkPvg(pv,grp)
		#pvg=mkPvg(pv,grp)
		
		pval=pvd.values()
		pk=pvd.keys(
		if pval.count(xo)==2 and pval.count(u'')==1:
		
			pick =pk[pval.index('')]
			print 'new pick', pick 
			return pick,pk
			


def findOpen(xmoves,pv):
	
	for xm in xmoves:
		if xm in pv.values():
			return xm

	return 'k'

def mkPick(pv):
	p='k'
	winners=['k'] 

	
	
	pick,winners=chkGrps(pv,wingroups,'x')
		print 'x', pick
		print 'wingroup', winners
	
	except:
		try:	
			pick,devnull= chkGrps(pv,wingroups,'o')
			print 'o' ,pick

		except:
			p=findOpen(xmoves,pv)
			
	return p,winners
	


class BoardCreate(CreateView):
	model = Board
	fields = '__all__'

def play(request):
   	
    	if request.method == 'GET':
		form=BoardForm()
		freshboard=1
		return render(request,'tic/board_form.html',{'form':form,'freshboard':1})	

    	if request.method == 'POST':
		post_values=request.POST.copy()
		form = BoardForm(post_values)
		
		pick,winners=mkPick(post_values)
		print 'pick--->', pick
		print 'winners --->',winners
		if form.is_valid():
            	
			return render(request,'tic/board_form.html',{'form':form,'pick':pick,'wingroup':winners})	

		
		return render(request,'tic/board_form.html',{'form':form,'pick':pick,'wingroup':winners})	
	
