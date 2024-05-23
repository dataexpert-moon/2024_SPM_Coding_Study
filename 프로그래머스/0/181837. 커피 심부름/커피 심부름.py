def solution(order):
    total = 0
    # 아메리카노, 카페라테 메뉴 딕셔너리 형태로 만들기
    cafe_menu = {'iceamericano': 4500, 'americanoice': 4500,
                 'americano': 4500, 'anything': 4500,
                 'hotamericano': 4500, 'americanohot': 4500,
                'icecafelatte': 5000, 'cafelatteice': 5000,
                'hotcafelatte': 5000, 'cafelattehot': 5000,
                'cafelatte': 5000}
    
    for one_order in order:
        total += cafe_menu.get(one_order) # key로 value 얻기 - get
    
    return total