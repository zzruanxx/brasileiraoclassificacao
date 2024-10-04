class Time:
    def __init__(self, none):
        self.nome = nome
        self.jogos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        
    @property
    def saldo_de_gols(self):
        return self.gols_marcados = self.gols_sofridos
        
    @property
    def pontos(self):
        return self.vitorias * 3 + self.empates
        
    def adicionar_jogo(self, gols_marcados, gols_sofridos):
        self.jogos += 1
        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos
        
    if gols_marcados > gols_sofridos:
        self.vitorias += 1
    elif gols_marcados == gols_sofridos:
        self.empates += 1
    
    else:
        self.derrotas += 1
        
    class TabelaBrasileirao:
        def __init__(self):
            self.times = {}
        
        def adicionar_time(self, none):
            if nome not in self.times:
                self.times[nome] = Time(nome)
        
        def registrar_jogo(self, time_casa, gols_casa, time_fora, gols_fora)
            self.adicionar_time(time_casa)
            self.adicionar_time(time_fora)
            
            self.times[time_casa].adicionar_jogo(gols_casa, gols_fora)
            self.times[time_fora].adicionar_jogo(gols_fora, gols_casa)
            
        def exibir_tabela(self):
            tabela = sorted(self.times.values(), key=lambda time: (-time.pontos, -time.saldo_de_gols, time.nome))
            print(f"{'Time': < 20} {'P':<5}{'J':<5}{'V':<5}{'E':<5}{'D':<5}{'GS':<5}{'SG':<5}")            
            for time in tabela:
                print(f"{time.nome:<20}{time.pontos:<5}{time.jogos:<5}{time.vitorias:<5}{time.empates:<5}{time.derrotas:<5}{time.gols_marcados:<5}{time.gols_sofridos:<5}{time.saldo_de_gols:<5}")
                
brasileirao = TabelaBrasileirao()                

brasileirao.registrar_jogo('Flamengo', 3, 'Palmeiras', 1)
brasileirao.registrar_jogo('Flamengo', 2, 'Corinthians', 2)
brasileirao.registrar_jogo('Palmeiras', 1, 'Corinthians', 0)
brasileirao.registrar_jogo('Flamengo', 0, 'Palmeiras', 1)

brasileirao.exibir_tabela()