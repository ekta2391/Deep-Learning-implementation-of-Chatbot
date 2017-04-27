import modules.util as util
import numpy as np

'''
    Action Templates
    1. 'any preference on a type of genre',
    2. 'api_call <genre> <artist> <track>',
    3. 'great let me get the spotify link',
    4. 'hello what can I help you with today',
    5. 'here it is <album>',
    6. 'here it is <spotify link>',
    7. 'which album would you like to hear',
    8. "i'm on it",
    9. 'is there anything i can help you with',
    10. 'ok let me look into some options for you',
    11. 'sure is there anything else to update',
    12. 'sure let me find an other option for you',
    13. 'what do you think of this track: ',
    14. 'which artist should it be',
    15. 'which track are you looking for',
    16. "you're welcome",
    
    [1] : artist
    [2] : genre
    [3] : album
    [4] : track
    
'''   
  
class ActionTracker():

    def __init__(self, ent_tracker):
        # maintain an instance of EntityTracker
        self.et = ent_tracker
        # get a list of action templates
        self.action_templates = self.get_action_templates()
        self.action_size = len(self.action_templates)
        print("Action Size", self.action_size)
        # action mask
        self.am = np.zeros([self.action_size], dtype=np.float32)
        # action mask lookup, built on intuition
        self.am_dict = {
                '0000' : [ 4,8,1,14,7,15],
                '0001' : [ 4,8,1,14,7],
                '0010' : [ 4,8,1,14,15],
                '0011' : [ 4,8,1,14],
                '0100' : [ 4,8,1,7,15],
                '0101' : [ 4,8,1,7],
                '0110' : [ 4,8,1,15],
                '0111' : [ 4,8,1],
                '1000' : [ 4,8,14,7,15],
                '1001' : [ 4,8,14,7],
                '1010' : [ 4,8,14,15],
                '1011' : [ 4,8,14],
                '1100' : [ 4,8,7,15],
                '1101' : [ 4,8,7],
                '1110' : [ 4,8,15],
                '1111' : [ 2,3,5,6,8,9,10,11,12,13,16 ]
                }


    def action_mask(self):
        # get context features as string of ints (0/1)
        # giving us '0000' as a string value (context features returns us 0/1 for the four entites depemding upon their values)
        ctxt_f = ''.join([ str(flag) for flag in self.et.context_features().astype(np.int32) ])

        def construct_mask(ctxt_f):
            # indices is [4,8,...] as per the ctxt_f value
            indices = self.am_dict[ctxt_f]
            print(indices)
            for index in indices:
                self.am[index-1] = 1.
            return self.am
    
        return construct_mask(ctxt_f)

    def get_action_templates(self):
        responses = list(set([ self.et.extract_entities(response, update=False)
            for response in util.get_responses() ]))
        print(responses)
       
        def extract_(response):
            
            template = []
            for word in response.split(' '):
                if 'spotify_music' in word: 
                    if 'R_spotify_link' in word:
                        template.append('<spotify_link>')
                    elif 'R_genre' in word:
                        template.append('<genre>')
                    else:
                        template.append('<artist>')
                else:
                    template.append(word)
            
            return ' '.join(template)

        # extract restaurant entities
        return sorted(set([ extract_(response) for response in responses ]))
