import os, sys, time, random, art


def author(incorrect_answer, author_err):

	random_author = random.randint(10000,99999)
	Art=text2art(f"{random_author}","slant")
	print(Art)

	while True:
		try:

			author_answer = input("answer> [2 q")

			if str(author_answer) == str(random_author):
				break


			else:
				incorrect_answer = incorrect_answer + 1
				
				if incorrect_answer == 3:
					with open(author_err) as author_error:
						exec(author_error.read())

				elif incorrect_answer != 3:
					print("Incorrect answer.")
					continue




		except KeyboardInterrupt:
			continue


os.system('cls' if os.name == 'nt' else 'clear')
author(incorrect_answer=0, author_err="branche//errors//input_errors//author_error.py")