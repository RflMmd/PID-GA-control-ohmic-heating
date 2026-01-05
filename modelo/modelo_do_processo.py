from control import tf

def aquecimento_ohmico():
    G = tf([0.001221, 0.000479], [1, 0.4022, 4.262e-05])
    return G
