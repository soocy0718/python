def solution(store, customer):
    answer = []
    for i in customer:
      if i in store:
        answer.append('yes')
      else:
        answer.append('no')
    return answer