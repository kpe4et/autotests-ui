import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
        @allure.title("Check displaying of empty courses list")
        def test_empty_courses_list(self, courses_list_page: CoursesListPage):
                
                courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

                courses_list_page.navbar.check_visible('username')
                courses_list_page.sidebar.check_visible()
                courses_list_page.toolbar_view.check_visible()
                courses_list_page.check_visible_empty_view()

        @allure.title("Create course")
        def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
                
                # Проверяем страницу создания курса
                create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

                # Проверим отображение формы
                create_course_page.create_course_toolbar_view.check_visible()
                create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
                create_course_page.create_course_form.check_visible(
                        title='', estimated_time='', description='', max_score='0', min_score='0'
                )
                
                # Проверяем блоки создания заданий
                create_course_page.create_course_exercises_toolbar_view.check_visible()
                create_course_page.check_visible_exercises_empty_view()
                
                # Заполняем данные курса и создаем его
                create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
                create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
                
                # Проверим, что поля содержат корректные данные и перейдем создадим курс
                create_course_page.create_course_form.fill(
                        title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
                )
                create_course_page.create_course_form.check_visible(
                        title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
                )
                create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
                create_course_page.create_course_toolbar_view.click_create_course_button()

                # Проверяем данные созданного курса
                courses_list_page.toolbar_view.check_visible()
                courses_list_page.course_view.check_visible(
                        index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
                )

        @allure.title("Edit course")
        def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
                create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
                create_course_page.create_course_form.fill(
                        title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
                )
                create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
                create_course_page.create_course_toolbar_view.click_create_course_button()


                courses_list_page.course_view.check_visible(
                        index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
                )
                courses_list_page.course_view.menu.click_edit(index=0)

                create_course_page.create_course_form.fill(
                        title='Python', estimated_time='Eternity', description='Python', max_score='100', min_score='1'
                )
                create_course_page.create_course_toolbar_view.click_create_course_button()

                courses_list_page.course_view.check_visible(
                        index=0, title='Python', estimated_time='Eternity', max_score='100', min_score='1'
                )
