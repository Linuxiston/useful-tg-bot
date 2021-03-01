import random

quotes_from_quran = [
    "«Namozni mukammal ado etingiz, zakot beringiz va ruku qiluvchilar bilan birga ruku qilingiz» (Baqara, 43).",
    "«Namozni mukammal ado etingiz va zakot beringiz!» (Baqara, 110).",
    "«Alloh imonlaringizni (Baytul-Maqdisga qarab o‘qigan namozlaringiz ajrini) zoe ketkizmas. Albatta, Alloh odamlarga mehribon va rahmlidir» (Baqara, 143).",
    "«(Ey Muhammad), imon keltirgan bandalarimga ayting, namozni mukammal ado etsinlar hamda savdo-sotiq va oshna-og‘aynigarchilik bo‘lmaydigan Kun (qiyomat) kelmay turib, Biz ularga rizq qilib bergan narsalardan xufyona va oshkora ehson qilsinlar!» (Ibrohim, 31).",
    'Quyosh og‘ishidan to tun qorong‘usigacha namozni mukammal ado qiling va tonggi o‘qishni (bomdod namozini) ham (ado qiling). Zero, tonggi o‘qish (farishtalar) hozir bo‘ladigan (namoz)dir. Tunda (bir qismida) uyg‘onib o‘zingiz uchun tahajjud (nafl) namozini o‘qing! Shoyadki, Rabbingiz Sizni (Qiyomat kunida) maqtovli (shafoat qiladigan maqomda) tiriltirsa» (Al-Isro, 78­79).',
    "«Ahlingizni namoz (o‘qish)ga buyuring va (o‘zingiz ham) unga (namozga) bardoshli bo‘ling!» (Toha, 132).",
    "«Darhaqiqat, mo‘minlar najot topdilar. Ular namozlarga (qo‘rquv va umid bilan) bo‘yin eguvchi kishilardirlar. Ular (barcha) namozlarni (vaqtida ado etib qazo bo‘lishdan) saqlaguvchi kishilardir» (Mo‘minlar, 1­2, 9).",
    "«Albatta, namoz fahsh va yomonlikdan qaytarur! Albatta, Allohning zikri (barcha narsadan) ulug‘dir!» (Ankabut, 45).",
    "«Bas (ey, Muhammad), ular (kofirlar) aytayotgan so‘zlarga sabr qiling va Quyosh chiqishidan va botishidan avval Rabbingizga hamd bilan tasbeh ayting (namoz o‘qing)! Yana kechaning (bir qismida) va sajdalar (namozlar) ortidan tasbeh ayting!» (Qof, 39­40).",
    "«(Ey Muhammad,) Siz Rabbingizning hukmiga sabr qiling! Zotan, Siz Bizning ko‘z o‘ngimizda (himoyamizda)dirsiz! (Tongdan uyqudan) turgan paytingizda, Rabbingizga hamd bilan tasbeh ayting! Shuningdek, kechadan (vaqt ajratib) va yulduzlar yuz o‘girgach (botgach saharda) ham Unga tasbeh ayting» (Tur, 48-49).",
    "«Darhaqiqat, inson betoqat qilib yaratilgandir. Qachonki unga yomonlik (kambag‘allik yoki musibat) yetsa, u o‘ta besabrlik qiluvchidir. Qachonki unga yaxshilik (boylik, salomatlik) yetsa, u o‘ta man etuvchi (baxil)dir. Faqat namozxonlar bundan mustasnodirlar» (Maorij, 19­23)."
]

def pick_random_quote():
    return random.choice(quotes_from_quran)