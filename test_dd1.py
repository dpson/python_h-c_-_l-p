list_dr.append(list[i+1])
            print(list_dr)
            i=i+1
        elif (list[i+1]-list[i]) > max_count:
            fail_cnt += 1
            if fail_cnt <2:
                list_dr.append(list[i+1])
                
                print(list_dr)
                i=i+1
            else:
                break
               
          
       
             
           


