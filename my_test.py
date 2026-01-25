sales_data = [ # منطقه شمال
    [ # فروشگاه A
        [  # محصولات: [الکترونیک، پوشاک، مواد غذایی]
            [100, 200, 300],
            [150, 250, 350]   # فروش سه ماهه
        ],
        [  # فروشگاه B  
            [80, 180, 280],
            [120, 220, 320]
        ]
    ],
    [  # منطقه جنوب
        [
            [90, 190, 290],
            [130, 230, 330]
        ],
        [
            [70, 170, 270],
            [110, 210, 310]
        ]
    ]
]

answer = [shop[0][0]
          for regin in sales_data
          for shop in regin]


electronics = [shop[0][0]  # اولین عدد از هر فروشگاه
              for region in sales_data
              for shop in region]

print(electronics)  # [100, 150, 80, 120, 90, 130, 70, 110]


print(answer)