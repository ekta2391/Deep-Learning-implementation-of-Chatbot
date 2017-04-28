from enum import Enum
import numpy as np


class EntityTracker():

    def __init__(self):
        self.entities = {
                '<artist>' : None,
                '<genre>' : None,
                '<album>' : None,
                '<track>': None,
                
                }
        self.num_features = 4 # tracking 4 entities
        self.rating = None

        # constants
        self.albums = ['Attention', 'Five', 'x(DeluxeEdition)','x (Wembley Edition)','Views', 'DAMN',  'Life', 'The-Cure','Hozier']
        self.genres = ['pop', 'hiphop', 'rap', 'rock', 'jazz'] 
        self.artists = ['CharliePuth', 'EdSheeran', 'DrakeMore', 'KendrickLamar', 'Lady-Gaga','Hozier']
        self.tracks = ['Photograph','Sunburn','Feel','Be like you','Get it together','Blem','Free Smoke','Shape of you','Sedated']
        

        self.EntType = Enum('Entity Type', '<album> <genre> <artist> <track> <non_ent>')


    def ent_type(self, ent):
        if ent in self.albums:
            #assumption this is giving us the actual artist name that we passed
            return self.EntType['<album>'].name
        elif ent in self.genres:
            return self.EntType['<genre>'].name
        elif ent in self.artists:
            return self.EntType['<artist>'].name
        elif ent in self.tracks:
            return self.EntType['<track>'].name
        else:
            return ent


    def extract_entities(self, utterance, update=True):
        tokenized = []
        for word in utterance.split(' '):
            entity = self.ent_type(word)
            if word != entity and update:
                self.entities[entity] = word

            tokenized.append(entity)

        return ' '.join(tokenized)


    def context_features(self):
       keys = list(set(self.entities.keys()))
       self.ctxt_features = np.array( [bool(self.entities[key]) for key in keys], 
                                   dtype=np.float32 )
       
       
    
       return self.ctxt_features


    def action_mask(self):
        print('Not yet implemented. Need a list of action templates!')
