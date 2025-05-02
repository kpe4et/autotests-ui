from playwright.sync_api import Page, expect

from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.navigation.navbar_component import NavbarComponent
from components.courses.create_course_exercise_form_component import CourseExercisesFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.excercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_exercise_form = CourseExercisesFormComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)
        

    def check_visible_exercises_empty_view(self):
        self.excercises_empty_view.check_visible(title="There is no exercises", description='Click on "Create exercise" button to create new exercise')

