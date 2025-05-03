from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file_input import FileInput

from playwright.sync_api import Page, expect


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier = identifier

        self.preview_empty_view = EmptyViewComponent(page, identifier="create-course-preview")
        
        self.preview_image = Image(page, '{identifier}-image-upload-widget-preview-image', 'Preview image')

        self.image_upload_info_icon = Icon(page, '{identifier}-image-upload-widget-info-icon', 'Upload image icon')
        self.image_upload_info_title = Text(page, '{identifier}-image-upload-widget-info-title-text', 'Upload image title')
        self.image_upload_info_description = Text(page, '{identifier}-image-upload-widget-info-description-text', 'Upload image description')

        self.upload_button = Button(page, '{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button = Button(page, '{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input = FileInput(page, '{identifier}-image-upload-widget-input', 'Upload input')

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible(identifier=self.identifier)

        self.image_upload_info_title.check_visible(identifier=self.identifier)
        self.image_upload_info_title.check_have_text(text='Tap on "Upload image" button to select file', identifier=self.identifier)

        self.image_upload_info_description.check_visible(identifier=self.identifier)
        self.image_upload_info_description.check_have_text(text='Recommended file size 540X300', identifier=self.identifier)

        self.upload_button.check_visible(identifier=self.identifier)

        if is_image_uploaded:
            self.remove_button.check_visible(identifier=self.identifier)
            self.preview_image.check_visible(identifier=self.identifier)

        if not is_image_uploaded:
            # Если картинка yt загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here',
            )
            
    def click_remove_image_button(self):
        self.remove_button.click(identifier=self.identifier)

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file, identifier=self.identifier)
