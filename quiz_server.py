import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address='127.0.0.1'
port= 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

questions=[
    "What is the Italian word for PIE? \n a.mozarella \n b.pasty \n c.patty \n d.pizza",
    "Water boils at 212 units at which scale? \n a.fahrenheit \n b.celsius \n c.rankine \n d.kelvin",
    "Which sea creature has three hearts \n a.dolphin \n b.octopus \n c.walrus \n d.seal",
    "Who was the character famous in our chilhood rhymes associated with a lamb? \n a.mary \n b.jack \n c.johnny \n d.mukesh",
    "How many bones does an sdult human have? \n a.206 \n b.208 \n c.201 \n d.196",
    "How many wonders are there in the world? \n a.7 \n b.8 \n c.10 \n.4",
    "What element does not exist? \n a.Xf \n b.Re \n c.Si \n d.Pa",
    "How many states are there in india? \n a.24 \n b.29 \n c.30 \n d.31",
    "Who invented the telephone? \n a.A.G Bell \n b.John Wick \n c.Thomas Edison \n d.G Marconi",
    "Who is Loki? \n a.God of Thunder \n b.God of Dwarves \n c.God of mischief \n d.God of Gods",
    "Who was the first indian female astronut? \n a.Sunita William \n b.Kapana Chawala \n c.None of the above \n d.both of them",
    "What is the smallest continent? \n a.Asia \n b.Anatarctica \n.Africa \n c.Australia",
    "The beaver is the national emblem of which country? \n a.Zimbabwe \n b.Iceland \n c.Argentina \n d.Canada",
    "How many players are on the field in baseball? \n a.6 \n b.7 \n c.9 \n d.8",
    "Hg stands for? \n a.Mercury \n b.Hulgerium \n c.Argenine \n d.Halfnium",
    "Who gifted the statue of Liberty to the USA? \n a.Brazil \n b.France \n c.Wales \n d.Germany",
    "Which planet is closest to the sun? \n a.Mercury \n.Pluto \n c.Earth \n d.Venus"
]

answers = ['d','a','b','a','a','a','a','b','a','c','b','d','d','c','a','b','a']

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()

    def clientthread(conn):
        score=0
        conn.send("Welcome to this quiz game!".encode('utf-8'))
        conn.send("You will receive a question. The answer to that question should be one of a,b,c,d")
        conn.send("Good Luck!\n\n".encode('utf-8'))
        index, question,answer =get_random_question_answer(conn)

        while True:
            try:
                message = conn.recv(2048).decode('utf-8')
                if message:
                    if message.lower() == answer:
                        score += 11
                        conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                    else:
                        conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                    remove_question(index)
                    index,question,answer ==get_random_question_answer(conn)
                else:
                    remove(conn)     
            except:
                continue
    def remove_question(index):
        questions.pop(index)
        answers.pop(index)

    def get_random_question_answer(conn):
        random_index = random.randint(0,len(questions)-1)
        random_questions = questions[random_index]
        random_answer = answers[random_index]
        conn.send(random_questions.encode('utf-8'))
        return random_index,random_questions,random_answer
    
    
    