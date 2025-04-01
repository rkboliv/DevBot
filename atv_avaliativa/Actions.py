from rasa_sdk import Action
from rasa_sdk.events import SlotSet

SOLUCOES = {
    "não consigo acessar minha conta": "Tente redefinir sua senha clicando em 'Esqueci minha senha' na página de login.",
    "quero mudar meu plano": "Você pode alterar seu plano acessando as configurações da sua conta no nosso site.",
    "o aplicativo não funciona": "Verifique se está usando a versão mais recente do aplicativo e se sua internet está estável."
}

class ActionFornecerSuporte(Action):
    def name(self):
        return "action_fornecer_suporte"
    
    def run(self, dispatcher, tracker, domain):
        problema = tracker.get_slot("problema")
        
        if problema in SOLUCOES:
            dispatcher.utter_message(text=SOLUCOES[problema])
        else:
            dispatcher.utter_message(text="Não consegui resolver seu problema. Encaminhando para um atendente humano...")
        
        return []
