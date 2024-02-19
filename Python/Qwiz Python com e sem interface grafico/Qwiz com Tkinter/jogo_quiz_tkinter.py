
from tkinter import *
import random
from tkinter import messagebox as mb
import json
 
class Quiz:

    def __init__(self):
         
        self.q_no=0
    
        self.display_title()
        self.display_question()
        self.display_subtitle()
        
        self.opt_selected=IntVar()
        
        self.opts=self.radio_buttons()
        
        self.display_options()
        self.buttons()
        
        self.data_size=len(question)
        self.correct=0
 
    def display_result(self):
         
        wrong_count = self.data_size - self.correct
        correct = f"Respostas Certas: {self.correct}"
        wrong = f"Respostas Erradas: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Pontuação: {score}%"
        mb.showinfo("Resultado Final", f"{result}\n{correct}\n{wrong}")
 
    def check_ans(self, q_no):
         
        if self.opt_selected.get() == answer[q_no]:
            return True
 
    def next_btn(self):
         
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
         
        if self.q_no==self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()
 
    def buttons(self):
         
        next_button = Button(gui, text="Proxima Questão",command=self.next_btn,
        width=12,bg="blue",font=("ariel",16,"bold"))
        next_button.place(x=320,y=360)
         
        quit_button = Button(gui, text="Sair", command=gui.destroy,
        width=5,bg="black",font=("ariel",16," bold"))
        quit_button.place(x=708,y=2)
 
    def display_options(self):

        val=0
        self.opt_selected.set(0)
         
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
            
    def display_question(self):
         
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=140)
 
    def display_title(self):
         
        title = Label(gui, text="QUIZ - As 50 Capitais de Cidades Europeias",
        width=50, bg="orange",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def display_subtitle(self):

        sub_line1 = Label(gui, text="Seja bem-vindo ao Jogo das 50 Capitais Europeias, responda as questões e por cada questão correta recebe um ponto, no final",
        width=200,fg="black", font=("ariel", 12, "bold"))
        sub_line1.place(x=-500, y=50)

        sub_line2 = Label(gui, text="será apresentado o seu resultado e a percentagem de questões certas. Responda a primeira e Clique em Proxima Questão.",
        width=200,fg="black", font=("ariel", 12, "bold"))
        sub_line2.place(x=-500, y=70)

        sub_line3 = Label(gui, text="Se pretender sair basta clicar em SAIR e o jogo termina imediatamente.",
        width=200,fg="black", font=("ariel", 12))
        sub_line3.place(x=-400, y=90)
         
    def radio_buttons(self):
         
        q_list = []
        y_pos = 185
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))

            q_list.append(radio_btn)

            radio_btn.place(x = 100, y = y_pos)

            y_pos += 40
         
        return q_list
 
gui = Tk()
gui.geometry("800x450")
gui.title("")
with open('data.json') as f:
    data = json.load(f)
question = (data['questao'])
options = (data['opcoes'])
answer = (data['resposta'])
quiz = Quiz()
gui.mainloop()
