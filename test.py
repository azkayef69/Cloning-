def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;97m(50000MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
