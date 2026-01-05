from control import tf

def ft_PID(Kp, Ki, Kd, N):
    P = tf([Kp], [1])
    I = tf([Ki], [1, 0])
    D = tf([Kd * N, 0], [1, N])
    C = P + I + D
    return C
