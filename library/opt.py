def simulate_opt(reference_string, frame_size):
    frame = []
    page_faults = 0

    for i in range(len(reference_string)):
        if reference_string[i] not in frame:
            if len(frame) < frame_size:
                frame.append(reference_string[i])
            else:
                page_to_replace = find_optimal_page(reference_string, frame, i)
                frame[frame.index(page_to_replace)] = reference_string[i]
            page_faults += 1

            print(f"{page_faults}번째 페이지 폴트: {frame}")


    hit_count = len(reference_string) - page_faults

    print("\nHit 발생 횟수:", hit_count)
    print("Page Fault 발생 횟수:", page_faults)
    print("Page Fault Rate (%):", (page_faults / len(reference_string)) * 100)

def find_optimal_page(reference_string, frame, start_index):
    farthest_index = -1
    page_to_replace = None

    for page in frame:
        if page not in reference_string[start_index:]:
            return page
        else:
            index = reference_string.index(page, start_index)
            if index > farthest_index:
                farthest_index = index
                page_to_replace = page

    return page_to_replace

