import test

if __name__ == "__main__":
    # test.test_wrapper("[]", True)
    # test.test_wrapper("[]]", False)
    test.test_wrapper("({[]})", True)

    # received = input('lil bitch boi\t')

    # print(f'Received  = {received}')
    # while received not in ['q', 'Q', 'Quit', 'quit']:
    #     truthy_return = input('T/F bitch\n')
    #     if truthy_return in ['t', 'T']:
    #         truthy_return = True
    #     else:
    #         truthy_return = False

    #     test.test_wrapper(received, truthy_return)

    #     received = input('Put in the shit bitch\n')
