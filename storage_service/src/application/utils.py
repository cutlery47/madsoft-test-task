from src.storage.models.meme import Meme

def meme_to_dict(meme: Meme) -> dict:
    dict_meme = meme.__dict__
    dict_meme.pop('_sa_instance_state', None)
    return dict_meme
