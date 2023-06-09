def simulate_lru(reference_string, frame_size):
    frame = []
    page_faults = 0
    hit_count = 0

    for page in reference_string:
        if page in frame:
            # 페이지가 프레임에 이미 존재하는 경우
            hit_count += 1
            # 해당 페이지를 가장 최근에 사용한 위치로 이동
            frame.remove(page)
            frame.append(page)
        else:
            # 페이지가 프레임에 존재하지 않는 경우
            page_faults += 1
            if len(frame) < frame_size:
                # 아직 프레임에 여유 공간이 있는 경우
                frame.append(page)
            else:
                # 프레임이 모두 차 있는 경우, 가장 오래 전에 사용된 페이지를 교체
                frame.pop(0)
                frame.append(page)

            # 페이지 폴트가 발생한 순간 현재의 프레임 상태를 출력
            print(f"{page_faults}번째 페이지 폴트: {frame}")

    print("\nHit 발생 횟수:", hit_count)
    print("Page Fault 발생 횟수:", page_faults)
    print("Page Fault Rate (%):", (page_faults / len(reference_string)) * 100)

def simulate_second_chance(reference_string, frame_size):
    frame = []
    reference_bits = []
    page_faults = 0
    hit_count = 0

    # 페이지를 교체해야 할 경우 cursor를 활용하여 프레임을 선택
    # 현재 프레임의 위치를 나타냄
    cursor = 0

    for page in reference_string:
        if page in frame:
            # 페이지가 프레임에 이미 존재하는 경우
            hit_count += 1
            # 해당 페이지의 참조 비트를 1로 설정
            index = frame.index(page)
            reference_bits[index] = 1
        else:
            # 페이지가 프레임에 존재하지 않는 경우
            page_faults += 1
            if len(frame) < frame_size:
                # 아직 프레임에 여유 공간이 있는 경우
                frame.append(page)
                reference_bits.append(1)
            else:
                # 프레임이 모두 차 있는 경우, 페이지 교체
                while True:
                    # 현재 cursor 위치의 페이지의 참조 비트 확인
                    if reference_bits[cursor] == 0:
                        # 참조 비트가 0이면 페이지 교체 후 종료
                        frame[cursor] = page
                        reference_bits[cursor] = 1
                        break
                    else:
                        # 참조 비트가 1이면 참조 비트를 0으로 설정하고 cursor 이동
                        reference_bits[cursor] = 0
                        clock_hand = (cursor + 1) % frame_size

            # 페이지 교체 후 프레임 상태 출력
            print(f"{page_faults}번째 페이지 폴트: {frame}")

    print("\nHit 발생 횟수:", hit_count)
    print("Page Fault 발생 횟수:", page_faults)
    print("Page Fault Rate (%):", (page_faults / len(reference_string)) * 100)
