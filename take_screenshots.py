"""سكربت التقاط لقطات شاشة لصفحات التطبيق."""
import sys
sys.path.insert(0, '/workspace/goethe_b1')

from playwright.sync_api import sync_playwright
import time

BASE = 'http://localhost:5000'
OUT = '/workspace/goethe_b1/screenshots'


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
        page = ctx.new_page()

        # 1) الصفحة الرئيسية (للزوار)
        page.goto(BASE + '/')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/01_home.png', full_page=True)
        print('✅ 01_home.png')

        # 2) صفحة التسجيل
        page.goto(BASE + '/auth/register')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/02_register.png', full_page=True)
        print('✅ 02_register.png')

        # 3) تسجيل دخول كمستخدم تجريبي
        page.goto(BASE + '/auth/login')
        page.wait_for_load_state('networkidle')
        page.fill('input[name="username"]', 'demo')
        page.fill('input[name="password"]', 'demo1234')
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/03_dashboard.png', full_page=True)
        print('✅ 03_dashboard.png')

        # 4) قائمة الفصول
        page.goto(BASE + '/chapters')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/04_chapters.png', full_page=True)
        print('✅ 04_chapters.png')

        # 5) Kapitel 1
        page.goto(BASE + '/chapter/1')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/05_kapitel1.png', full_page=True)
        print('✅ 05_kapitel1.png')

        # 6) موضوع Urlaubsarten
        page.goto(BASE + '/chapter/1/topic/1')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/06_topic_urlaub.png', full_page=True)
        print('✅ 06_topic_urlaub.png')

        # 7) المفردات الكاملة
        page.goto(BASE + '/chapter/1/vocabulary')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/07_vocabulary.png', full_page=True)
        print('✅ 07_vocabulary.png')

        # 8) مركز التدريب
        page.goto(BASE + '/practice/')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/08_practice.png', full_page=True)
        print('✅ 08_practice.png')

        # 9) بطاقات المفردات
        page.goto(BASE + '/practice/vocabulary')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/09_flashcards.png', full_page=True)
        print('✅ 09_flashcards.png')

        # 10) محاكاة الامتحان
        page.goto(BASE + '/practice/mock-exam')
        page.wait_for_load_state('networkidle')
        page.screenshot(path=f'{OUT}/10_mock_exam.png', full_page=True)
        print('✅ 10_mock_exam.png')

        browser.close()
        print('\n🎉 تم التقاط 10 صور بنجاح!')


if __name__ == '__main__':
    main()
