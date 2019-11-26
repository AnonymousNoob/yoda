# -*- mode: python3 -*-
import argparse

__author__ = "Praveen M"
__version__ = "0.1.0"


"""
Todo:
	Add class and share source and destination strings and opetations
	Add file parser method
"""


CHARMAP = {"DEL":'-',"INS":'+'}
operations = {}
def print_ses(e, s1, s2):
	"""
	Print Shortest Edit Script

	Scope:
		Color Code DEL and INS operations
		Transpose diff tree over source text
		Output for Merge Diff
	"""
	# Todo: Write UnitTest and revisit Data model
	global CHARMAP, operations # Remove this and make is an instance
	c = 0
	for idx,i in enumerate(s1):
		if idx in operations:
			for op in operations[idx]:
				if op == 'INS' and c>1:
					print (" ",s1[c+idx-1])
					c = 0            
				print (CHARMAP[op], s1[idx] if op == 'DEL' else s2[idx])
				if op == 'DEL':
					c += 1
		else:
			print (" ",i)


def diff(e, f, i=0, j=0):
	"""
	Implements Modified Myer's Algorithm to identify diff between to given text
	Complexity: O(N) [previously, O(ND)]

	Scope:
		Read Two files/ Different versions of files to compare changes and 
		identify 'delta' over each string.
		Oppossed to xdiff used in git, implement myer's algorithm to breakdown
		better diff to ease development and merge
		Reduce Myer's O(ND) complexity
		Pretty Print readable Diff

	"""
	# Todo: Tidy returns, recursions
	global operations # Remove this and make is an instance
	N,M,L,Z = len(e),len(f),len(e)+len(f),2*min(len(e),len(f))+2
	if N > 0 and M > 0:
		w,g,p = N-M,[0]*Z,[0]*Z
		for h in range(0, (L//2+(L%2!=0))+1):
			for r in range(0, 2):
				c,d,o,m = (g,p,1,1) if r==0 else (p,g,0,-1)
                # does graph even work this way?           
				for k in range(-(h-2*max(0,h-M)), h-2*max(0,h-N)+1, 2):
					a = c[(k+1)%Z] if (k==-h or k!=h and c[(k-1)%Z]<c[(k+1)%Z]) else c[(k-1)%Z]+1
					b = a-k
					s,t = a,b
					while a<N and b<M and e[(1-o)*N+m*a+(o-1)]==f[(1-o)*M+m*b+(o-1)]:
						a,b = a+1,b+1
					c[k%Z],z=a,-(k-w)
					if L%2==o and z>=-(h-o) and z<=h-o and c[k%Z]+d[z%Z] >= N:
						D,x,y,u,v = (2*h-1,s,t,a,b) if o==1 else (2*h,N-a,M-b,N-s,M-t)
						if D > 1 or (x != u and y != v):
							return diff(e[0:x],f[0:y],i,j)+diff(e[u:N],f[v:M],i+u,j+v)
						elif M > N:
							return diff([],f[N:M],i+N,j+N)
						elif M < N:
							return diff(e[M:N],[],i+M,j+M)
						else:                             
							return []
	elif N > 0: 
		for n in range(N):
			if i+n not in operations:
				operations[i+n] = []
			operations[i+n].append('DEL')
		return ""
	else:
		for n in range(M):
			if j+n not in operations:
				operations[j+n] = []
			operations[j+n].append('INS')
	return ""

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Output Diff between text.')
	parser.add_argument('src', metavar='source', help='source text')	
	parser.add_argument('dest', metavar='dest', help='destination text')		
	args = parser.parse_args()
	ses = diff(args.src, args.dest)
	print_ses(ses, args.src, args.dest)
	
