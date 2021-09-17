
def calcularCartas(carta1, carta2):

    if carta1[-1] == carta2[-1]:

        if (carta1[0] == 'A' and carta2[0] == 'K') or (carta1[0] == 'K' and carta2[0] == 'A'):
            return 0.68
        elif (carta1[0] == 'A' and carta2[0] == 'Q') or (carta1[0] == 'Q' and carta2[0] == 'A'):
            return 0.67
        elif (carta1[0] == 'A' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'A'):
            return 0.66
        elif (carta1[0] == 'A' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'A'):
            return 0.66
        elif (carta1[0] == 'A' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'A'):
            return 0.64
        elif (carta1[0] == 'A' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'A'):
            return 0.63
        elif (carta1[0] == 'A' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'A'):
            return 0.63
        elif (carta1[0] == 'A' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'A'):
            return 0.62
        elif (carta1[0] == 'A' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'A'):
            return 0.62
        elif (carta1[0] == 'A' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'A'):
            return 0.61
        elif (carta1[0] == 'A' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'A'):
            return 0.6
        elif (carta1[0] == 'A' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'A'):
            return 0.59
        elif (carta1[0] == 'K' and carta2[0] == 'Q') or (carta1[0] == 'Q' and carta2[0] == 'K'):
            return 0.64
        elif (carta1[0] == 'K' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'K'):
            return 0.64
        elif (carta1[0] == 'K' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'K'):
            return 0.63
        elif (carta1[0] == 'K' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'K'):
            return 0.61
        elif (carta1[0] == 'K' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'K'):
            return 0.6
        elif (carta1[0] == 'K' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'K'):
            return 0.59
        elif (carta1[0] == 'K' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'K'):
            return 0.58
        elif (carta1[0] == 'K' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'K'):
            return 0.58
        elif (carta1[0] == 'K' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'K'):
            return 0.57
        elif (carta1[0] == 'K' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'K'):
            return 0.56
        elif (carta1[0] == 'K' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'K'):
            return 0.55
        elif (carta1[0] == 'Q' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'Q'):
            return 0.61
        elif (carta1[0] == 'Q' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'Q'):
            return 0.61
        elif (carta1[0] == 'Q' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'Q'):
            return 0.59
        elif (carta1[0] == 'Q' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'Q'):
            return 0.58
        elif (carta1[0] == 'Q' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'Q'):
            return 0.56
        elif (carta1[0] == 'Q' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'Q'):
            return 0.55
        elif (carta1[0] == 'Q' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'Q'):
            return 0.55
        elif (carta1[0] == 'Q' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'Q'):
            return 0.54
        elif (carta1[0] == 'Q' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'Q'):
            return 0.53
        elif (carta1[0] == 'Q' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'Q'):
            return 0.52
        elif (carta1[0] == 'J' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'J'):
            return 0.59
        elif (carta1[0] == 'J' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'J'):
            return 0.57
        elif (carta1[0] == 'J' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'J'):
            return 0.56
        elif (carta1[0] == 'J' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'J'):
            return 0.54
        elif (carta1[0] == 'J' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'J'):
            return 0.53
        elif (carta1[0] == 'J' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'J'):
            return 0.52
        elif (carta1[0] == 'J' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'J'):
            return 0.51
        elif (carta1[0] == 'J' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'J'):
            return 0.5
        elif (carta1[0] == 'J' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'J'):
            return 0.5
        elif (carta1[0] == 'T' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'T'):
            return 0.56
        elif (carta1[0] == 'T' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'T'):
            return 0.54
        elif (carta1[0] == 'T' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'T'):
            return 0.53
        elif (carta1[0] == 'T' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'T'):
            return 0.51
        elif (carta1[0] == 'T' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'T'):
            return 0.49
        elif (carta1[0] == 'T' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'T'):
            return 0.49
        elif (carta1[0] == 'T' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'T'):
            return 0.48
        elif (carta1[0] == 'T' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'T'):
            return 0.47
        elif (carta1[0] == '9' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == '9'):
            return 0.53
        elif (carta1[0] == '9' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == '9'):
            return 0.51
        elif (carta1[0] == '9' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '9'):
            return 0.5
        elif (carta1[0] == '9' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '9'):
            return 0.48
        elif (carta1[0] == '9' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '9'):
            return 0.46
        elif (carta1[0] == '9' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '9'):
            return 0.46
        elif (carta1[0] == '9' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '9'):
            return 0.45
        elif (carta1[0] == '8' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == '8'):
            return 0.5
        elif (carta1[0] == '8' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '8'):
            return 0.49
        elif (carta1[0] == '8' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '8'):
            return 0.47
        elif (carta1[0] == '8' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '8'):
            return 0.45
        elif (carta1[0] == '8' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '8'):
            return 0.43
        elif (carta1[0] == '8' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '8'):
            return 0.43
        elif (carta1[0] == '7' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '7'):
            return 0.48
        elif (carta1[0] == '7' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '7'):
            return 0.46
        elif (carta1[0] == '7' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '7'):
            return 0.45
        elif (carta1[0] == '7' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '7'):
            return 0.43
        elif (carta1[0] == '7' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '7'):
            return 0.41
        elif (carta1[0] == '6' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '6'):
            return 0.46
        elif (carta1[0] == '6' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '6'):
            return 0.44
        elif (carta1[0] == '6' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '6'):
            return 0.42
        elif (carta1[0] == '6' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '6'):
            return 0.4
        elif (carta1[0] == '5' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '5'):
            return 0.44
        elif (carta1[0] == '5' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '5'):
            return 0.43
        elif (carta1[0] == '5' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '5'):
            return 0.41
        elif (carta1[0] == '4' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '4'):
            return 0.42
        elif (carta1[0] == '4' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '4'):
            return 0.4
        elif (carta1[0] == '3' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '3'):
            return 0.39
        elif carta1[0] == '2' and carta2[0] == '2':
            return 0.51
    else:
        if (carta1[0] == 'A' and carta2[0] == 'A'):
            return 0.85
        elif (carta1[0] == 'A' and carta2[0] == 'K') or (carta1[0] == 'K' and carta2[0] == 'A'):
            return 0.66
        elif (carta1[0] == 'A' and carta2[0] == 'Q') or (carta1[0] == 'Q' and carta2[0] == 'A'):
            return 0.65
        elif (carta1[0] == 'A' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'A'):
            return 0.65
        elif (carta1[0] == 'A' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'A'):
            return 0.64
        elif (carta1[0] == 'A' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'A'):
            return 0.62
        elif (carta1[0] == 'A' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'A'):
            return 0.61
        elif (carta1[0] == 'A' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'A'):
            return 0.6
        elif (carta1[0] == 'A' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'A'):
            return 0.59
        elif (carta1[0] == 'A' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'A'):
            return 0.6
        elif (carta1[0] == 'A' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'A'):
            return 0.59
        elif (carta1[0] == 'A' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'A'):
            return 0.58
        elif (carta1[0] == 'A' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'A'):
            return 0.57
        elif carta1[0] == 'K' and carta2[0] == 'K':
            return 0.83
        elif (carta1[0] == 'K' and carta2[0] == 'Q') or (carta1[0] == 'Q' and carta2[0] == 'K'):
            return 0.62
        elif (carta1[0] == 'K' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'K'):
            return 0.62
        elif (carta1[0] == 'K' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'K'):
            return 0.61
        elif (carta1[0] == 'K' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'K'):
            return 0.59
        elif (carta1[0] == 'K' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'K'):
            return 0.58
        elif (carta1[0] == 'K' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'K'):
            return 0.57
        elif (carta1[0] == 'K' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'K'):
            return 0.56
        elif (carta1[0] == 'K' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'K'):
            return 0.55
        elif (carta1[0] == 'K' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'K'):
            return 0.54
        elif (carta1[0] == 'K' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'K'):
            return 0.54
        elif (carta1[0] == 'K' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'K'):
            return 0.53
        elif carta1[0] == 'Q' and carta2[0] == 'Q':
            return 0.8
        elif (carta1[0] == 'Q' and carta2[0] == 'J') or (carta1[0] == 'J' and carta2[0] == 'Q'):
            return 0.59
        elif (carta1[0] == 'Q' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'Q'):
            return 0.59
        elif (carta1[0] == 'Q' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'Q'):
            return 0.57
        elif (carta1[0] == 'Q' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'Q'):
            return 0.55
        elif (carta1[0] == 'Q' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'Q'):
            return 0.54
        elif (carta1[0] == 'Q' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'Q'):
            return 0.53
        elif (carta1[0] == 'Q' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'Q'):
            return 0.52
        elif (carta1[0] == 'Q' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'Q'):
            return 0.51
        elif (carta1[0] == 'Q' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'Q'):
            return 0.5
        elif (carta1[0] == 'Q' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'Q'):
            return 0.49
        elif carta1[0] == 'J' and carta2[0] == 'J':
            return 0.78
        elif (carta1[0] == 'J' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'J'):
            return 0.57
        elif (carta1[0] == 'J' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'J'):
            return 0.55
        elif (carta1[0] == 'J' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'J'):
            return 0.53
        elif (carta1[0] == 'J' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'J'):
            return 0.52
        elif (carta1[0] == 'J' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'J'):
            return 0.5
        elif (carta1[0] == 'J' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'J'):
            return 0.49
        elif (carta1[0] == 'J' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'J'):
            return 0.48
        elif (carta1[0] == 'J' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'J'):
            return 0.48
        elif (carta1[0] == 'J' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'J'):
            return 0.47
        elif carta1[0] == 'J' and carta2[0] == 'J':
            return 0.78
        elif (carta1[0] == 'J' and carta2[0] == 'T') or (carta1[0] == 'T' and carta2[0] == 'J'):
            return 0.57
        elif (carta1[0] == 'J' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'J'):
            return 0.55
        elif (carta1[0] == 'J' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'J'):
            return 0.53
        elif (carta1[0] == 'J' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'J'):
            return 0.52
        elif (carta1[0] == 'J' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'J'):
            return 0.5
        elif (carta1[0] == 'J' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'J'):
            return 0.49
        elif (carta1[0] == 'J' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'J'):
            return 0.48
        elif (carta1[0] == 'J' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'J'):
            return 0.48
        elif (carta1[0] == 'J' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'J'):
            return 0.47
        elif carta1[0] == 'T' and carta2[0] == 'T':
            return 0.75
        elif (carta1[0] == 'T' and carta2[0] == '9') or (carta1[0] == '9' and carta2[0] == 'T'):
            return 0.53
        elif (carta1[0] == 'T' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == 'T'):
            return 0.52
        elif (carta1[0] == 'T' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == 'T'):
            return 0.5
        elif (carta1[0] == 'T' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == 'T'):
            return 0.48
        elif (carta1[0] == 'T' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == 'T'):
            return 0.47
        elif (carta1[0] == 'T' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == 'T'):
            return 0.46
        elif (carta1[0] == 'T' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == 'T'):
            return 0.45
        elif (carta1[0] == 'T' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == 'T'):
            return 0.44
        elif carta1[0] == '9' and carta2[0] == '9':
            return 0.72
        elif (carta1[0] == '9' and carta2[0] == '8') or (carta1[0] == '8' and carta2[0] == '9'):
            return 0.50
        elif (carta1[0] == '9' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == '9'):
            return 0.48
        elif (carta1[0] == '9' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '9'):
            return 0.47
        elif (carta1[0] == '9' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '9'):
            return 0.45
        elif (carta1[0] == '9' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '9'):
            return 0.43
        elif (carta1[0] == '9' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '9'):
            return 0.43
        elif (carta1[0] == '9' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '9'):
            return 0.42
        elif carta1[0] == '8' and carta2[0] == '8':
            return 0.69
        elif (carta1[0] == '8' and carta2[0] == '7') or (carta1[0] == '7' and carta2[0] == '8'):
            return 0.47
        elif (carta1[0] == '8' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '8'):
            return 0.46
        elif (carta1[0] == '8' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '8'):
            return 0.44
        elif (carta1[0] == '8' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '8'):
            return 0.42
        elif (carta1[0] == '8' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '8'):
            return 0.4
        elif (carta1[0] == '8' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '8'):
            return 0.4
        elif carta1[0] == '7' and carta2[0] == '7':
            return 0.67
        elif (carta1[0] == '7' and carta2[0] == '6') or (carta1[0] == '6' and carta2[0] == '7'):
            return 0.45
        elif (carta1[0] == '7' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '7'):
            return 0.43
        elif (carta1[0] == '7' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '7'):
            return 0.41
        elif (carta1[0] == '7' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '7'):
            return 0.39
        elif (carta1[0] == '7' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '7'):
            return 0.37
        elif carta1[0] == '6' and carta2[0] == '6':
            return 0.64
        elif (carta1[0] == '6' and carta2[0] == '5') or (carta1[0] == '5' and carta2[0] == '6'):
            return 0.43
        elif (carta1[0] == '6' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '6'):
            return 0.41
        elif (carta1[0] == '6' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '6'):
            return 0.39
        elif (carta1[0] == '6' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '6'):
            return 0.37
        elif carta1[0] == '5' and carta2[0] == '5':
            return 0.61
        elif (carta1[0] == '5' and carta2[0] == '4') or (carta1[0] == '4' and carta2[0] == '5'):
            return 0.41
        elif (carta1[0] == '5' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '5'):
            return 0.39
        elif (carta1[0] == '5' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '5'):
            return 0.37
        elif carta1[0] == '4' and carta2[0] == '4':
            return 0.58
        elif (carta1[0] == '4' and carta2[0] == '3') or (carta1[0] == '3' and carta2[0] == '4'):
            return 0.38
        elif (carta1[0] == '4' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '4'):
            return 0.36
        elif carta1[0] == '3' and carta2[0] == '3':
            return 0.55
        elif (carta1[0] == '3' and carta2[0] == '2') or (carta1[0] == '2' and carta2[0] == '3'):
            return 0.35
        elif carta1[0] == '2' and carta2[0] == '2':
            return 0.51

        