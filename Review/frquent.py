def find_most_frequent_number_naive(numbers):
    # O(N^2) 접근: 각 숫자마다 전체 배열을 다시 확인해야 한다!

    # 아직 가장 많이 나온 수와 횟수를 모르니 0과 None 으로 초기화한다.
    max_count = 0
    most_frequent = None

    # 배열에서 숫자를 하나씩 꺼낸다.
    # numbers 가 [1, 2, 3, 2, 1, 3, 1, 4, 2, 1] 라면,
    # num 은 1, 2, 3, 2, ... 가 될 것이다.
    for num in numbers:

        # 현재 숫자가 몇 번 나왔는지 기록한다.
        current_count = 0

        # 배열을 처음부터 끝까지 다시 보면서 현재 숫자와 같은지 확인한다.
        for compare_num in numbers:
            if num == compare_num:
                current_count += 1

        # 방금 센 숫자가 지금까지 본 것 중 가장 많이 나온 거라면
        if current_count > max_count:
            # 최댓값을 업데이트하고
            max_count = current_count
            # 해당 숫자를 저장한다.
            most_frequent = num

    # 가장 많이 나온 숫자와 횟수를 반환한다.
    return most_frequent, max_count


def find_most_frequent_number_optimal(numbers):
    # O(N) 접근: 딕셔너리를 사용해서 배열을 한 번만 순회한다.

    # 각 숫자가 몇 번 나왔는지 저장할 딕셔너리를 만든다.
    # 예: {1: 3, 2: 2}는 1이 3번, 2가 2번 나왔다는 뜻이다.
    count_dict = {}

    # 배열을 한 번만 돌면서
    for num in numbers:
        # 숫자를 본 적이 있다면 횟수를 1 증가
        if num in count_dict:
            count_dict[num] += 1
        # 처음 보는 숫자라면 1부터 시작
        else:
            count_dict[num] = 1

    # 기록을 바탕으로 가장 많이 나온 숫자와 횟수를 찾는다.
    most_frequent = None
    max_count = 0

    # 딕셔너리에 저장된 모든 숫자와 횟수를 확인
    for num, count in count_dict.items():
        # 현재 숫자가 지금까지 본 것보다 더 많이 나왔다면
        if count > max_count:
            # 최댓값을 업데이트하고
            max_count = count
            # 해당 숫자를 저장한다.
            most_frequent = num

    return most_frequent, max_count


# 실행 결과:
# 입력된 숫자 목록: [1, 2, 3, 2, 1, 3, 1, 4, 2, 1]
#
# 첫 번째 방법(느린 방법)의 결과:
# 가장 많이 나온 숫자는 1이고, 4번 나왔어요!
#
# 두 번째 방법(빠른 방법)의 결과:
# 가장 많이 나온 숫자는 1이고, 4번 나왔어요!

numbers = [1, 2, 3, 2, 1, 3, 1, 4, 2, 1]
print("입력된 숫자 목록:", numbers)
print("\n첫 번째 방법(느린 방법)의 결과:")
number, count = find_most_frequent_number_naive(numbers)
print(f"가장 많이 나온 숫자는 {number}이고, {count}번 나왔어요!")

print("\n두 번째 방법(빠른 방법)의 결과:")
number, count = find_most_frequent_number_optimal(numbers)
print(f"가장 많이 나온 숫자는 {number}이고, {count}번 나왔어요!")

# 데이터가 1만개 이고, 한 번 실행당 1초가 걸린다면,
# 느린 방법은 27777시간 46분 40초가 걸리며,
# 빠른 방법은 2시간 46분 40초가 걸린다.

# 빠른 알고리즘의 경우 for문이 두개 있어서 O(2N) 으로 생각할 수 있다.
# 시간 복잡도에서 N앞에 배수(2N, 3N, 4N, ...), 뒤에 상수(N+2, N+1000, ...)는
# 모두 무시되며, 그냥 O(N)으로 표기한다.