
 from typing import Any, Text, Dict, List

 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher


 class ActionRecomendarFilme(Action):
     def name(self) -> Text:
         return "action_recomendar_filme"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       genero = tracker.get_slot("genero")
       filmes = self.obter_recomendacoes(genero)
       if filmes:
          dispatcher.utter_message(text=f"Para o gênero {genero}, recomendo {',' . join(filmes)}")

       else:
           dispatcher.utter_message(text="Desculpe, não encontrei recomendações para esse gênero.")


       return []
     

     def obter_rcomendacoes(self, genero: Text) -> list[Text]:
        filmes_por_genero = {
           "comédia": ["Se Beber, Não Case!", "Minha Mãe é Uma Peça", "Mister Bean"]
           "ação": ["Vingadores", "Guerra Mundial Z", "Missão Impossível"]
           "drama": ["Extraordinário", "Milagres do Paraíso", "Cartas Para Deus", "O Menino do Pijama Listrado"]
           "suspense": ["O Lar das Crianças Peculiares", "Anjos do Apocalipse", "Bird Box"]
        }

#