
from library import fifo
from library import opt
from library import lru

if __name__ == "__main__":

    while True:
        print("\n가상 메모리 교체 정책 선택\n")
        choice = int(input("1: FIFO / 2: OPT / 3: LRU / 4: LRU (Second Chance) / 5: 종료 -> "))

        # 강의자료 참조열 예제: 70120304230321201701

        if choice == 1:
            reference_string = str(input("참조열 입력 -> "))
            frame_size = int(input("프레임 사이즈 입력 -> "))
            print()
            fifo.simulate_fifo(reference_string, frame_size)

        elif choice == 2:
            reference_string = str(input("참조열 입력 -> "))
            frame_size = int(input("프레임 사이즈 입력 -> "))
            print()
            opt.simulate_opt(reference_string, frame_size)

        elif choice == 3:
            reference_string = str(input("참조열 입력 -> "))
            frame_size = int(input("프레임 사이즈 입력 -> "))
            print()
            lru.simulate_lru(reference_string, frame_size)

        elif choice == 4:
            reference_string = str(input("참조열 입력 -> "))
            frame_size = int(input("프레임 사이즈 입력 -> "))
            print()
            lru.simulate_second_chance(reference_string, frame_size)

        else:
            exit()
