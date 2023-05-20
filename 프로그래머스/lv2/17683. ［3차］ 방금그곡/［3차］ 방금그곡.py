def minute(t1, t2):
    t_1, m_1 = map(int, t1.split(":"))
    t_2, m_2 = map(int, t2.split(":"))
    t = t_2 - t_1
    m = m_2 - m_1
    
    return t * 60 + m


def solution(m, musicinfos):
    answer = "(None)"
    ml = 0
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
    for musicinfo in musicinfos:
        t1, t2, music, scale = musicinfo.split(",")
        mm = minute(t1, t2)
        scale = scale.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
        l = len(scale)
        a, b = mm // l, mm % l
        listen_scale = scale * a + "".join(scale[:b])
        if m in listen_scale and mm > ml:
            answer = music
            ml = mm
        
    return answer