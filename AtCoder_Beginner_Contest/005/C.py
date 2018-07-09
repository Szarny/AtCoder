def main():
    T = int(input())

    n_takoyaki = int(input())
    takoyaki_list = [int(_) for _ in input().split()]

    n_customer = int(input())
    customer_list = [int(_) for _ in input().split()]

    if n_takoyaki < n_customer:
        print("no")
        return

    for customer in customer_list:
        is_processable = False
        for takoyaki in takoyaki_list:

            if 0 <= customer - takoyaki <= T:
                takoyaki_list.remove(takoyaki)
                is_processable = True
                break

        if not is_processable:
            print("no")
            return

    print("yes")
    return

main()
