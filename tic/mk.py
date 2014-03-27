				
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
n
def convGroup(group,form,xolist):
	xout=[]
	free=[]
	for g in group:
		c=form[g]
		if c in xolist:
			xout.append(c)
		else:
			free.append(g)
#	print 'free ', free
#	print 'xout', xout
	return xout,free			



def twoOfThree(group,form):
	pick='no'
	xo='no'	
	
	xout,free=convGroup(group,form,xolist)
	xout=list(set(xout))
	if len(xout)==1 and len(free)==1:
		return xout[0], free[0]	
	
	
	return xo,pick
				
def chkGroups(groups,form):
	xo='no'
	pick='no'
	for group in groups:
		xo,pick= twoOfThree(group,form)
		if xo != 'no':
#			print xo, pick
			return xo,pick
			
	return xo,pick		
	

def findOpen(xmoves,form):
	for move in xmoves:
		
		if form[move]=='':
			return move
	return 'no'		
		
	
def mkMove(form):
	allgroups=wingroups+midgroups
	xo,pick=chkGroups(allgroups,form)
	if xo !='no':
		return pick
		
	else:
		pick =findOpen(form)	
		return pick
		
