from data_handler import *

def similarty(s1,s2):
    
    score_diff = 10000 * abs(float(s1['score'])-float(s2['score']))
    acous_diff = 1000 * abs(float(s1['acousticness'])-float(s2['acousticness']))
    dancb_diff = 100 * abs(float(s1['danceability'])-float(s2['danceability']))
    energ_diff = 30 * abs(float(s1['energy'])-float(s2['energy']))
    liven_diff = 100 * abs(float(s1['liveness'])-float(s2['liveness']))
    loudn_diff = 10 * abs(float(s1['loudness'])-float(s2['loudness']))
    spech_diff = 100 * abs(float(s1['speechiness'])-float(s2['speechiness']))
    tempo_diff = 0.1 * abs(float(s1['tempo'])-float(s2['tempo']))
    valnc_diff = 10 * abs(float(s1['valence'])-float(s2['valence']))
    
    difference = score_diff + acous_diff + dancb_diff**2 + energ_diff**2 \
    + liven_diff**2 + loudn_diff**2 + spech_diff**2 + tempo_diff + valnc_diff**2
    
    return difference

def dfFilterEnergy(df, id):
    x = music_df.energy[id]
    maax = 0.050
    miin = 0.050
    return df.loc[(df['energy'] > x-miin) & (df['energy'] < x+maax)]

def dfFilterDance(df, id):
    x = music_df.danceability[id]
    maax = 0.050
    miin = 0.050
    return df.loc[(df['danceability'] > x-miin) & (df['danceability'] < x+maax)]

def dfFilterLoud(df, id):
    x = music_df.loudness[id]
    maax = 0.50
    miin = 0.50
    return df.loc[(music_df['loudness'] > x-miin) & (df['loudness'] < x+maax)]

def getNearSongListId(id):
    df_enrg = dfFilterEnergy(music_df, id)
    df_danc = dfFilterDance(df_enrg, id)
    df_loud = dfFilterLoud(df_danc, id)
    return df_loud.index.tolist()


def getMusic(song, artist=None, k=5):
    id = getSongId(song=song, artist=artist)
    if id:
        list_of_score = []
        
        nearMusicList = getNearSongListId(id)
        if len(nearMusicList) ==0:
            return None, getMusicWithid(id)

        for songid in nearMusicList:
            
            sim = similarty(music_df.iloc[id],music_df.iloc[songid])
            songItem = (sim, songid)
            list_of_score.append(songItem)            
        
        list_of_musicid = getKMusic(list_of_score, id, k)
        
        rec_musics = getDictResult(list_of_musicid)

        return rec_musics, getMusicWithid(id)
        
    else:
        return None, [song, artist]