 if fail_cnt < 2:
                fail_cnt += 1
                list_dr.append(list[i+1])
                print(list_dr)
                i=i+1
            else:
                break
        else:
            list_dr.append(list[i+1])
            print(list_dr)
            i=i+1
