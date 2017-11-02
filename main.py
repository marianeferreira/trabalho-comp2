# -*- coding: utf-8 -*-

from interface import *

root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='7.png'))
root.protocol("WM_DELETE_WINDOW", lambda:sair(root)) # Executa a função sair quando o botão X é clicado
app = Minha_Aplicacao(root)
app.mainloop()