import numpy as np
players = player_gen(60)
teams = {}
sorted_players = sorted(players, key=lambda tup: tup[1])[::-1]
print('average = {}'.format(np.mean([player[1] for player in sorted_players])))
n_teams = len(players) // 5
for i in range(0, n_teams):
    teams['team' + str(i)] = [sorted_players.pop(i)]
n_teams = len(sorted_players) // 4
n_players = len(sorted_players)
for i in range(0, n_players):
    teams['team' + str(i % n_teams)].append(sorted_players[len(sorted_players) - i - 1])

tots = []
for key in teams.keys():
    mmr_tot = np.sum([team[1] for team in teams[key]])
    tots.append((key, np.mean(mmr_tot)))    
initial_std = np.std([t[1] for t in tots])
print('INITIAL STD: {}'.format(initial_std))
stds = []
for i in range(20):    
    tots = []
    for key in teams.keys():
        mmr_tot = np.sum([team[1] for team in teams[key]])
        tots.append((key, np.mean(mmr_tot)))
    current_std = np.std([t[1] for t in tots])
    stds.append(current_std)
    
    sorted_teams = sorted(tots, key=lambda tup: tup[1])[::-1]
    print('Top team is {}, lowest team is {}'.format(sorted_teams[0], sorted_teams[-1]))
    diff = sorted_teams[0][1] - sorted_teams[-1][1]
    print('With a difference of {}'.format(diff))
    tmax_sorted_players = sorted(teams[sorted_teams[0][0]], key=lambda tup: tup[1])[::-1]
    tmin_sorted_players = sorted(teams[sorted_teams[-1][0]], key=lambda tup: tup[1])[::-1]
    mem = 9999999
    for i, (p_max, p_min) in enumerate(zip(tmax_sorted_players, tmin_sorted_players)):
        print('{} from {} vs {} from {}'.format(p_max, sorted_teams[0], p_min, sorted_teams[-1]))
        p_diff = abs(p_max[1] - p_min[1])
        abs_diff = abs(diff/2 - p_diff)
        print('offset difference: {}'.format(abs_diff))
        if abs_diff < mem:
            mem = abs_diff
            change_index = i
        if current_std < initial_std:
            initial_std = current_std
            besto_teams = dict(teams)
            final_teams = dict(teams)
    print('swapping {}, {}'.format(tmax_sorted_players[change_index], tmin_sorted_players[change_index]))
    tmax_sorted_players[change_index], tmin_sorted_players[change_index] = tmin_sorted_players[change_index], tmax_sorted_players[change_index]
    teams[sorted_teams[0][0]], teams[sorted_teams[-1][0]] = tmax_sorted_players, tmin_sorted_players
    
print('=================PHASE 2=============')

stds2 = []
changed = False
for i in range(20):    
    tots = []
    for key in besto_teams.keys():
        mmr_tot = np.sum([team[1] for team in besto_teams[key]])
        tots.append((key, np.mean(mmr_tot)))
    current_std = np.std([t[1] for t in tots])
    stds2.append(current_std)
    sorted_teams = sorted(tots, key=lambda tup: tup[1])[::-1]
    print('Top team is {}, lowest team is {}'.format(sorted_teams[0], sorted_teams[-1]))
    diff = sorted_teams[0][1] - sorted_teams[-1][1]
    print('With a difference of {}'.format(diff))
    tmax_sorted_players = sorted(besto_teams[sorted_teams[0][0]], key=lambda tup: tup[1])[::-1]
    tmin_sorted_players = sorted(besto_teams[sorted_teams[-1][0]], key=lambda tup: tup[1])[::-1]
    mem = 9999999
    
    for i, p_max in enumerate(tmax_sorted_players):
        for j, p_min in enumerate(tmin_sorted_players):
            print('{} from {} vs {} from {}'.format(p_max, sorted_teams[0], p_min, sorted_teams[-1]))
            p_diff = p_max[1] - p_min[1]
            if p_diff > 0:
                abs_diff = abs((diff/2) - p_diff)
                print('offset difference: {}'.format(abs_diff))
                if abs_diff < mem and abs_diff < diff:
                    mem = abs_diff
                    change_index_max = i
                    change_index_min = j
                print('CURRENT STD: {}'.format(current_std))
                print('MEM STD: {}'.format(initial_std))
                if current_std < initial_std:
                    initial_std = current_std
                    besto_teams_2 = dict(besto_teams)
                    final_teams = dict(besto_teams)
                    changed = True 
            else:
                pass
                                     
    print('swapping {}, {}'.format(tmax_sorted_players[change_index_max], tmin_sorted_players[change_index_min]))
    tmax_sorted_players[change_index_max], tmin_sorted_players[change_index_min] = tmin_sorted_players[change_index_min], tmax_sorted_players[change_index_max]
    besto_teams[sorted_teams[0][0]], besto_teams[sorted_teams[-1][0]] = tmax_sorted_players, tmin_sorted_players
    print(besto_teams[sorted_teams[0][0]])
    print(besto_teams[sorted_teams[-1][0]])

if changed is not True:
    besto_teams_2 = besto_teams
tots = []
for key in final_teams.keys():
    mmr_tot = np.sum([team[1] for team in final_teams[key]])
    tots.append((key, np.mean(mmr_tot)))    
print('FINAL STD: {}'.format(np.std([t[1] for t in tots])))
print('STD PHASE 1 LOG: {}'.format(stds))
print('STD PHASE 2 LOG: {}'.format(stds2))
print('')
print('================ EQUIPOS FINALES SEGUN YOYOX ================')
for key in besto_teams_2:
    print('{} (mmr promedio {}):'.format(key, np.mean([player[1] for player in final_teams[key]])))
    for player in final_teams[key]:
        print('nick: {} mmr: {}'.format(player[0], player[1]))
print('================ /EQUIPOS FINALES SEGUN YOYOX ================')

def player_gen(n):
    mmrs = np.random.randint(1000, 5500, size=n)
    players = [('player'+str(i), mmr) for i, mmr in enumerate(mmrs)]
    return players
    