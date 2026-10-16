import re
p='C:/Users/vota2/sites/fenix-fitness/index.html'
s=open(p,encoding='utf-8').read()

# 1) hero background becomes photo 1
s=s.replace('src="assets/photos/avatar.jpg" alt="Fenix club"', 'src="assets/photos/1.jpg" alt="Fenix Fitness Club"')

# 2) trainers section replacement
start=s.find('id="trainers"')
pre=s[:start]
# keep imports before id; find section start earlier
sec_start=s.rfind('<section id="trainers"', 0, start+1)
pre=s[:sec_start]
# find end of this section
end_marker='</div></div></section>'
end=s.find(end_marker, start)+len(end_marker)
suffix=s[end:]

new_trainers='''
<section id="trainers" class="reveal"><div class="shell"><div class="section-head"><span class="eyebrow">Команда</span><h2 class="section-title">Тренеры</h2><p>Реальные тренеры, которых вы найдёте в группе. Фото взяты из папки 1–12 (связка по вашим описаниям).</p></div>
<div class="trainers-grid">
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/1.jpg" alt="Тренер 1" loading="lazy"></div><div class="trainer-name">Тренер №1</div><div class="trainer-role">Персональный тренер</div><div class="trainer-note">Сильный тренерский состав, личная консультация. Цена 700 ₽.</div><div class="trainer-price">700 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/2.jpg" alt="Екатерина" loading="lazy"></div><div class="trainer-name">Екатерина</div><div class="trainer-role">ЖИРОТОП — групповое направление</div><div class="trainer-note">«Я стройная, изящная, красивая!» Мощные тренировки, хорошее настроение, мотивация. vk.com/katibelaya</div><div class="trainer-price">400 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/3.jpg" alt="Андрей" loading="lazy"></div><div class="trainer-name">Андрей</div><div class="trainer-role">Персональный тренер</div><div class="trainer-note">Сильный и надёжный наставник. Консультирует по питанию. «Большая радость и гордость за моих людей».</div><div class="trainer-price">700 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/4.jpg" alt="Елена" loading="lazy"></div><div class="trainer-name">Елена</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/id96272356. Подходит для результативной работы.</div><div class="trainer-price">500 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/5.jpg" alt="Тренер-реабилитолог" loading="lazy"></div><div class="trainer-name">Тренер-реабилитолог</div><div class="trainer-role">Оздоровительный фитнес</div><div class="trainer-note">Восстановление после травм и боли (спина, шея, суставы). Высшее УралГУФК, среднее мед. VK: vk.com/slbdnkv</div><div class="trainer-price">800 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/6.jpg" alt="Алексей Протеинов" loading="lazy"></div><div class="trainer-name">Алексей Протеинов</div><div class="trainer-role">Тренажёрный зал / пауэрлифтинг</div><div class="trainer-note">Опыт с 2019, жим лежа 195 кг. Образование: курсы, н/в высшее химик-аналитик. vk.com/alex_proteinov</div><div class="trainer-price">700 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/7.jpg" alt="Александр" loading="lazy"></div><div class="trainer-name">Александр</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/id39329790. Персональная тренировка 800–1000 ₽.</div><div class="trainer-price">800 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/8.jpg" alt="Вероника" loading="lazy"></div><div class="trainer-name">Вероника</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/brod_ve</div><div class="trainer-price">700 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/9.jpg" alt="Олеся" loading="lazy"></div><div class="trainer-name">Олеся</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/ololees</div><div class="trainer-price">600 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/10.jpg" alt="Светлана Чуканова" loading="lazy"></div><div class="trainer-name">Светлана Чуканова</div><div class="trainer-role">Директор / тренер</div><div class="trainer-note">IFBB, МС. Поддержка питания на удалёнке. Тренер ряда спортсменов.</div><div class="trainer-price">По запросу</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/11.jpg" alt="Виктор" loading="lazy"></div><div class="trainer-name">Виктор</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/victorthedreamer. На связи по ЛС.</div><div class="trainer-price">700 ₽</div></article>
<article class="trainer"><div class="trainer-avatar"><img src="assets/photos/12.jpg" alt="Светлана" loading="lazy"></div><div class="trainer-name">Светлана</div><div class="trainer-role">Твой персональный тренер</div><div class="trainer-note">VK: vk.com/id59910648. Часы 8:00–19:00.</div><div class="trainer-price">700 ₽</div></article>
</div></div></section>
'''
s=pre+new_trainers+suffix

# add avatar img style for trainers
s=s.replace('.trainer-avatar{', '.trainer-avatar{position:relative;')
s=s.replace('.trainer-avatar .initials{', '.trainer-avatar img{width:100%;height:100%;object-fit:cover;display:block;}\n.trainer-avatar .initials{')

# review authors without spans/badges
s=s.replace(' <span>Яндекс</span>', '')
s=s.replace(' <span>2ГИС</span>', '')
s=s.replace(' <span>ВКонтакте</span>', '')

open(p,'w',encoding='utf-8').write(s)
print("done")