from tkinter import * #biblioteca nativa
from tkinter import ttk


janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()


        self.lista_frame2()
        janela.mainloop() #a janela fica carregada na tela até ser fechada


    def tela(self):

        self.janela.title('MAGALU') #título
        self.janela.configure(background='#0000FF') #cor de fundo
        self.janela.geometry('700x500') #tamanho da tela
        self.janela.resizable(True, True) #deixar responsivo
        self.janela.wm_maxsize(width=700, height=500) #trava nessa medida

    def frames(self):
        self.frame0 = Frame(self.janela, bg='#0b090a') #uma característica de frame, usado para editá-lo
        self.frame0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame1 = Frame(self.janela, bg='#0b090a')  # uma característica de frame, usado para editá-lo
        self.frame1.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.11) #relheight altura da sombra

        self.frame2 = Frame(self.janela, bg='#0b090a')  # uma característica de frame, usado para editá-lo
        self.frame2.place(relx=0.03, rely=0.5, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btBuscar = Button(self.frame1, text='Buscar', bg='#d3d3d3', foreground='black') #criando o botão
        self.btBuscar.place(relx=0.15, rely=0.4, relwidth=0.1, relheight=0.5) #dimensionando o botão

        self.btLimpar = Button(self.frame1, text='Limpar', bg='#d3d3d3', foreground='black')  # criando o botão
        self.btLimpar.place(relx=0.27, rely=0.4, relwidth=0.1, relheight=0.5)  # dimensionando o botão

        self.btCreate = Button(self.frame1, text='Create', bg='#d3d3d3', foreground='black')  # criando o botão
        self.btCreate.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.5)  # dimensionando o botão

        self.btRead = Button(self.frame1, text='Read', bg='#d3d3d3', foreground='black')  # criando o botão
        self.btRead.place(relx=0.57, rely=0.4, relwidth=0.1, relheight=0.5)  # dimensionando o botão

        self.btUpdate = Button(self.frame1, text='Update', bg='#d3d3d3', foreground='black')  # criando o botão
        self.btUpdate.place(relx=0.69, rely=0.4, relwidth=0.1, relheight=0.5)  # dimensionando o botão

        self.btDelete = Button(self.frame1, text='Delete', bg='#d3d3d3', foreground='black')  # criando o botão
        self.btDelete.place(relx=0.81, rely=0.4, relwidth=0.1, relheight=0.5)  # dimensionando o botão




    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=('col1', #criando as colunas
                                                                     'col2',
                                                                     'col3')) #faixa de cima da tabela


        self.listaCli.heading('#0', text='ID') #dando nome as colunas
        self.listaCli.heading('#1', text='Modelo')
        self.listaCli.heading('#2', text='Preço')
        self.listaCli.heading('#3', text='Marca')

        self.listaCli.column('#0', width=35) #largura das colunas
        self.listaCli.column('#1', width=188)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=70)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)












