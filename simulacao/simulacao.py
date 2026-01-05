from control import feedback, step_response, forced_response

def simulacao_do_sistema(G, C, tempo, setpoint):
    L = C * G
    H = feedback(L, 1)
    t, y = step_response(H, T=tempo)
    y *= setpoint
    _, u = forced_response(C, T=tempo, U=(setpoint - y))
    return t, y, u
