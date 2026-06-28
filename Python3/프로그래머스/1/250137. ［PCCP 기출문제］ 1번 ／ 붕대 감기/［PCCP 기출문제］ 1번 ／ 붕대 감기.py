def solution(bandage, health, attacks):
    duration = bandage[0]
    treat_per_sec = bandage[1]
    additional_treat = bandage[2]
    current_health = health
    current_time = 0
    
    for attack in attacks:
        attack_time = attack[0]
        attack_amount = attack[1]
        
        free_time = attack_time - current_time - 1
        if free_time > 0:
            current_health += free_time * treat_per_sec
            current_health += (free_time // duration) * additional_treat
            if current_health > health:
                current_health = health
                
        current_health -= attack_amount    
        
        if current_health <= 0: 
            return -1
            
        current_time = attack_time 
        

    return current_health