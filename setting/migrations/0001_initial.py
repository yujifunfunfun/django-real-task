# Generated by Django 3.1.6 on 2021-06-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(choices=[], default='', max_length=100, verbose_name='アカウントID')),
                ('auction_mode', models.CharField(choices=[('オークション', 'オークション'), ('フリマ', 'フリマ')], default='オークション', max_length=10, verbose_name='オークション/フリマ選択')),
                ('units', models.IntegerField(default=1, verbose_name='個数')),
                ('kaisai_kikan', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=1, verbose_name='開催期間')),
                ('end_time', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)], default=22, verbose_name='終了時間')),
                ('shipping_address', models.CharField(choices=[('海外', '海外'), ('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], default='東京都', max_length=10, verbose_name='商品発送元の都道府県')),
                ('souryou_futan', models.CharField(choices=[('落札者', '落札者'), ('出品者', '出品者')], default='落札者', max_length=10, verbose_name='送料負担')),
                ('item_condition', models.CharField(default='未使用', max_length=10, verbose_name='商品の状態')),
                ('hyouka_seigen', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='いいえ', max_length=10, verbose_name='入札者評価制限')),
                ('bad_hyouka_seigen', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='いいえ', max_length=10, verbose_name='悪い評価の割合での制限')),
                ('nyuusatsusya_ninsyou_seigen', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='いいえ', max_length=10, verbose_name='入札者認証制限')),
                ('auto_extention', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='はい', max_length=10, verbose_name='自動延長')),
                ('fast_end', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='はい', max_length=10, verbose_name='早期終了')),
                ('auto_saisyuppin', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=3, verbose_name='自動再出品')),
                ('shipping_date', models.CharField(choices=[('1〜2日', '1〜2日'), ('2〜3日', '2〜3日'), ('7〜13日', '7〜13日'), ('14日以降', '14日以降')], default='2～3日', max_length=10, verbose_name='発送までの日数')),
                ('other_shipping_method', models.CharField(default='委託配送会社', max_length=20, verbose_name='配送方法１')),
                ('other_shipping_price', models.IntegerField(default=1200, verbose_name='配送方法１の一律価格')),
                ('description_template', models.TextField(default='<CENTER>$$description$$</CENTER>', verbose_name='説明文テンプレート(\u3000$$description$$\u3000を商品説明を入れたい箇所に入力してください)')),
                ('syuppin_sleep_sec', models.IntegerField(default=5, verbose_name='出品毎の待ち時間(秒)')),
            ],
            options={
                'db_table': 'sample',
            },
        ),
    ]