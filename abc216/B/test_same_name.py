import same_name

def test_detect_same_name_1():
    name_list = ["tanaka taro"
                ,"sato hanako"
                ,"tanaka taro"]
    ans = same_name.detect_same_name(name_list)
    assert ans == "Yes"

def test_detect_same_name_2():
    name_list = ["saito ichiro"
                 ,"saito jiro"
                 ,"saito saburo"]
    ans = same_name.detect_same_name(name_list)
    assert ans == "No"

def test_detect_same_name_3():
    name_list = ["sypdgidop bkseq"
                "bajsqz hh"
                "ozjekw mcybmtt"
                "qfeysvw dbo"]
    ans = same_name.detect_same_name(name_list)
    assert ans == "No"