health = 100

def dmg():
	global health 
	
	while health > 0:
		health -= 1
		print(health)
		
dmg()