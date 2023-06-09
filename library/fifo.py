def simulate_fifo(reference_string, frame_size):
    frame = []
    page_set = set()
    page_faults = 0

    for page in reference_string:
        if page not in page_set:
            if len(frame) == frame_size:
                removed_page = frame.pop(0)
                page_set.remove(removed_page)

            frame.append(page)
            page_set.add(page)
            page_faults += 1

            print(f"{page_faults}번째 페이지 폴트: {frame}")  # 현재 메모리에 있는 페이지 출력

    hit_count = len(reference_string) - page_faults

    print("\nHit 발생 횟수:", hit_count)
    print("Page Fault 발생 횟수:", page_faults)
    print("Page Fault Rate (%):", (page_faults / len(reference_string)) * 100)
