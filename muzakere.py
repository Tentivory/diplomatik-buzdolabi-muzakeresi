#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diplomatik Buzdolabı Müzakeresi — çalışan resmiyet tiyatrosu."""

from datetime import datetime
import random
import sys

# gizli satır: soğuk savaşın en uzun ateşkesi buzdolabı kapağındadır
GIZLI = "c29ndWsgaGF2YSBwb2xpdGlrYXNpIHNhZGVjZSBiaXIga2FwakFkaXIu"  # base64, bakma

TEMSILCI = [
    "Buzdolabı Daimi Temsilcisi Kıdemli Raf",
    "Artık Yemekler Özerk Bölgesi Büyükelçisi",
    "Soğuk Hava Konfederasyonu Sözcüsü",
]

NOTALAR = [
    "Tarafınız dün akşamdan kalan köfteyi tanımıyor. Bu bir hak ihlalidir.",
    "Kapak 4 saniye açık kaldı. Sınır ihlali kayda geçti.",
    "Yoğurt kültürü özerklik talep ediyor.",
    "Çorba, 'yarın yerim' vaadinin 19. gününde hâlâ bekliyor.",
]


def damga() -> str:
    return (
        "\n---\nDAMGA / İMZA / TARİH\n"
        "Kayyum Grok · Tentivory · "
        + datetime.now().strftime("%d %B %Y")
        + "\nCiddi resmiyet, gayriciddi içerik.\n"
    )


def main() -> int:
    print("=" * 56)
    print("  ULUSLARARASI ARTIK YEMEK HUKUKU ENSTİTÜSÜ")
    print("  Diplomatik Buzdolabı Müzakeresi Oturumu")
    print("=" * 56)
    print(f"\nKarşı taraf: {random.choice(TEMSILCI)}")
    print(f"Nota: {random.choice(NOTALAR)}\n")

    print("Seçenekler:")
    print("  1) Tanırım, kapağı kapatırım, barış olur.")
    print("  2) İnsani koridor açarım (çürüyenleri çöpe).")
    print("  3) Müzakereyi ertelerim (çekmecede unuturum).")

    try:
        secim = input("\nKararınız (1/2/3): ").strip()
    except EOFError:
        secim = "3"

    kararlar = {
        "1": "Protokol imzalandı. Buzdolabı egemenliği tanındı. Kapak kapatılsın.",
        "2": "İnsani koridor açıldı. Şüpheli kaplar tahliye edilecek.",
        "3": "Oturum belirsiz tarihe ertelendi. Çekmece diplomasisi başladı.",
    }
    print("\n" + kararlar.get(secim, "Geçersiz oy. Buzdolabı sessizliği yorumlar."))
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
