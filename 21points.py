import random

def draw_card():
    """返回一張回機的牌"""
    return random.randint(1, 11)

def calculate_hand(hand):
    """計算玩家牌的數"""
    total = sum(hand)
    # A牌要1還是11
    if total > 21 and 11 in hand:
        total -= 10
    return total

def play_blackjack():
    bank = int(input('輸入一開始的點數:'))
    while bank > 0:
        print(f"\n你目前的點數為: {bank}")
        bet = int(input("輸入下你得注金額: "))
        if bet <= 0 or bet > bank:
            print("下注金額無效，請重新輸入:")
            continue
        
        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), draw_card()]

        print(f"你的牌為: {player_hand} 總共是: {calculate_hand(player_hand)}")
        print(f"莊家的第一張牌: {dealer_hand[0]}")

        # 玩家回合
        while True:
            action = input("要牌請輸入[Y]，停牌請輸入[N]:").upper()
            if action == 'Y':
                player_hand.append(draw_card())
                print(f"你的牌為: {player_hand} 總共是: {calculate_hand(player_hand)}")
                if calculate_hand(player_hand) > 21:
                    print("爆了啦:>")
                    bank -= bet
                    break
            elif action == 'N':
                break
            else:
                print("輸入無效，請重新輸入:")

        if calculate_hand(player_hand) <= 21:
            # 莊家的時候
            print(f"莊家的牌為: {dealer_hand} 總共是: {calculate_hand(dealer_hand)}")
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(draw_card())
                import time
                time.sleep(2.3)
                print(f"莊家的牌為: {dealer_hand} 總共是: {calculate_hand(dealer_hand)}")
            
            player_total = calculate_hand(player_hand)
            dealer_total = calculate_hand(dealer_hand)
            import time
            time.sleep(2)
            
            if dealer_total > 21 or player_total > dealer_total:
                print("恭喜你赢了！")
                bank += bet
            elif player_total < dealer_total:
                print("你輸了！")
                bank -= bet
            else:
                print("平局！")
        
        if bank > 0:
            print('目前點數為:',bank)
            cont = input("繼續請輸入[Y] 退出請輸入[N]:").upper()
            if cont != 'Y':
                break
    
    print("遊戲結束，最終點數為", bank)

if __name__ == "__main__":
    play_blackjack()
