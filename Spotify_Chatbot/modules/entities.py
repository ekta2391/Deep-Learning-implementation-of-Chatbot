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
        self.artists = ['Charlie Puth', 'Ed Sheeran', 'Drake-More', 'Kendrick Lamar', 'Lady Gaga']
        self.genres = ['pop', 'hip hop', 'rap', 'rock', 'jazz'] 
        self.albums = ['Attention', '5', 'x (Deluxe Edition)','x (Wembley Edition)', 'Views', 'DAMN',  'Life', 'The Cure']
        self.tracks = ['A','B','C']
        

        self.EntType = Enum('Entity Type', '<artist> <genre> <album> <track> <non_ent>')


    def ent_type(self, ent):
        if ent in self.artists:
            return self.EntType['<artist>'].name
        elif ent in self.genres:
            return self.EntType['<genre>'].name
        elif ent in self.albums:
            return self.EntType['<album>'].name
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
