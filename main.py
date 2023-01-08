import sys
import random
import webbrowser
import colorama

symbols = "qwertyuiopasdfghjklzxcvbnm1234567890"
auto_open = False

def main():
	global auto_open
	
	try:
		amount = int(sys.argv[sys.argv.index("-a") + 1])
	except ValueError:
		print(colorama.Fore.RED + "[ERROR] Specify an amount with the -a parameter!")
		raise SystemExit(-1)
	except IndexError:
		print(colorama.Fore.RED + "[ERROR] Specify a value!")
		raise SystemExit(-1)

	try:
		if sys.argv[sys.argv.index("-o")]:
			auto_open = True
	except ValueError:
		pass

	[link_action(f"https://prnt.sc/{i}") for i in generate(amount)]

def link_action(link):
	global auto_open
	print(link)

	if auto_open:
		webbrowser.open(link)

def generate(amount: int = 0) -> list:
	result = []

	for i in range(amount):
		tmp = ""
		for i in range(6): # 6 - amount of symbols
			tmp += random.choice(symbols)

		result.append(tmp)

	return result


if __name__ == "__main__":
	main()
