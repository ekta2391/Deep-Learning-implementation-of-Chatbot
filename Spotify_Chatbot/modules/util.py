def read_content():
    return ' '.join(get_utterances())

def read_dialogs(with_indices=False):

    def rm_index(row):
        return [' '.join(row[0].split(' ')[1:])] + row[1:]

    def filter_(dialogs):
        filtered_ = []
        for row in dialogs:
            if row[0][:14] != 'spotify_music_':
                filtered_.append(row)
        return filtered_

    with open('data/temp_data_8.txt') as f:
        dialogs = filter_([ rm_index(row.split('\t')) for row in  f.read().split('\n') ])
        # organize dialogs -> dialog_indices
        prev_idx = -1
        n = 1
        dialog_indices = []
        updated_dialogs = []
        for i, dialog in enumerate(dialogs):
            if not dialogs[i][0]:
                dialog_indices.append({
                    'start' : prev_idx + 1,
                    'end' : i - n + 1
                })
                prev_idx = i-n
                n += 1
            else:
                updated_dialogs.append(dialog)        

        if with_indices:
            return updated_dialogs, dialog_indices[:-1]
        
        return updated_dialogs

# returns the user'srequest part
def get_utterances(dialogs=[]):
    dialogs = dialogs if len(dialogs) else read_dialogs()
    return [ row[0] for row in dialogs ]

# returns the chatbot response part
def get_responses(dialogs=[]):
    dialogs = dialogs if len(dialogs) else read_dialogs()
    return [ row[1] for row in dialogs ] 
