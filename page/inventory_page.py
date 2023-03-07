class InventoryPage:
    my_inventory = "xpath=//html/body/div[2]/div/div/div[1]/div/ul/li[7]/a/span"
    select_goods = "xpath=//html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/label/span[1]/input"
    grounding_but = "xpath=//html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/button[3]"
    show_all = "text=显示全部"
    show_can_sale = "text=显示可出售"
    pricing_sale = "xpath=//html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/input"
    max_day = "xpath=//html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/input"
    short_rental = "xpath=//html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div/div[2]/input"
    antecedent_money = "xpath=//html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div[3]/div[2]/div/div[2]/input"
    charter_money = "text=只卖不租"

    add_comment = "[placeholder=点我添加描述]"
    confirm_grounding_but = "text=确认上架"
    only_sale = "text=只卖不租"
    # confirm = 'document.getElementsByClassName("ant-btn ant-btn-primary")[5].click()'
    confirm = "text=确 认"
    msg = "text=上架成功"
