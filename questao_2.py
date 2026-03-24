class Televisão:
    """
    Representa uma televisão digital simples.
    Permite controlar o canal, o volume e a função mudo.
    """
    def __init__(self):
        """
        Configura os valores iniciais quando a TV está ligada.
        Canal 1, volume 10, mudo desativado.
        """
        self.canal = 1
        self.volume = 10
        self.mudo = False
    
    def alterar_canais(self, novo_canal):
        """
        Troca o canal da TV.
        
        :param novo_canal: O canal que deseja (ex: 5, 7, 12).
        """
        self.canal = novo_canal

    def aumentar_volume(self):
        """
        Aumenta o volume de um em um, desde que a TV não esteja no mudo.
        """
        if not self.mudo:
            self.volume += 1

    def diminuir_volume(self):
        """
        Diminui o volume de um em um, desde que a TV não esteja no mudo 
        e o volume atual seja maior que 0.
        """
        if not self.mudo and self.volume > 0:
            self.volume -= 1

    def modo_mudo(self):
        """
        Alterna o estado do som da TV.
        Se estava mudo, volta ao normal. Se estava com som, fica silencioso.
        """
        if self.mudo:
            self.mudo = False
        else:
            self.mudo = True