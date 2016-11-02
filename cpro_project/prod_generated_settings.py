import datetime
TOTAL_DONATORS = 15
LATEST_NEWS = [{'url': u'/event/39/LIVE-Groove-Dance-Burst-4/', 'hide_title': True, 'image': u'//i.cinderella.pro/u/e/WfjRjALive-Groove-Dance-Burst-4.png', 'ajax': u'/ajax/event/39/', 'title': u'LIVE Groove Dance burst'}]
FAVORITE_CHARACTERS = [(154L, u'Abe Nana', u'//i.cinderella.pro/u/c/puchi/100037R-Abe-Nana-Cute.png'), (263L, u'Aiba Yumi', u'//i.cinderella.pro/u/c/puchi/300089N-Aiba-Yumi-Passion.png'), (172L, u'Aikawa Chinatsu', u'//i.cinderella.pro/u/c/puchi/200005N-Aikawa-Chinatsu-Cool.png'), (244L, u'Aino Nagisa', u'//i.cinderella.pro/u/c/puchi/300237N-Aino-Nagisa-Passion.png'), (243L, u'Akagi Miria', u'//i.cinderella.pro/u/c/puchi/300013N-Akagi-Miria-Passion.png'), (227L, u'Anastasia', u'//i.cinderella.pro/u/c/puchi/200039R-Anastasia-Cool.png'), (151L, u'Anzai Miyako', u'//i.cinderella.pro/u/c/puchi/100273N-Anzai-Miyako-Cute.png'), (176L, u'Araki Hina', u'//i.cinderella.pro/u/c/puchi/200013N-Araki-Hina-Cool.png'), (163L, u'Ariura Kanna', u'//i.cinderella.pro/u/c/puchi/100221R-Ariura-Kanna-Cute.png'), (305L, u'Asano Fuka', u'//i.cinderella.pro/u/i/vITyBwAsano-Fuka.png'), (192L, u'Asari Nanami', u'//i.cinderella.pro/u/c/puchi/220225N-Asari-Nanami-Cool.png'), (204L, u'Ayase Honoka', u'//i.cinderella.pro/u/c/puchi/200077R-Ayase-Honoka-Cool.png'), (158L, u'Clarice', u'//i.cinderella.pro/u/c/puchi/100105R-Clarice-Cute.png'), (141L, u'Domyoji Karin', u'//i.cinderella.pro/u/c/puchi/100079R-Domyoji-Karin-Cute.png'), (307L, u'Ebihara Naho', u'//i.cinderella.pro/u/i/ug4KSyEbihara-Naho.png'), (255L, u'Eto Misaki', u'//i.cinderella.pro/u/c/puchi/300257R-Eto-Misaki-Passion.png'), (219L, u'Fujii Tomo', u'//i.cinderella.pro/u/c/puchi/200177R-Fujii-Tomo-Cool.png'), (122L, u'Fujimoto Rina', u'//i.cinderella.pro/u/c/puchi/100071N-Fujimoto-Rina-Cute.png'), (184L, u'Fujiwara Hajime', u'//i.cinderella.pro/u/c/puchi/200135N-Fujiwara-Hajime-Cool.png'), (104L, u'Fukuyama Mai', u'//i.cinderella.pro/u/c/puchi/100069N-Fukuyama-Mai-Cute.png'), (187L, u'Furusawa Yoriko', u'//i.cinderella.pro/u/c/puchi/200267R-Furusawa-Yoriko-Cool.png'), (134L, u'Futaba Anzu', u'//i.cinderella.pro/u/c/puchi/100027R-Futaba-Anzu-Cute.png'), (292L, u'Hamaguchi Ayame', u'//i.cinderella.pro/u/c/puchi/300093R-Hamaguchi-Ayame-Passion.png'), (304L, u'Hamakawa Ayuna', u'//i.cinderella.pro/u/i/Ta0cvmHamakawa-Ayuna.png'), (165L, u'Harada Miyo', u'//i.cinderella.pro/u/c/puchi/100133R-Harada-Miyo-Cute.png'), (182L, u'Hattori Toko', u'//i.cinderella.pro/u/c/puchi/200289R-Hattori-Toko-Cool.png'), (223L, u'Hayami Kanade', u'//i.cinderella.pro/u/c/puchi/200037R-Hayami-Kanade-Cool.png'), (162L, u'Hayasaka Mirei', u'//i.cinderella.pro/u/c/puchi/100143R-Hayasaka-Mirei-Cute.png'), (247L, u'Himekawa Yuki', u'//i.cinderella.pro/u/c/puchi/300017N-Himekawa-Yuki-Passion.png'), (270L, u'Hino Akane', u'//i.cinderella.pro/u/c/puchi/300031R-Hino-Akane-Passion.png'), (201L, u'Hojo Karen', u'//i.cinderella.pro/u/c/puchi/200027R-Hojo-Karen-Cool.png'), (234L, u'Honda Mio', u'//i.cinderella.pro/u/c/puchi/300001R-Honda-Mio-Passion.png'), (258L, u'Hori Yuko', u'//i.cinderella.pro/u/c/puchi/300021N-Hori-Yuko-Passion.png'), (256L, u'Hoshi Syoko', u'//i.cinderella.pro/u/c/puchi/300069N-Hoshi-Syoko-Passion.png'), (139L, u'Hyodo Rena', u'//i.cinderella.pro/u/c/puchi/100129R-Hyodo-Rena-Cute.png'), (283L, u'Ichihara Nina', u'//i.cinderella.pro/u/c/puchi/300113R-Ichihara-Nina-Passion.png'), (126L, u'Ichinose Shiki', u'//i.cinderella.pro/u/c/puchi/100087N-Ichinose-Shiki-Cute.png'), (113L, u'Igarashi Kyoko', u'//i.cinderella.pro/u/c/puchi/100099N-Igarashi-Kyoko-Cute.png'), (106L, u'Imai Kana', u'//i.cinderella.pro/u/c/puchi/100141N-Imai-Kana-Cute.png'), (147L, u'Imura Setsuna', u'//i.cinderella.pro/u/c/puchi/100131R-Imura-Setsuna-Cute.png'), (267L, u'Jougasaki Mika', u'//i.cinderella.pro/u/c/puchi/300027R-Jougasaki-Mika-Passion.png'), (268L, u'Jougasaki Rika', u'//i.cinderella.pro/u/c/puchi/300029R-Jougasaki-Rika-Passion.png'), (175L, u'Kamijo Haruna', u'//i.cinderella.pro/u/c/puchi/200011N-Kamijo-Haruna-Cool.png'), (174L, u'Kamiya Nao', u'//i.cinderella.pro/u/c/puchi/200009N-Kamiya-Nao-Cool.png'), (198L, u'Kanzaki Ranko', u'//i.cinderella.pro/u/c/puchi/200025R-Kanzaki-Ranko-Cool.png'), (257L, u'Katagiri Sanae', u'//i.cinderella.pro/u/c/puchi/300073N-Katagiri-Sanae-Passion.png'), (202L, u'Kate', u'//i.cinderella.pro/u/c/puchi/200029R-Kate-Cool.png'), (173L, u'Kawashima Mizuki', u'//i.cinderella.pro/u/c/puchi/200007N-Kawashima-Mizuki-Cool.png'), (183L, u'Kiba Manami', u'//i.cinderella.pro/u/c/puchi/220231R-Kiba-Manami-Cool.png'), (238L, u'Kimura Natsuki', u'//i.cinderella.pro/u/c/puchi/300009N-Kimura-Natsuki-Passion.png'), (170L, u'Kirino Aya', u'//i.cinderella.pro/u/c/puchi/200273N-Kirino-Aya-Cool.png'), (231L, u'Kiryu Tsukasa', u'//i.cinderella.pro/u/c/puchi/200279R-Kiryu-Tsukasa-Cool.png'), (303L, u'Kishibe Ayaka', u'//i.cinderella.pro/u/i/c6SBGKKishibe-Ayaka.png'), (284L, u'Kita Hinako', u'//i.cinderella.pro/u/c/puchi/300121R-Kita-Hinako-Passion.png'), (286L, u'Kitagawa Mahiro', u'//i.cinderella.pro/u/c/puchi/300211R-Kitagawa-Mahiro-Passion.png'), (249L, u'Kitami Yuzu', u'//i.cinderella.pro/u/c/puchi/300127N-Kitami-Yuzu-Passion.png'), (132L, u'Kobayakawa Sae', u'//i.cinderella.pro/u/c/puchi/100023R-Kobayakawa-Sae-Cute.png'), (157L, u'Koga Koharu', u'//i.cinderella.pro/u/c/puchi/100287N-Koga-Koharu-Cute.png'), (111L, u'Kohinata Miho', u'//i.cinderella.pro/u/c/puchi/100013N-Kohinata-Miho-Cute.png'), (288L, u'Komatsu Ibuki', u'//i.cinderella.pro/u/c/puchi/300189R-Komatsu-Ibuki-Passion.png'), (254L, u'Koseki Reina', u'//i.cinderella.pro/u/c/puchi/300177R-Koseki-Reina-Passion.png'), (150L, u'Koshimizu Sachiko', u'//i.cinderella.pro/u/c/puchi/100073R-Koshimizu-Sachiko-Cute.png'), (155L, u'Kudo Shinobu', u'//i.cinderella.pro/u/c/puchi/100113R-Kudo-Shinobu-Cute.png'), (156L, u'Kurihara Nene', u'//i.cinderella.pro/u/c/puchi/100247R-Kurihara-Nene-Cute.png'), (168L, u'Kurokawa Chiaki', u'//i.cinderella.pro/u/c/puchi/200003N-Kurokawa-Chiaki-Cool.png'), (191L, u'Layla', u'//i.cinderella.pro/u/c/puchi/200161R-Layla-Cool.png'), (127L, u'Maekawa Miku', u'//i.cinderella.pro/u/c/puchi/100019R-Maekawa-Miku-Cute.png'), (275L, u'Makihara Shiho', u'//i.cinderella.pro/u/c/puchi/300255R-Makihara-Shiho-Passion.png'), (287L, u'Mary Cochran', u'//i.cinderella.pro/u/c/puchi/300099R-Mary-Cochran-Passion.png'), (260L, u'Matoba Risa', u'//i.cinderella.pro/u/c/puchi/300155N-Matoba-Risa-Passion.png'), (129L, u'Matsubara Saya', u'//i.cinderella.pro/u/c/puchi/100217R-Matsubara-Saya-Cute.png'), (169L, u'Matsumoto Sarina', u'//i.cinderella.pro/u/c/puchi/200069N-Matsumoto-Sarina-Cool.png'), (194L, u'Matsunaga Ryo', u'//i.cinderella.pro/u/c/puchi/200021R-Matsunaga-Ryo-Cool.png'), (225L, u'Matsuo Chizuru', u'//i.cinderella.pro/u/c/puchi/200285N-Matsuo-Chizuru-Cool.png'), (239L, u'Matsuyama Kumiko', u'//i.cinderella.pro/u/c/puchi/300011N-Matsuyama-Kumiko-Passion.png'), (181L, u'Mifune Miyu', u'//i.cinderella.pro/u/c/puchi/200123N-Mifune-Miyu-Cool.png'), (108L, u'Mimura Kanako', u'//i.cinderella.pro/u/c/puchi/100007N-Mimura-Kanako-Cute.png'), (131L, u'Miyamoto Frederica', u'//i.cinderella.pro/u/c/puchi/100021R-Miyamoto-Frederica-Cute.png'), (289L, u'Miyoshi Sana', u'//i.cinderella.pro/u/c/puchi/300157R-Miyoshi-Sana-Passion.png'), (179L, u'Mizuki Seira', u'//i.cinderella.pro/u/c/puchi/200155N-Mizuki-Seira-Cool.png'), (103L, u'Mizumoto Yukari', u'//i.cinderella.pro/u/c/puchi/100065N-Mizumoto-Yukari-Cute.png'), (186L, u'Mizuno Midori', u'//i.cinderella.pro/u/c/puchi/200185R-Mizuno-Midori-Cool.png'), (107L, u'Mochida Arisa', u'//i.cinderella.pro/u/c/puchi/100005N-Mochida-Arisa-Cute.png'), (136L, u'Momoi Azuki', u'//i.cinderella.pro/u/c/puchi/100081R-Momoi-Azuki-Cute.png'), (226L, u'Morikubo Nono', u'//i.cinderella.pro/u/c/puchi/200119R-Morikubo-Nono-Cool.png'), (271L, u'Moroboshi Kirari', u'//i.cinderella.pro/u/c/puchi/300033R-Moroboshi-Kirari-Passion.png'), (280L, u'Mukai Takumi', u'//i.cinderella.pro/u/c/puchi/300105R-Mukai-Takumi-Passion.png'), (121L, u'Munakata Atsumi', u'//i.cinderella.pro/u/c/puchi/100159N-Munakata-Atsumi-Cute.png'), (293L, u'Murakami Tomoe', u'//i.cinderella.pro/u/c/puchi/300129R-Murakami-Tomoe-Passion.png'), (160L, u'Muramatsu Sakura', u'//i.cinderella.pro/u/c/puchi/100151R-Muramatsu-Sakura-Cute.png'), (302L, u'Nagatomi Hasumi', u'//i.cinderella.pro/u/i/9Dd66oNagatomi-Hasumi.png'), (102L, u'Nakano Yuka', u'//i.cinderella.pro/u/c/puchi/100003N-Nakano-Yuka-Cute.png'), (291L, u'Namba Emi', u'//i.cinderella.pro/u/c/puchi/300145R-Nanba-Emi-Passion.png'), (236L, u'Namiki Meiko', u'//i.cinderella.pro/u/c/puchi/300199R-Namiki-Meiko-Passion.png'), (298L, u'Nanjo Hikaru', u'//i.cinderella.pro/u/c/puchi/300245R-Nanjo-Hikaru-Passion.png'), (218L, u'Narumiya Yume', u'//i.cinderella.pro/u/c/puchi/200195N-Narumiya-Yume-Cool.png'), (273L, u'Natalia', u'//i.cinderella.pro/u/c/puchi/300075R-Natalia-Passion.png'), (230L, u'Ninomiya Asuka', u'//i.cinderella.pro/u/c/puchi/200093R-Ninomiya-Asuka-Cool.png'), (259L, u'Nishijima Kai', u'//i.cinderella.pro/u/c/puchi/300231R-Nishijima-Kai-Passion.png'), (308L, u'Nishikawa Honami', u'//i.cinderella.pro/u/i/zCcivlNishikawa-Honami.png'), (185L, u'Nitta Minami', u'//i.cinderella.pro/u/c/puchi/200019N-Nitta-Minami-Cool.png'), (264L, u'Nonomura Sora', u'//i.cinderella.pro/u/c/puchi/300023R-Nonomura-Sora-Passion.png'), (112L, u'Ogata Chieri', u'//i.cinderella.pro/u/c/puchi/100015N-Ogata-Chieri-Cute.png'), (246L, u'Ohtsuki Yui', u'//i.cinderella.pro/u/c/puchi/300015N-Ootsuki-Yui-Passion.png'), (253L, u'Oikawa Shizuku', u'//i.cinderella.pro/u/c/puchi/300071N-Oikawa-Shizuku-Passion.png'), (222L, u'Okazaki Yasuha', u'//i.cinderella.pro/u/c/puchi/200153R-Okazaki-Yasuha-Cool.png'), (109L, u'Okuyama Saori', u'//i.cinderella.pro/u/c/puchi/100009N-Okuyama-Saori-Cute.png'), (123L, u'Oohara Michiru', u'//i.cinderella.pro/u/c/puchi/100233N-Oohara-Michiru-Cute.png'), (224L, u'Ooishi Izumi', u'//i.cinderella.pro/u/c/puchi/200145R-Ooishi-Izumi-Cool.png'), (153L, u'Oonishi Yuriko', u'//i.cinderella.pro/u/c/puchi/100237R-Oonishi-Yuriko-Cute.png'), (125L, u'Oonuma Kurumi', u'//i.cinderella.pro/u/c/puchi/100265R-Oonuma-Kurumi-Cute.png'), (120L, u'Oota Yu', u'//i.cinderella.pro/u/c/puchi/100257N-Oota-Yu-Cute.png'), (164L, u'Otokura Yuuki', u'//i.cinderella.pro/u/c/puchi/100213N-Otokura-Yuuki-Cute.png'), (237L, u'Ryuzaki Kaoru', u'//i.cinderella.pro/u/c/puchi/300007N-Ryuzaki-Kaoru-Passion.png'), (189L, u'Sagisawa Fumika', u'//i.cinderella.pro/u/c/puchi/200091N-Sagisawa-Fumika-Cool.png'), (133L, u'Saionji Kotoka', u'//i.cinderella.pro/u/c/puchi/100025R-Saionji-Kotoka-Cute.png'), (240L, u'Saito Yoko', u'//i.cinderella.pro/u/c/puchi/320223N-Saito-Yoko-Passion.png'), (205L, u'Sajo Yukimi', u'//i.cinderella.pro/u/c/puchi/200075R-Sajo-Yukimi-Cool.png'), (149L, u'Sakakibara Satomi', u'//i.cinderella.pro/u/c/puchi/100195R-Sakakibara-Satomi-Cute.png'), (159L, u'Sakuma Mayu', u'//i.cinderella.pro/u/c/puchi/100089R-Sakuma-Mayu-Cute.png'), (115L, u'Sakurai Momoka', u'//i.cinderella.pro/u/c/puchi/100127N-Sakurai-Momoka-Cute.png'), (180L, u'Sasaki Chie', u'//i.cinderella.pro/u/c/puchi/200017N-Sasaki-Chie-Cool.png'), (297L, u'Sato Shin', u'//i.cinderella.pro/u/c/puchi/300241R-Sato-Shin-Passion.png'), (241L, u'Sawada Marina', u'//i.cinderella.pro/u/c/puchi/300271N-Sawada-Marina-Passion.png'), (119L, u'Seki Hiromi', u'//i.cinderella.pro/u/c/puchi/100197N-Seki-Hiromi-Cute.png'), (203L, u'Sena Shiori', u'//i.cinderella.pro/u/c/puchi/200287R-Sena-Shiori-Cool.png'), (269L, u'Senzaki Ema', u'//i.cinderella.pro/u/c/puchi/300081R-Senzaki-Ema-Passion.png'), (167L, u'Shibuya Rin', u'//i.cinderella.pro/u/c/puchi/200001R-Shibuya-Rin-Cool.png'), (105L, u'Shiina Noriko', u'//i.cinderella.pro/u/c/puchi/100067N-Shiina-Noriko-Cute.png'), (101L, u'Shimamura Uzuki', u'//i.cinderella.pro/u/c/puchi/100001R-Shimamura-Uzuki-Cute.png'), (210L, u'Shinohara Rei', u'//i.cinderella.pro/u/c/puchi/220249R-Shinohara-Rei-Cool.png'), (220L, u'Shiomi Syuko', u'//i.cinderella.pro/u/c/puchi/200085N-Shiomi-Syuko-Cool.png'), (161L, u'Shiragiku Hotaru', u'//i.cinderella.pro/u/c/puchi/100119R-Shiragiku-Hotaru-Cute.png'), (214L, u'Shirasaka Koume', u'//i.cinderella.pro/u/c/puchi/200083R-Shirasaka-Koume-Cool.png'), (274L, u'Soma Natsumi', u'//i.cinderella.pro/u/c/puchi/300261N-Soma-Natsumi-Passion.png'), (285L, u'Sugisaka Umi', u'//i.cinderella.pro/u/c/puchi/320209N-Sugisaka-Umi-Passion.png'), (299L, u'Suzumiya Seika', u'//i.cinderella.pro/u/i/QRp1UCSuzumiya-Seika.png'), (295L, u'Syuto Aoi', u'//i.cinderella.pro/u/c/puchi/300167N-Syuto-Aoi-Passion.png'), (188L, u'Tachibana Arisu', u'//i.cinderella.pro/u/c/puchi/200067N-Tachibana-Arisu-Cool.png'), (178L, u'Tada Riina', u'//i.cinderella.pro/u/c/puchi/200015N-Tada-Riina-Cool.png'), (197L, u'Takagaki Kaede', u'//i.cinderella.pro/u/c/puchi/200023R-Takagaki-Kaede-Cool.png'), (171L, u'Takahashi Reiko', u'//i.cinderella.pro/u/c/puchi/200245R-Takahashi-Reiko-Cool.png'), (301L, u'Takamine Noa', u'//i.cinderella.pro/u/i/RKuEPYTakamine-Noa.png'), (235L, u'Takamori Aiko', u'//i.cinderella.pro/u/c/puchi/300003N-Takamori-Aiko-Passion.png'), (177L, u'Togo Ai', u'//i.cinderella.pro/u/c/puchi/200171N-Togo-Ai-Cool.png'), (272L, u'Totoki Airi', u'//i.cinderella.pro/u/c/puchi/300035R-Totoki-Airi-Passion.png'), (294L, u'Tsuchiya Ako', u'//i.cinderella.pro/u/c/puchi/300153R-Tsuchiya-Ako-Passion.png'), (138L, u'Tsukimiya Miyabi', u'//i.cinderella.pro/u/c/puchi/100183R-Tsukimiya-Miyabi-Cute.png'), (250L, u'Ueda Suzuho', u'//i.cinderella.pro/u/c/puchi/300195N-Ueda-Suzuho-Passion.png'), (216L, u'Ujiie Mutsumi', u'//i.cinderella.pro/u/c/puchi/220211N-Ujiie-Mutsumi-Cool.png'), (213L, u'Umeki Otoha', u'//i.cinderella.pro/u/c/puchi/200187R-Umeki-Otoha-Cool.png'), (266L, u'Wakabayashi Tomoka', u'//i.cinderella.pro/u/c/puchi/300083R-Wakabayashi-Tomoka-Passion.png'), (221L, u'Wakiyama Tamami', u'//i.cinderella.pro/u/c/puchi/200111R-Wakiyama-Tamami-Cool.png'), (211L, u'Wakui Rumi', u'//i.cinderella.pro/u/c/puchi/200207R-Wakui-Rumi-Cool.png'), (190L, u'Yagami Makino', u'//i.cinderella.pro/u/c/puchi/200127R-Yagami-Makino-Cool.png'), (242L, u'Yaguchi Miu', u'//i.cinderella.pro/u/c/puchi/300103N-Yaguchi-Miu-Passion.png'), (228L, u'Yamato Aki', u'//i.cinderella.pro/u/c/puchi/200125R-Yamato-Aki-Cool.png'), (145L, u'Yanagi Kiyora', u'//i.cinderella.pro/u/c/puchi/100277R-Yanagi-Kiyora-Cute.png'), (306L, u'Yanase Miyuki', u'//i.cinderella.pro/u/i/ODZ7UTYanase-Miyuki.png'), (135L, u'Yao Feifei', u'//i.cinderella.pro/u/c/puchi/100207R-Yao-Feifei-Cute.png'), (118L, u'Yokoyama Chika', u'//i.cinderella.pro/u/c/puchi/100109N-Yokoyama-Chika-Cute.png'), (262L, u'Yorita Yoshino', u'//i.cinderella.pro/u/c/puchi/300141N-Yorita-Yoshino-Passion.png'), (212L, u'Yoshioka Saki', u'//i.cinderella.pro/u/c/puchi/200255N-Yoshioka-Saki-Cool.png'), (229L, u'Yuki Haru', u'//i.cinderella.pro/u/c/puchi/200141R-Yuki-Haru-Cool.png'), (124L, u'Yusa Kozue', u'//i.cinderella.pro/u/c/puchi/100283R-Yusa-Kozue-Cute.png'), (300L, u'Zaizen Tokiko', u'//i.cinderella.pro/u/i/t7jtb7Zaizen-Tokiko.png')]
STARTERS = [(100001L, u'Shimamura Uzuki', u'//i.cinderella.pro/u/c/icon/100001R-Shimamura-Uzuki-Cute.png'), (200001L, u'Shibuya Rin', u'//i.cinderella.pro/u/c/icon/200001R-Shibuya-Rin-Cool.png'), (300001L, u'Honda Mio', u'//i.cinderella.pro/u/c/icon/300001R-Honda-Mio-Passion.png')]
MAX_STATS = {'visual_awakened_max': 7089L, 'dance_awakened_max': 7089L, 'vocal_awakened_max': 7089L, 'overall_max': 12574L, 'overall_awakened_max': 15291L, 'hp_max': 42L, 'visual_max': 5830L, 'hp_awakened_max': 44L, 'dance_max': 5830L, 'vocal_max': 5830L}
GENERATED_DATE = datetime.datetime.fromtimestamp(1478047116.09)