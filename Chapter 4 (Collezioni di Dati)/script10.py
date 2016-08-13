###########################################################################################
#
# David Canino, August 2016
#
# Basic management of the 'dictonaries' (hashing tables) in the Python Language
#
# scritp10.py script
###########################################################################################
d0={}
print("\n\tNew dictionary 'd0'=",d0," of type ",type(d0))
print("\tThe new dictionary 'd0' contains",len(d0),"associations\n")
d1={ "one" : 1, "two" : 2, "three" : 3 }
print("\tNew dictionary 'd1'=",d1," of type ",type(d1))
print("\tThe new dictionary 'd1' contains",len(d1),"associations")
ll1=d1.keys()
vl1=d1.values()
pl1=d1.items()
print("\tThe collection of the keys in the dictionary 'd1':",ll1,"with type",type(ll1))
print("\tThe collection of the values in the dictionary 'd1':",vl1,"with type",type(vl1))
print("\tThe collection of the pairs <key/value> in the dictionary 'd1':",pl1,"with type",type(pl1),"\n")

d2=dict( { "four" : 4, "five" : 5, "six" : 6 } )
print("\tNew dictionary 'd2'=",d2," of type ",type(d2))
print("\tThe new dictionary 'd2' contains",len(d2),"associations")
ll2=d2.keys()
vl2=d2.values()
pl2=d2.items()
print("\tThe collection of the keys in the dictionary 'd2':",ll2,"with type",type(ll2))
print("\tThe collection of the values in the dictionary 'd2':",vl2,"with type",type(vl2))
print("\tThe collection of the pairs <key/value> in the dictionary 'd2':",pl2,"with type",type(pl2),"\n")

d3=dict( { ("seven",7), ("eight",8), ("nine",9), ("ten",10) })
print("\tNew dictionary 'd3'=",d3," of type ",type(d3))
print("\tThe new dictionary 'd3' contains",len(d3),"associations")
ll3=d3.keys()
vl3=d3.values()
pl3=d3.items()
print("\tThe collection of the keys in the dictionary 'd3':",ll3,"with type",type(ll3))
print("\tThe collection of the values in the dictionary 'd3':",vl3,"with type",type(vl3))
print("\tThe collection of the pairs <key/value> in the dictionary 'd3':",pl3,"with type",type(pl3),"\n")

d4=dict(zip({"one","three","five","seven","nine" },{1.0,3.0,5.0,7.0,9.0}))
print("\tNew dictionary 'd4'=",d4," of type ",type(d4))
print("\tThe new dictionary 'd4' contains",len(d4),"associations")
ll4=d4.keys()
vl4=d4.values()
pl4=d4.items()
print("\tThe collection of the keys in the dictionary 'd4':",ll4,"with type",type(ll4))
print("\tThe collection of the values in the dictionary 'd4':",vl4,"with type",type(vl4))
print("\tThe collection of the pairs <key/value> in the dictionary 'd4':",pl4,"with type",type(pl4),"\n")

print("\tThe dictionary 'd1' contains",len(d1),"associations")
d1.clear()
print("\tThe dictionary 'd1' contains",len(d1),"associations after its cleaning\n")

print("\tThe dictionary 'd2' contains",len(d2),"associations")
d2.clear()
print("\tThe dictionary 'd2' contains",len(d2),"associations after its cleaning\n")

print("\tThe dictionary 'd3' contains",len(d3),"associations")
d3.clear()
print("\tThe dictionary 'd3' contains",len(d3),"associations after its cleaning\n")

print("\tThe dictionary 'd4' contains",len(d4),"associations")
d4.clear()
print("\tThe dictionary 'd4' contains",len(d4),"associations after its cleaning\n")