path = open('moves.txt', 'r')
pathing = path.read().split(',')

class Pacman:
    vuln_ghost = 200
    lives = 3 
    points = 5000

    def pacman_eats_ghost():
        Pacman.points += Pacman.vuln_ghost
        Pacman.vuln_ghost *= 2
        if Pacman.vuln_ghost == 1600:
            Pacman.vuln_ghost

    def pacman_gets_ate():
        Pacman.lives -= 1

    def pacman_eats_edibles(edibles):
        Pacman.points += edibles
        return Pacman.points
    
    def pacman_extra_life():
        Pacman.lives += 1

new_life = 10000

edibles = {
    'dot' : 10,
    'cherry' : 100,
    'strawberry' : 300,
    'orange' : 500, 
    'apple' : 700, 
    'melon' : 1000, 
    'galaxian' : 2000, 
    'bell' : 3000,
    'key' : 5000,
}

for encounter in pathing:
    hit = encounter.lower()
    
    if hit == 'vulnerableghost':
        Pacman.pacman_eats_ghost()

    elif hit == 'invincibleghost':
        print('lost a life')
        Pacman.pacman_gets_ate()
    
    else:
        for key, value in edibles.items():
            # print(key, value, hit)
            if hit == key:
                # print(hit, key)
                Pacman.pacman_eats_edibles(value)
    if Pacman.points >= new_life:
        print('gained a life')
        Pacman.pacman_extra_life()
        new_life += 10000
    if Pacman.lives == 0:
        break
print(f"Lives: {Pacman.lives}\n"
    f"Points: {Pacman.points}")