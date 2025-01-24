import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
import threading
from api import obter_cotacao_cripto

kivy.require('2.0.0')  # Certifique-se de que a versão do Kivy seja compatível

class CryptoApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        self.title_label = Label(text="Consulta de Criptomoeda", font_size=24, color=(0.2, 0.8, 0.3, 1))
        layout.add_widget(self.title_label)

        # Campos de entrada
        self.cripto_input = TextInput(hint_text="Criptomoeda (ex: bitcoin)", multiline=False, size_hint=(1, None), height=40)
        self.moeda_input = TextInput(hint_text="Moeda (ex: brl, usd)", multiline=False, size_hint=(1, None), height=40)

        layout.add_widget(self.cripto_input)
        layout.add_widget(self.moeda_input)

        # Barra de carregamento
        self.carregando = ProgressBar(max=100, value=0, size_hint=(1, None), height=30)
        layout.add_widget(self.carregando)

        # Resultados
        self.result_label = Label(text="", font_size=18, color=(1, 1, 1, 1))
        layout.add_widget(self.result_label)

        # Botões
        self.search_button = Button(text="Buscar Cotação", on_press=self.buscar_cotacao, size_hint=(1, None), height=50)
        self.clear_button = Button(text="Limpar", on_press=self.limpar_campos, size_hint=(1, None), height=50)
        self.exit_button = Button(text="Sair", on_press=self.sair_aplicacao, size_hint=(1, None), height=50)

        layout.add_widget(self.search_button)
        layout.add_widget(self.clear_button)
        layout.add_widget(self.exit_button)

        return layout

    def buscar_cotacao(self, instance):
        cripto = self.cripto_input.text.strip().lower()
        moeda = self.moeda_input.text.strip().lower()

        if cripto == "" or moeda == "":
            self.show_warning("Entrada inválida", "Por favor, preencha os campos de criptomoeda e moeda.")
            return

        # Exibe a barra de carregamento
        self.carregando.value = 50

        # Rodando a busca em uma thread separada para não bloquear a interface
        threading.Thread(target=self.obter_resultado, args=(cripto, moeda)).start()

    def obter_resultado(self, cripto, moeda):
        preco = obter_cotacao_cripto(cripto, moeda)

        # Atualiza a interface com o resultado
        if isinstance(preco, float):
            self.result_label.text = f"A cotação para {cripto.upper()} em {moeda.upper()} é: {preco:.2f}"
        else:
            self.result_label.text = f"Erro na consulta. Código de erro: {preco}"

        self.carregando.value = 0  # Remove a barra de carregamento

    def limpar_campos(self, instance):
        self.cripto_input.text = ""
        self.moeda_input.text = ""
        self.result_label.text = ""

    def sair_aplicacao(self, instance):
        from kivy.app import App
        App.get_running_app().stop()

    def show_warning(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

# Rodando a aplicação
if __name__ == "__main__":
    CryptoApp().run()
