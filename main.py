def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    cut = int(input())
    a = int(input())
    b = int(input())

    infected = a
    infected_last = a
    result = 0

    while infected <= cut:
        result += 1
        infected += infected_last * b
        infected_last *= b

    print(result)

    # songs = 'ABCDE'
    # button = 0
    # presses = 1
    #
    # while button != 4:
    #     button = int(input())
    #     presses = int(input())
    #     for i in range(presses):
    #         if button == 1:
    #             songs = songs[1:] + songs[0]
    #         elif button == 2:
    #             songs = songs[-1] + songs[:-1]
    #         elif button == 3:
    #             songs = songs[1] + songs[0] + songs[2:]
    #
    # result = ''
    # for a in songs:
    #     result = result + a + ' '
    #
    # print(result[:9])