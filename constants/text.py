home_slogan = """
    <h1 style='text-align: center; color: black;'>
        <b>停車位一點通，找車位更輕鬆</b>
        </h1>
    <h4 style='text-align: center; color: black;'>
        ParkFinder，助您即時查詢、追蹤統計台北市停車場的可用停車位
        </h4>
    """

home_title1 = """
    <h2 style='text-align: center; color: grey;'><b>兩大使用場景</b></h2>
    """

home_case1_title = """
    <h3 style='text-align: left; color: black;'><b>鎖定空閒停車場</b></h3>
    """
home_case1_text = """
    <p style='text-align: left; color: black;'>
        「明天要去看電影時，附近哪一個停車場比較會有停車位？」、
        「下週一中午只有一小時處理這些事情，哪個停車場可以讓我迅速找到停車位，節省時間和油費？」、
        「在規劃這個週末的聖誕夜活動時，如果能知道我想去的景點附近通常哪個停車場會比較有停車位，我就能更有效率地安排行程！」...
        讓 ParkFinder 來協助您回答這些問題吧！
    </p>
    """
home_case1_expander = """
    <p style='text-align: left; color: black;'>
        台北市政府提供之停車資訊 API，只有即時的資訊。
        對於需要提前規畫行程的人來說，過去某時段平均剩餘空位才是比較有價值的。
    </p>
    <p style='text-align: left; color: black;'>
        ParkFinder 持續蒐集歷史資料，並提供歷史統計數據，為謹慎行事的您提供最有價值的安排！
    </p>
    """

home_case2_title = """
    <h3 style='text-align: left; color: black;'><b>購買停車場月票</b></h3>
    """
home_case2_text = """
    <p style='text-align: left; color: black;'>
        「我家附近真的只有這一處停車場適合抽籤嗎？」、
        「平常上班需要停車的時候，會不會我抽到的停車場剛好都沒有車位？」、
        「與其選擇這一處比較近的停車場，該不會多走五分鐘就能到的另一處停車場會有更多車位？」...
        讓 ParkFinder 來協助您回答這些問題吧！
    </p>
    """
home_case2_expander = """
    <p style='text-align: left; color: black;'>
        臺北市公有路外停車場因租金優惠廣受歡迎，卻也因此導致月票的購買以及運作相當複雜。以下三個障礙使得離車主最近的停車場有時不一定會是最好的目標：
    </p>
    <ol>
        <li> 車主每個月都必須經過<b>電腦抽籤</b>的篩選才能獲得購買月票的資格 </li>
        <li> 登記系統規定同一車號最多只能<b>登記 2 處停車場</b>進行抽籤</li>
        <li> 月票僅僅是停車場的入場券，擁有月票的車主們仍必須依<b>先到先停為原則</b>搶奪稀有的車位</li>
    </ol>
    <link style='text-align: left; color: black;'>
        資料來源: <a href="https://monthtkt.pma.gov.tw/park/">臺北市政府停車管理工程處-路外月票抽籤</a>
    </p>
    """


home_title2 = """
    <h2 style='text-align: center; color: grey;'><b>四大常用功能</b></h2>
    """

home_func1_title = """
    <h3 style='text-align: left; color: black;'><b>追蹤趨勢變化</b></h3>
    """
home_func1_text = """
    <p style='text-align: left; color: black;'>
        針對特定停車場，統計工作日與週末的平均剩餘車位，以解決如工作日下班時段，會不會沒有車位可停的疑慮。
    </p>
    """

home_func2_title = """
    <h3 style='text-align: left; color: black;'><b>比較數量差異</b></h3>
    """
home_func2_text = """
    <p style='text-align: left; color: black;'>
        同時聚焦多個停車場，比較同一時段剩餘車位的數量差異，用以制定最佳的停車場月票購買策略。
    </p>
    """

home_func3_title = """
    <h3 style='text-align: left; color: black;'><b>查詢歷史資料</b></h3>
    """
home_func3_text = """
    <p style='text-align: left; color: black;'>
        完整紀錄個別停車場的歷史可停車位資料，隨時查閱最精準的數據。
    </p>
    """

home_func4_title = """
    <h3 style='text-align: left; color: black;'><b>整合地圖資訊</b></h3>
    """
home_func4_text = """
    <p style='text-align: left; color: black;'>
        結合地理資訊視覺化，快速掌握特定區域內各停車場的可停車位數，以最有效率的方式尋找理想目標。
    </p>
    """

tech_title1 = """
    <h2 style='text-align: center; color: grey;'><b>自動化、蒐集、儲存</b></h2>
    """

tech_logo1 = """
    <p style='text-align: left; color: black;'>
        在 AWS 上建立 EC2 實例，令其以每 5 分鐘的間隔自動採集數據，將收集到的資訊存儲在雲端伺服器中。
    </p>
    """
tech_logo2 = """
    <p style='text-align: left; color: black;'>
        整合臺北市政府停車場資訊導引系統的
        <a href="https://tpis.pma.gov.tw/ParkInfo/">API</a>，
        實現即時停車場資訊的串接，以提供最及時的停車場資訊。
    </p>
    """
tech_logo3 = """
    <p style='text-align: left; color: black;'>
        透過 SQL 建立關聯式資料庫，有效處理資料流，並積累即時資料轉換為歷史資料，以呈現更全面的資訊紀錄。
    </p>
    """

tech_title2 = """
    <h2 style='text-align: center; color: grey;'><b>分析、視覺化、互動式操作</b></h2>
    """

tech_logo4 = """
    <p style='text-align: left; color: black;'>
        應用 Pandas 執行資料處理與資料分析，彙整各停車場的可用停車位資訊，以產生直觀易懂的統計數據。
    </p>
    """
tech_logo5 = """
    <p style='text-align: left; color: black;'>
        運用 Plotly 與 Mapbox 創建多樣化的視覺化工具，以互動式介面提供所需的關鍵資訊，協助做出最佳決策。
    </p>
    """
tech_logo6 = """
    <p style='text-align: left; color: black;'>
        架設 Streamlit 網站，提供使用者在任何時間、任何地點都能進行分析的操作工具。
    </p>
    """

about_name1 = """
    <h2 style='text-align: left; color: black;'><b>羅偉駿 Alex Lo</b></h2>
    """
about_link1 = """
        [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/charliealex123/)
        [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/CharlieAlex)
        [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@asdfghjkl12345zz6)
        """
about_intro1 = """
    <p style='text-align: left; color: black;'>
        台大經研所碩士，
        曾於蝦皮、露天等電商實習，
        負責資料蒐集、整理與分析，
        喜歡學習新事物，
        正在服兵役...
    </p>
    """

about_name2 = """
    <h2 style='text-align: left; color: black;'><b>陳家威 Teddy Chen</b></h2>
    """
about_link2 = """
        [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chiaweichen/)
        [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/teddy21019)
        [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@ted21019)
        """
about_intro2 = """
    <p style='text-align: left; color: black;'>
        （差點不能）台大經濟研究所畢業，
        沉迷於因果推論與計量，
        喜歡自行搜集數據解決問題，
        正在尋找資料科學家的相關職缺。
    </p>
    """