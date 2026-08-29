def to_seconds(time_str):
    mm, ss = map(int, time_str.split(":"))
    return mm * 60 + ss

def to_time_str(seconds):
    mm = seconds // 60
    ss = seconds % 60
    return f"{str(mm).zfill(2)}:{str(ss).zfill(2)}"

def solution(video_len, pos, op_start, op_end, commands):
    total_len = to_seconds(video_len)
    current_pos = to_seconds(pos)
    opening_start = to_seconds(op_start)
    opening_end = to_seconds(op_end)
    
    if opening_start <= current_pos <= opening_end:
        current_pos = opening_end
        
    for cmd in commands:
        if cmd == "prev":
            current_pos -= 10
            if current_pos < 0: 
                current_pos = 0
        elif cmd == "next":
            current_pos += 10
            if current_pos > total_len: 
                current_pos = total_len
                
        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end

    return to_time_str(current_pos)