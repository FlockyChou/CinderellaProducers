import datetime
TOTAL_DONATORS = 0
LATEST_NEWS = [{'url': u'/event/2/LIVE-Party/', 'hide_title': True, 'image': u'//i.cinderella.pro/u/e/NoneLIVE-Party.png', 'ajax': u'/ajax/event/2/', 'title': u'LIVE Party'}]
FAVORITE_CHARACTERS = [(154, u'Abe Nana', u'//i.cinderella.pro/u/c/puchi/100037R-Abe-Nana-Cute.png'), (263, u'Aiba Yumi', u'//i.cinderella.pro/u/c/puchi/300089N-Aiba-Yumi-Passion.png'), (172, u'Aikawa Chinatsu', u'//i.cinderella.pro/u/c/puchi/200005N-Aikawa-Chinatsu-Cool.png'), (244, u'Aino Nagisa', u'//i.cinderella.pro/u/c/puchi/300237N-Aino-Nagisa-Passion.png'), (243, u'Akagi Miria', u'//i.cinderella.pro/u/c/puchi/300013N-Akagi-Miria-Passion.png'), (227, u'Anastasia', u'//i.cinderella.pro/u/c/puchi/200039R-Anastasia-Cool.png'), (151, u'Anzai Miyako', u'//i.cinderella.pro/u/c/puchi/100273N-Anzai-Miyako-Cute.png'), (176, u'Araki Hina', u'//i.cinderella.pro/u/c/puchi/200013N-Araki-Hina-Cool.png'), (163, u'Ariura Kanna', u'//i.cinderella.pro/u/c/puchi/100221R-Ariura-Kanna-Cute.png'), (192, u'Asari Nanami', u'//i.cinderella.pro/u/c/puchi/220225N-Asari-Nanami-Cool.png'), (204, u'Ayase Honoka', u'//i.cinderella.pro/u/c/puchi/200077R-Ayase-Honoka-Cool.png'), (158, u'Clarice', u'//i.cinderella.pro/u/c/puchi/100105R-Clarice-Cute.png'), (141, u'Domyoji Karin', u'//i.cinderella.pro/u/c/puchi/100079R-Domyoji-Karin-Cute.png'), (255, u'Eto Misaki', u'//i.cinderella.pro/u/c/puchi/300257R-Eto-Misaki-Passion.png'), (219, u'Fujii Tomo', u'//i.cinderella.pro/u/c/puchi/200177R-Fujii-Tomo-Cool.png'), (122, u'Fujimoto Rina', u'//i.cinderella.pro/u/c/puchi/100071N-Fujimoto-Rina-Cute.png'), (184, u'Fujiwara Hajime', u'//i.cinderella.pro/u/c/puchi/200135N-Fujiwara-Hajime-Cool.png'), (104, u'Fukuyama Mai', u'//i.cinderella.pro/u/c/puchi/100069N-Fukuyama-Mai-Cute.png'), (187, u'Furusawa Yoriko', u'//i.cinderella.pro/u/c/puchi/200267R-Furusawa-Yoriko-Cool.png'), (134, u'Futaba Anzu', u'//i.cinderella.pro/u/c/puchi/100027R-Futaba-Anzu-Cute.png'), (292, u'Hamaguchi Ayame', u'//i.cinderella.pro/u/c/puchi/300093R-Hamaguchi-Ayame-Passion.png'), (165, u'Harada Miyo', u'//i.cinderella.pro/u/c/puchi/100133R-Harada-Miyo-Cute.png'), (223, u'Hayami Kanade', u'//i.cinderella.pro/u/c/puchi/200037R-Hayami-Kanade-Cool.png'), (162, u'Hayasaka Mirei', u'//i.cinderella.pro/u/c/puchi/100143R-Hayasaka-Mirei-Cute.png'), (247, u'Himekawa Yuki', u'//i.cinderella.pro/u/c/puchi/300017N-Himekawa-Yuki-Passion.png'), (270, u'Hino Akane', u'//i.cinderella.pro/u/c/puchi/300031R-Hino-Akane-Passion.png'), (201, u'Hojo Karen', u'//i.cinderella.pro/u/c/puchi/200027R-Hojo-Karen-Cool.png'), (234, u'Honda Mio', u'//i.cinderella.pro/u/c/puchi/300001R-Honda-Mio-Passion.png'), (258, u'Hori Yuko', u'//i.cinderella.pro/u/c/puchi/300021N-Hori-Yuko-Passion.png'), (256, u'Hoshi Syoko', u'//i.cinderella.pro/u/c/puchi/300069N-Hoshi-Syoko-Passion.png'), (139, u'Hyodo Rena', u'//i.cinderella.pro/u/c/puchi/100129R-Hyodo-Rena-Cute.png'), (283, u'Ichihara Nina', u'//i.cinderella.pro/u/c/puchi/300113R-Ichihara-Nina-Passion.png'), (126, u'Ichinose Shiki', u'//i.cinderella.pro/u/c/puchi/100087N-Ichinose-Shiki-Cute.png'), (113, u'Igarashi Kyoko', u'//i.cinderella.pro/u/c/puchi/100099N-Igarashi-Kyoko-Cute.png'), (106, u'Imai Kana', u'//i.cinderella.pro/u/c/puchi/100141N-Imai-Kana-Cute.png'), (147, u'Imura Setsuna', u'//i.cinderella.pro/u/c/puchi/100131R-Imura-Setsuna-Cute.png'), (267, u'Jougasaki Mika', u'//i.cinderella.pro/u/c/puchi/300027R-Jougasaki-Mika-Passion.png'), (268, u'Jougasaki Rika', u'//i.cinderella.pro/u/c/puchi/300029R-Jougasaki-Rika-Passion.png'), (175, u'Kamijo Haruna', u'//i.cinderella.pro/u/c/puchi/200011N-Kamijo-Haruna-Cool.png'), (174, u'Kamiya Nao', u'//i.cinderella.pro/u/c/puchi/200009N-Kamiya-Nao-Cool.png'), (198, u'Kanzaki Ranko', u'//i.cinderella.pro/u/c/puchi/200025R-Kanzaki-Ranko-Cool.png'), (257, u'Katagiri Sanae', u'//i.cinderella.pro/u/c/puchi/300073N-Katagiri-Sanae-Passion.png'), (202, u'Kate', u'//i.cinderella.pro/u/c/puchi/200029R-Kate-Cool.png'), (173, u'Kawashima Mizuki', u'//i.cinderella.pro/u/c/puchi/200007N-Kawashima-Mizuki-Cool.png'), (183, u'Kiba Manami', u'//i.cinderella.pro/u/c/puchi/220231R-Kiba-Manami-Cool.png'), (238, u'Kimura Natsuki', u'//i.cinderella.pro/u/c/puchi/300009N-Kimura-Natsuki-Passion.png'), (170, u'Kirino Aya', u'//i.cinderella.pro/u/c/puchi/200273N-Kirino-Aya-Cool.png'), (284, u'Kita Hinako', u'//i.cinderella.pro/u/c/puchi/300121R-Kita-Hinako-Passion.png'), (286, u'Kitagawa Mahiro', u'//i.cinderella.pro/u/c/puchi/300211R-Kitagawa-Mahiro-Passion.png'), (249, u'Kitami Yuzu', u'//i.cinderella.pro/u/c/puchi/300127N-Kitami-Yuzu-Passion.png'), (132, u'Kobayakawa Sae', u'//i.cinderella.pro/u/c/puchi/100023R-Kobayakawa-Sae-Cute.png'), (111, u'Kohinata Miho', u'//i.cinderella.pro/u/c/puchi/100013N-Kohinata-Miho-Cute.png'), (288, u'Komatsu Ibuki', u'//i.cinderella.pro/u/c/puchi/300189R-Komatsu-Ibuki-Passion.png'), (254, u'Koseki Reina', u'//i.cinderella.pro/u/c/puchi/300177R-Koseki-Reina-Passion.png'), (150, u'Koshimizu Sachiko', u'//i.cinderella.pro/u/c/puchi/100073R-Koshimizu-Sachiko-Cute.png'), (155, u'Kudo Shinobu', u'//i.cinderella.pro/u/c/puchi/100113R-Kudo-Shinobu-Cute.png'), (156, u'Kurihara Nene', u'//i.cinderella.pro/u/c/puchi/100247R-Kurihara-Nene-Cute.png'), (168, u'Kurokawa Chiaki', u'//i.cinderella.pro/u/c/puchi/200003N-Kurokawa-Chiaki-Cool.png'), (191, u'Layla', u'//i.cinderella.pro/u/c/puchi/200161R-Layla-Cool.png'), (127, u'Maekawa Miku', u'//i.cinderella.pro/u/c/puchi/100019R-Maekawa-Miku-Cute.png'), (275, u'Makihara Shiho', u'//i.cinderella.pro/u/c/puchi/300255R-Makihara-Shiho-Passion.png'), (287, u'Mary Cochran', u'//i.cinderella.pro/u/c/puchi/300099R-Mary-Cochran-Passion.png'), (260, u'Matoba Risa', u'//i.cinderella.pro/u/c/puchi/300155N-Matoba-Risa-Passion.png'), (129, u'Matsubara Saya', u'//i.cinderella.pro/u/c/puchi/100217R-Matsubara-Saya-Cute.png'), (169, u'Matsumoto Sarina', u'//i.cinderella.pro/u/c/puchi/200069N-Matsumoto-Sarina-Cool.png'), (194, u'Matsunaga Ryo', u'//i.cinderella.pro/u/c/puchi/200021R-Matsunaga-Ryo-Cool.png'), (239, u'Matsuyama Kumiko', u'//i.cinderella.pro/u/c/puchi/300011N-Matsuyama-Kumiko-Passion.png'), (181, u'Mifune Miyu', u'//i.cinderella.pro/u/c/puchi/200123N-Mifune-Miyu-Cool.png'), (108, u'Mimura Kanako', u'//i.cinderella.pro/u/c/puchi/100007N-Mimura-Kanako-Cute.png'), (131, u'Miyamoto Frederica', u'//i.cinderella.pro/u/c/puchi/100021R-Miyamoto-Frederica-Cute.png'), (289, u'Miyoshi Sana', u'//i.cinderella.pro/u/c/puchi/300157R-Miyoshi-Sana-Passion.png'), (179, u'Mizuki Seira', u'//i.cinderella.pro/u/c/puchi/200155N-Mizuki-Seira-Cool.png'), (103, u'Mizumoto Yukari', u'//i.cinderella.pro/u/c/puchi/100065N-Mizumoto-Yukari-Cute.png'), (186, u'Mizuno Midori', u'//i.cinderella.pro/u/c/puchi/200185R-Mizuno-Midori-Cool.png'), (107, u'Mochida Arisa', u'//i.cinderella.pro/u/c/puchi/100005N-Mochida-Arisa-Cute.png'), (136, u'Momoi Azuki', u'//i.cinderella.pro/u/c/puchi/100081R-Momoi-Azuki-Cute.png'), (226, u'Morikubo Nono', u'//i.cinderella.pro/u/c/puchi/200119R-Morikubo-Nono-Cool.png'), (271, u'Moroboshi Kirari', u'//i.cinderella.pro/u/c/puchi/300033R-Moroboshi-Kirari-Passion.png'), (280, u'Mukai Takumi', u'//i.cinderella.pro/u/c/puchi/300105R-Mukai-Takumi-Passion.png'), (121, u'Munakata Atsumi', u'//i.cinderella.pro/u/c/puchi/100159N-Munakata-Atsumi-Cute.png'), (293, u'Murakami Tomoe', u'//i.cinderella.pro/u/c/puchi/300129R-Murakami-Tomoe-Passion.png'), (160, u'Muramatsu Sakura', u'//i.cinderella.pro/u/c/puchi/100151R-Muramatsu-Sakura-Cute.png'), (102, u'Nakano Yuka', u'//i.cinderella.pro/u/c/puchi/100003N-Nakano-Yuka-Cute.png'), (236, u'Namiki Meiko', u'//i.cinderella.pro/u/c/puchi/300199R-Namiki-Meiko-Passion.png'), (291, u'Nanba Emi', u'//i.cinderella.pro/u/c/puchi/300145R-Nanba-Emi-Passion.png'), (298, u'Nanjo Hikaru', u'//i.cinderella.pro/u/c/puchi/300245R-Nanjo-Hikaru-Passion.png'), (218, u'Narumiya Yume', u'//i.cinderella.pro/u/c/puchi/200195N-Narumiya-Yume-Cool.png'), (273, u'Natalia', u'//i.cinderella.pro/u/c/puchi/300075R-Natalia-Passion.png'), (230, u'Ninomiya Asuka', u'//i.cinderella.pro/u/c/puchi/200093R-Ninomiya-Asuka-Cool.png'), (259, u'Nishijima Kai', u'//i.cinderella.pro/u/c/puchi/300231R-Nishijima-Kai-Passion.png'), (185, u'Nitta Minami', u'//i.cinderella.pro/u/c/puchi/200019N-Nitta-Minami-Cool.png'), (112, u'Ogata Chieri', u'//i.cinderella.pro/u/c/puchi/100015N-Ogata-Chieri-Cute.png'), (253, u'Oikawa Shizuku', u'//i.cinderella.pro/u/c/puchi/300071N-Oikawa-Shizuku-Passion.png'), (222, u'Okazaki Yasuha', u'//i.cinderella.pro/u/c/puchi/200153R-Okazaki-Yasuha-Cool.png'), (109, u'Okuyama Saori', u'//i.cinderella.pro/u/c/puchi/100009N-Okuyama-Saori-Cute.png'), (123, u'Oohara Michiru', u'//i.cinderella.pro/u/c/puchi/100233N-Oohara-Michiru-Cute.png'), (224, u'Ooishi Izumi', u'//i.cinderella.pro/u/c/puchi/200145R-Ooishi-Izumi-Cool.png'), (153, u'Oonishi Yuriko', u'//i.cinderella.pro/u/c/puchi/100237R-Oonishi-Yuriko-Cute.png'), (125, u'Oonuma Kurumi', u'//i.cinderella.pro/u/c/puchi/100265R-Oonuma-Kurumi-Cute.png'), (120, u'Oota Yu', u'//i.cinderella.pro/u/c/puchi/100257N-Oota-Yu-Cute.png'), (246, u'Ootsuki Yui', u'//i.cinderella.pro/u/c/puchi/300015N-Ootsuki-Yui-Passion.png'), (164, u'Otokura Yuuki', u'//i.cinderella.pro/u/c/puchi/100213N-Otokura-Yuuki-Cute.png'), (237, u'Ryuzaki Kaoru', u'//i.cinderella.pro/u/c/puchi/300007N-Ryuzaki-Kaoru-Passion.png'), (189, u'Sagisawa Fumika', u'//i.cinderella.pro/u/c/puchi/200091N-Sagisawa-Fumika-Cool.png'), (133, u'Saionji Kotoka', u'//i.cinderella.pro/u/c/puchi/100025R-Saionji-Kotoka-Cute.png'), (240, u'Saito Yoko', u'//i.cinderella.pro/u/c/puchi/320223N-Saito-Yoko-Passion.png'), (205, u'Sajo Yukimi', u'//i.cinderella.pro/u/c/puchi/200075R-Sajo-Yukimi-Cool.png'), (149, u'Sakakibara Satomi', u'//i.cinderella.pro/u/c/puchi/100195R-Sakakibara-Satomi-Cute.png'), (159, u'Sakuma Mayu', u'//i.cinderella.pro/u/c/puchi/100089R-Sakuma-Mayu-Cute.png'), (115, u'Sakurai Momoka', u'//i.cinderella.pro/u/c/puchi/100127N-Sakurai-Momoka-Cute.png'), (180, u'Sasaki Chie', u'//i.cinderella.pro/u/c/puchi/200017N-Sasaki-Chie-Cool.png'), (297, u'Sato Shin', u'//i.cinderella.pro/u/c/puchi/300241R-Sato-Shin-Passion.png'), (119, u'Seki Hiromi', u'//i.cinderella.pro/u/c/puchi/100197N-Seki-Hiromi-Cute.png'), (269, u'Senzaki Ema', u'//i.cinderella.pro/u/c/puchi/300081R-Senzaki-Ema-Passion.png'), (167, u'Shibuya Rin', u'//i.cinderella.pro/u/c/puchi/200001R-Shibuya-Rin-Cool.png'), (105, u'Shiina Noriko', u'//i.cinderella.pro/u/c/puchi/100067N-Shiina-Noriko-Cute.png'), (101, u'Shimamura Uzuki', u'//i.cinderella.pro/u/c/puchi/100001R-Shimamura-Uzuki-Cute.png'), (210, u'Shinohara Rei', u'//i.cinderella.pro/u/c/puchi/220249R-Shinohara-Rei-Cool.png'), (220, u'Shiomi Syuko', u'//i.cinderella.pro/u/c/puchi/200085N-Shiomi-Syuko-Cool.png'), (161, u'Shiragiku Hotaru', u'//i.cinderella.pro/u/c/puchi/100119R-Shiragiku-Hotaru-Cute.png'), (214, u'Shirasaka Koume', u'//i.cinderella.pro/u/c/puchi/200083R-Shirasaka-Koume-Cool.png'), (274, u'Soma Natsumi', u'//i.cinderella.pro/u/c/puchi/300261N-Soma-Natsumi-Passion.png'), (285, u'Sugisaka Umi', u'//i.cinderella.pro/u/c/puchi/320209N-Sugisaka-Umi-Passion.png'), (295, u'Syuto Aoi', u'//i.cinderella.pro/u/c/puchi/300167N-Syuto-Aoi-Passion.png'), (188, u'Tachibana Arisu', u'//i.cinderella.pro/u/c/puchi/200067N-Tachibana-Arisu-Cool.png'), (178, u'Tada Riina', u'//i.cinderella.pro/u/c/puchi/200015N-Tada-Riina-Cool.png'), (197, u'Takagaki Kaede', u'//i.cinderella.pro/u/c/puchi/200023R-Takagaki-Kaede-Cool.png'), (171, u'Takahashi Reiko', u'//i.cinderella.pro/u/c/puchi/200245R-Takahashi-Reiko-Cool.png'), (235, u'Takamori Aiko', u'//i.cinderella.pro/u/c/puchi/300003N-Takamori-Aiko-Passion.png'), (177, u'Togo Ai', u'//i.cinderella.pro/u/c/puchi/200171N-Togo-Ai-Cool.png'), (272, u'Totoki Airi', u'//i.cinderella.pro/u/c/puchi/300035R-Totoki-Airi-Passion.png'), (294, u'Tsuchiya Ako', u'//i.cinderella.pro/u/c/puchi/300153R-Tsuchiya-Ako-Passion.png'), (138, u'Tsukimiya Miyabi', u'//i.cinderella.pro/u/c/puchi/100183R-Tsukimiya-Miyabi-Cute.png'), (250, u'Ueda Suzuho', u'//i.cinderella.pro/u/c/puchi/300195N-Ueda-Suzuho-Passion.png'), (216, u'Ujiie Mutsumi', u'//i.cinderella.pro/u/c/puchi/220211N-Ujiie-Mutsumi-Cool.png'), (213, u'Umeki Otoha', u'//i.cinderella.pro/u/c/puchi/200187R-Umeki-Otoha-Cool.png'), (266, u'Wakabayashi Tomoka', u'//i.cinderella.pro/u/c/puchi/300083R-Wakabayashi-Tomoka-Passion.png'), (221, u'Wakiyama Tamami', u'//i.cinderella.pro/u/c/puchi/200111R-Wakiyama-Tamami-Cool.png'), (211, u'Wakui Rumi', u'//i.cinderella.pro/u/c/puchi/200207R-Wakui-Rumi-Cool.png'), (190, u'Yagami Makino', u'//i.cinderella.pro/u/c/puchi/200127R-Yagami-Makino-Cool.png'), (242, u'Yaguchi Miu', u'//i.cinderella.pro/u/c/puchi/300103N-Yaguchi-Miu-Passion.png'), (228, u'Yamato Aki', u'//i.cinderella.pro/u/c/puchi/200125R-Yamato-Aki-Cool.png'), (145, u'Yanagi Kiyora', u'//i.cinderella.pro/u/c/puchi/100277R-Yanagi-Kiyora-Cute.png'), (135, u'Yao Feifei', u'//i.cinderella.pro/u/c/puchi/100207R-Yao-Feifei-Cute.png'), (118, u'Yokoyama Chika', u'//i.cinderella.pro/u/c/puchi/100109N-Yokoyama-Chika-Cute.png'), (262, u'Yorita Yoshino', u'//i.cinderella.pro/u/c/puchi/300141N-Yorita-Yoshino-Passion.png'), (212, u'Yoshioka Saki', u'//i.cinderella.pro/u/c/puchi/200255N-Yoshioka-Saki-Cool.png'), (229, u'Yuki Haru', u'//i.cinderella.pro/u/c/puchi/200141R-Yuki-Haru-Cool.png')]
STARTERS = [(100001, u'Shimamura Uzuki', u'//i.cinderella.pro/u/c/icon/100001R-Shimamura-Uzuki-Cute.png'), (200001, u'Shibuya Rin', u'//i.cinderella.pro/u/c/icon/200001R-Shibuya-Rin-Cool.png'), (300001, u'Honda Mio', u'//i.cinderella.pro/u/c/icon/300001R-Honda-Mio-Passion.png')]
MAX_STATS = {'visual_awakened_max': 7089, 'dance_awakened_max': 7089, 'vocal_awakened_max': 7089, 'overall_max': 12574, 'overall_awakened_max': 15291, 'hp_max': 40, 'visual_max': 5830, 'hp_awakened_max': 42, 'dance_max': 5830, 'vocal_max': 5830}
GENERATED_DATE = datetime.datetime.fromtimestamp(1474224161.1)
